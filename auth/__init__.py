from flask import Blueprint

bp = Blueprint('authentication', __name__)

from auth import authentication