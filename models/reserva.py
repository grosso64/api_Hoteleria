from klapi import db
from sqlalchemy.orm import relationship

class Reserva(db.Model):
    __tablename__ = 'reserva'
    
    id = db.Column(db.Integer, primary_key=True)
    habitacion_id = db.Column(db.Integer, db.ForeignKey('habitacion.id'), nullable=False)  # Clave foránea hacia habitacion
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Clave foránea hacia user
    
    cliente = db.relationship('User', back_populates='reservas')
    habitacion = db.relationship('Habitacion', back_populates='reservas')
