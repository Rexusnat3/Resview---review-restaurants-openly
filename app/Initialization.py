from flask import Flask
import App_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(App_routes.app.route)

    return app

