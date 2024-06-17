from flask import Flask
from config import Config
from extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from controllers.book_controller import book_bp
    app.register_blueprint(book_bp)

    @app.get("/")
    def home():
        return "Hello, world!"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
