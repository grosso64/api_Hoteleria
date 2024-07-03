from klapi import ma
from models.reserva import Reserva
from models.habitacion import Habitacion
from models.user import User  # Asegúrate de importar el modelo de usuario
from marshmallow import fields

class ReservaSchema(ma.SQLAlchemyAutoSchema):
    habitacion_numero = fields.Method("get_habitacion_numero")
    cliente_id = fields.Method("get_cliente_id")  # Añadir campo para cliente_id

    class Meta:
        model = Reserva
        load_instance = True

    def get_habitacion_numero(self, obj):
        habitacion = Habitacion.query.get(obj.habitacion_id)
        return habitacion.numero if habitacion else None

    def get_cliente_id(self, obj):
        cliente = User.query.get(obj.cliente_id)
        return cliente.id if cliente else None

reserva_schema = ReservaSchema()
reservas_schema = ReservaSchema(many=True)