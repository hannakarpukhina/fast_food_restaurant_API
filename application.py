from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
from services.db_service import DBService


db_service = DBService()
db = db_service.db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)
    return app


app = create_app()
app.register_blueprint(blueprint)
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
