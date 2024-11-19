from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)
    
    #orm
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models

    #블루프린트
    from .views import main_views ,auth_views ,card_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(card_views.bp)

    return app


