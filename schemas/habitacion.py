# En schemas/habitacion.py
from flask_marshmallow import Marshmallow
from models.habitacion import Habitacion

ma = Marshmallow()

class HabitacionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Habitacion

habitacion_schema = HabitacionSchema()
habitaciones_schema = HabitacionSchema(many=True)