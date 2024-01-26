from flask import Blueprint, render_template
from flask_security import current_user

blueprint = Blueprint('posts', __name__)

@blueprint.route('/')
def home():
    return render_template('posts/home.html', name=current_user.username if current_user.is_authenticated else 'login')
