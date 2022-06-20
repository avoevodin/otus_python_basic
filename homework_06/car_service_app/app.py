from os import getenv

from flask import Flask
from flask_migrate import Migrate

from car_service_app.models import db

app = Flask(__name__)

config_name = "car_service_app.config.%s" % getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(config_name)

db.init_app(app)

migrate = Migrate(app, db, compare_type=True)

if __name__ == "__main__":
    app.run(port=5000)
