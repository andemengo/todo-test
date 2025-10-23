from flask import Flask
import os
from .web import web_bp
from .api import api_bp
from .config import config

def create_app():
    app = Flask(__name__)
    
    # Carica configurazione dall'ambiente
    env = os.getenv('ENVIRONMENT', 'development')
    app.config.from_object(config[env])
    
    # Configurazione Jinja2
    app.jinja_env.trim_blocks = app.config['JINJA_TRIM_BLOCKS']
    app.jinja_env.lstrip_blocks = app.config['JINJA_LSTRIP_BLOCKS']
    
    # Registrazione blueprints
    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
