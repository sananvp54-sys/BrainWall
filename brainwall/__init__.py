from flask import Flask

def create_app():
    app = Flask(__name__)

    from brainwall.routes.pages import pages
    from brainwall.routes.api import api

    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix="/api")

    return app
