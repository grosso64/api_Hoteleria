from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hotel.db"
app.config['SQLALCHEMY_ECHO'] = True
app.config['JWT_SECRET_KEY'] = '0x76f4dfd8b8e5c7433d938a9a6e348ef62cf2a46a4e7348ae3fb9f3ad44e5c6a3'  # Cambiar esto a un secreto más seguro


ma = Marshmallow(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)



if __name__ == "__main__":
    app.run(debug=True)