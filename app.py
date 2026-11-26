from flask import Flask, render_template
from config import configs
from db import close_connection, init_db
from routes.tasks import bp as tasks_bp
from routes.users import bp as users_bp


def create_app(config_name: str = "default") -> Flask:
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    app.teardown_appcontext(close_connection)

    app.register_blueprint(tasks_bp)
    app.register_blueprint(users_bp)

    @app.get("/")
    def index():
        return render_template("index.html")

    init_db(app)
    return app


if __name__ == "__main__":
    create_app("development").run(debug=True)
