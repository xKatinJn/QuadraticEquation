from flask import Flask
from SOLUTION_3_BONUS.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from SOLUTION_3_BONUS.app.api import bp as api_bp
from SOLUTION_3_BONUS.app import routes

app.register_blueprint(api_bp, url_prefix='/api')
