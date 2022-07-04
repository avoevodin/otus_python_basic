from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from models import db
from views.services import services_app

app = Flask(__name__)

config_name = "config.%s" % getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(config_name)

db.init_app(app)

migrate = Migrate(
    app,
    db,
    compare_type=True,
)

app.register_blueprint(services_app, url_prefix="/services")


@app.get("/")
def index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5050)
