from flask import Blueprint, render_template
from .forms import RegisterationForm
from app.extensions import security, db
from flask_security import hash_password
from .models import User


blueprint = Blueprint('users', __name__)

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        user_email = security.datastore.find_user(email=form.email.data)
        user_email = security.datastore.find_user(username=form.username.data)
        # raise error in forms
        if not (user_email and user_email):
            security.datastore.create_user(
                email=form.email.data,
                username=form.username.data,
                password=hash_password(form.password.data)
            )
            db.session.commit()
            # show success mesage
            # redirect to home
            
    return render_template('users/register.html', form = form)
