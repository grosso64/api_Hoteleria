from klapi import db
from sqlalchemy.orm import relationship

class Habitacion(db.Model):
    __tablename__ = 'habitacion'
    
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), unique=True, nullable=False)
    precio_por_dia = db.Column(db.Float, nullable=False)
    activa = db.Column(db.Boolean, default=True, nullable=False)
    
    reservas = db.relationship('Reserva', back_populates='habitacion')