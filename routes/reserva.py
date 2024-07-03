# En routes/reserva.py

from flask import Blueprint, request, jsonify
from klapi import db
from models.reserva import Reserva
from models.habitacion import Habitacion
from models.user import User  # Asegúrate de importar el modelo de usuario
from routes.auth import role_required
from schemas.reserva import reserva_schema, reservas_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

reserva_bp = Blueprint('reserva_bp', __name__)

@reserva_bp.route('/reservas', methods=['POST'])
@jwt_required()
def create_reserva():
    data = request.get_json()
    habitacion_numero = data.get('habitacion_numero')
    fecha_inicio_str = data.get('fecha_inicio')
    fecha_fin_str = data.get('fecha_fin')

    if not habitacion_numero or not fecha_inicio_str or not fecha_fin_str:
        return jsonify({"message": "Faltan datos por ingresar"}), 400

    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
        fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()

        if fecha_inicio > fecha_fin:
            return jsonify({"message": "Fecha de inicio no puede ser mayor que fecha de fin"}), 400

        habitacion = Habitacion.query.filter_by(numero=habitacion_numero).first()
        if not habitacion:
            return jsonify({"message": "Habitación no encontrada"}), 404

        if not habitacion.activa:
            return jsonify({"message": "Habitación no está activa"}), 400

        habitacion_id = habitacion.id

        # Verificar disponibilidad de la habitación en las fechas proporcionadas
        reservas = Reserva.query.filter(
            Reserva.habitacion_id == habitacion_id,
            Reserva.fecha_fin >= fecha_inicio,
            Reserva.fecha_inicio <= fecha_fin
        ).first()
        
        if reservas:
            return jsonify({"message": "Habitación no disponible en el periodo seleccionado"}), 400

        # Obtener cliente_id del token JWT
        current_user = get_jwt_identity()
        cliente_id = current_user['id']  # Asumiendo que el ID del cliente se almacena en el token con la clave 'id'

        reserva = Reserva(habitacion_id=habitacion_id, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, cliente_id=cliente_id)
        db.session.add(reserva)
        db.session.commit()
    except ValueError:
        return jsonify({"message": "Formato de fecha inválido. Debe ser YYYY-MM-DD."}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

    return reserva_schema.jsonify(reserva), 201

@reserva_bp.route('/reservas', methods=['GET'])
@jwt_required()
@role_required('Empleado')
def get_reservas():
    reservas = Reserva.query.all()
    return reservas_schema.jsonify(reservas)
