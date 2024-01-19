from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import myapp
    app.add_url_rule("/", view_func=myapp.hello)

    return app
