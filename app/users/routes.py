from flask import Blueprint, render_template, redirect, url_for, request
from .forms import RegisterationForm, LoginForm
from app.extensions import security, db
from flask_security import hash_password, current_user, verify_password, login_user
from .models import User


blueprint = Blueprint('users', __name__)

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        user_email = security.datastore.find_user(email=form.email.data)
        user_username = security.datastore.find_user(username=form.username.data)
        # raise error in forms
        if not (user_email and user_username):
            security.datastore.create_user(
                email=form.email.data,
                username=form.username.data,
                password=hash_password(form.password.data)
            )
            db.session.commit()
            # show success mesage
            return redirect(url_for('posts.home'))
            
    return render_template('users/register.html', form = form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('posts.home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = security.datastore.find_user(email=form.email.data)
		if user and verify_password(form.password.data, user.password):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			# flash('you logged in successfully', 'success')
			return redirect(next_page if next_page else url_for('posts.home'))
		else:
			...
			# flash('Email or Password is wrong', 'danger')
	return render_template('users/login.html', form=form)