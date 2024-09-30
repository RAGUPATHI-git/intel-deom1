from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "This is secret key"
    from .views import views

    app.register_blueprint(views, url_prefix = '/')
    # app.register_blueprint(welcome, url_prefix = '/')

    return app