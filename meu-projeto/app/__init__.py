from flask import Flask
from config import Config
from app.extensions import mysql
from app.controllers.controller_exame import exame_blueprint
import logging
from logging.handlers import RotatingFileHandler
import os
import json

if not os.path.exists('logs'):
    os.makedirs('logs')

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage()
        }
        return json.dumps(log_record, ensure_ascii=False)  # Evita escape de caracteres especiais

# Definir o manipulador de log
log_handler = RotatingFileHandler('logs/conexoes_banco.json', maxBytes=1000000, backupCount=5)
log_handler.setFormatter(JsonFormatter())

logger = logging.getLogger('conexao_banco')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mysql.init_app(app)

    app.register_blueprint(exame_blueprint)

    return app 