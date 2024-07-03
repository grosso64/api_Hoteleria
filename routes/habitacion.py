# En routes/habitacion.py
from datetime import datetime
from sqlite3 import IntegrityError
from flask import Blueprint, app, request, jsonify
from klapi import db
from models.habitacion import Habitacion
from models.reserva import Reserva
from routes.auth import role_required
from schemas.habitacion import habitacion_schema, habitaciones_schema
from flask_jwt_extended import jwt_required

habitacion_bp = Blueprint('habitacion_bp', __name__)

@habitacion_bp.route('/habitaciones', methods=['POST'])
@jwt_required()
@role_required('Empleado')
def create_habitacion():
    data = request.get_json()
    numero = data.get('numero')
    precio_por_dia = data.get('precio_por_dia')

    if not numero or precio_por_dia is None:
        return jsonify({"message": "Faltan campos requeridos"}), 400

    try:
        precio_por_dia = float(precio_por_dia)
        if precio_por_dia < 0:
            raise ValueError("El precio por día no puede ser negativo")
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


    habitacion_existente = Habitacion.query.filter_by(numero=numero).first()
    if habitacion_existente:
        return jsonify({"message": "El número de habitación ya existe."}), 400

    habitacion = Habitacion(numero=numero, precio_por_dia=precio_por_dia)
    db.session.add(habitacion)

    try:
        db.session.commit()
        return habitacion_schema.jsonify(habitacion), 201
    except IntegrityError as e:
        db.session.rollback()
        if 'UNIQUE constraint failed' in str(e.orig):
            return jsonify({"message": "El número de habitación ya existe."}), 400
        app.logger.error('Error al crear habitación: %s', str(e))
        return jsonify({"message": "Error interno del servidor"}), 500
    except Exception as e:
        db.session.rollback()
        app.logger.error('Error al crear habitación: %s', str(e))
        return jsonify({"message": "Error interno del servidor"}), 500
    
@habitacion_bp.route('/habitaciones/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required('Empleado')
def delete_habitacion(id):
    habitacion = Habitacion.query.get(id)
    if not habitacion:
        return jsonify({"message": "Habitacion no encontrada"}), 404

    db.session.delete(habitacion)
    db.session.commit()
    return jsonify({"message": "Habitacion eliminada correctamente"}), 200


@habitacion_bp.route('/habitaciones/<int:numero>', methods=['PUT'])
@jwt_required()
@role_required('Empleado')
def update_habitacion(numero):
    habitacion = Habitacion.query.filter_by(numero=numero).first()
    if not habitacion:
        return jsonify({"message": "Habitacion no encontrada"}), 404

    data = request.get_json()
    precio_por_dia = data.get('precio_por_dia')

    if precio_por_dia is not None:
        try:
            precio_por_dia = float(precio_por_dia)
            if precio_por_dia < 0:
                raise ValueError("El precio por día no puede ser negativo")
        except ValueError as e:
            return jsonify({"message": str(e)}), 400
        habitacion.precio_por_dia = precio_por_dia

    habitacion.activa = data.get('activa', habitacion.activa)

    db.session.commit()
    return habitacion_schema.jsonify(habitacion)

@habitacion_bp.route('/habitaciones', methods=['GET'])
def get_habitaciones():
    habitaciones = Habitacion.query.all()
    return habitaciones_schema.jsonify(habitaciones)

@habitacion_bp.route('/habitaciones/<int:numero>', methods=['GET'])
@role_required('Empleado')
def get_habitacion(numero):
    habitacion = Habitacion.query.filter_by(numero=numero).first()
    if not habitacion:
        return jsonify({"message": "Habitacion no encontrada"}), 404

    return habitacion_schema.jsonify(habitacion)


@habitacion_bp.route('/habitaciones/buscar', methods=['GET'])
def buscar_habitaciones_rango():
    fecha_inicio_str = request.args.get('fecha_inicio')
    fecha_fin_str = request.args.get('fecha_fin')

    if not fecha_inicio_str or not fecha_fin_str:
        return jsonify({"message": "fecha no encontrada"}), 400

    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"message": "formato de fecha invalido. asi tiene que ser YYYY-MM-DD."}), 400

    subquery = db.session.query(Reserva.habitacion_id).filter(
        db.or_(
            db.and_(Reserva.fecha_inicio <= fecha_fin, Reserva.fecha_fin >= fecha_inicio),
            db.and_(Reserva.fecha_inicio <= fecha_inicio, Reserva.fecha_fin >= fecha_fin)
        )
    ).subquery()

    habitaciones = Habitacion.query.filter(Habitacion.id.notin_(subquery)).all()
    return habitaciones_schema.jsonify(habitaciones), 200
@habitacion_bp.route('/habitaciones/precio_menor', methods=['GET'])
@jwt_required()
def buscar_habitaciones_por_precio():
    precio_max = request.args.get('precio_max')
    if not precio_max:
        return jsonify({"message": "El precio máximo es requerido"}), 400

    try:
        precio_max = float(precio_max)
    except ValueError:
        return jsonify({"message": "El precio máximo debe ser un número"}), 400

    habitaciones = Habitacion.query.filter(Habitacion.precio_por_dia <= precio_max).all()
    resultado = [{"habitacion": habitacion.numero, "precio_por_dia": habitacion.precio_por_dia} for habitacion in habitaciones]

    return jsonify(resultado), 200

@habitacion_bp.route('/habitaciones/disponibilidad_dia', methods=['GET'])
@jwt_required()
def disponibilidad_habitaciones_dia():
    fecha_str = request.args.get('fecha')
    if not fecha_str:
        return jsonify({"message": "La fecha es requerida"}), 400

    try:
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"message": "formato de fecha invalido. asi tiene que ser YYYY-MM-DD."}), 400

    habitaciones = Habitacion.query.all()
    disponibilidad = []

    for habitacion in habitaciones:
        reserva = Reserva.query.filter(
            Reserva.habitacion_id == habitacion.id,
            Reserva.fecha_inicio <= fecha,
            Reserva.fecha_fin >= fecha
        ).first()
        
        if reserva:
            disponibilidad.append({"habitacion": habitacion.numero, "estado": "Ocupada"})
        else:
            disponibilidad.append({"habitacion": habitacion.numero, "estado": "Disponible"})

    return jsonify(disponibilidad), 200