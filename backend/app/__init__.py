from flask import Flask
import os
from pathlib import Path
from .web import web_bp
from .api import api_bp
from .config import config

def create_app():
    # Path al frontend
    base_dir = Path(__file__).parent.parent.parent
    frontend_dir = base_dir / 'frontend'
    
    app = Flask(__name__,
                template_folder=str(frontend_dir / 'templates'),
                static_folder=str(frontend_dir / 'static'))
    
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
