from flask import Blueprint


bp = Blueprint('api', __name__)

from SOLUTION_3_BONUS.app.api import solving, errors
