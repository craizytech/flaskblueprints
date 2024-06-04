from flask import Blueprint

bp = Blueprint('landing', __name__)

from home import landing
