"""
Configurazione centralizzata per l'applicazione Flask
Utilizza variabili d'ambiente per maggiore sicurezza
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Carica le variabili dal file .env nella root del progetto
base_dir = Path(__file__).parent.parent.parent
dotenv_path = base_dir / '.env'
load_dotenv(dotenv_path)


class Config:
    """Configurazione base"""
    # Sicurezza: SECRET_KEY da variabile d'ambiente
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-key-change-this')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    ENV = os.getenv('FLASK_ENV', 'production')
    
    # Configurazione Jinja2
    JINJA_TRIM_BLOCKS = True
    JINJA_LSTRIP_BLOCKS = True
    
    # Path al frontend
    BASE_DIR = base_dir
    FRONTEND_DIR = base_dir / 'frontend'


class DevelopmentConfig(Config):
    """Configurazione per sviluppo"""
    DEBUG = True
    ENV = 'development'


class ProductionConfig(Config):
    """Configurazione per produzione"""
    DEBUG = False
    ENV = 'production'
    # In produzione, SECRET_KEY DEVE essere impostata
    if not os.getenv('SECRET_KEY'):
        raise ValueError("SECRET_KEY deve essere impostata in produzione!")


# Dizionario per scegliere facilmente la configurazione
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
