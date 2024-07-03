from klapi import app
from routes.auth import auth_bp
from routes.habitacion import habitacion_bp
from routes.reserva import reserva_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(habitacion_bp, url_prefix='/api')
app.register_blueprint(reserva_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)