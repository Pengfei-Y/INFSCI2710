# user_bp
from flask import Blueprint

business_bp = Blueprint('business', __name__)


@business_bp.route('/bus')
def index():
    return "22"
