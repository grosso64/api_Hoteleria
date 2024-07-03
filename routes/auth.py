from functools import wraps
from flask import Blueprint, request, jsonify
from klapi import db
from models.user import User
from schemas.user import user_schema, users_schema
from flask_jwt_extended import create_access_token, get_jwt_identity, verify_jwt_in_request

auth_bp = Blueprint('auth_bp', __name__)

def role_required(rol):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_identity()
            if claims['rol'] != rol:
                return jsonify({"message": "acesso denegado"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@auth_bp.route('/registro', methods=['POST'])
def register():
    data = request.get_json()
    usuario = data.get('username')
    password = data.get('password')
    rol = data.get('role')

    if not usuario or not password or not rol:
        return jsonify({"message": "Faltan datos por ingresar"}), 400

    # Validar el rol
    if rol not in ['Cliente', 'Empleado']:
        return jsonify({"message": "Rol no válido, debe ser 'Cliente' o 'Empleado'"}), 400

    user = User(username=usuario, password=password, role=rol)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuario registrado"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=usuario, password=password).first()
    if not user:
        return jsonify({"message": "datos ingresados incorrectos"}), 401

    accesso_token = create_access_token(identity={'id': user.id, 'usuario': user.username, 'rol': user.role})
    return jsonify(access_token=accesso_token)