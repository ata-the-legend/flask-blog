from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo



class RegisterationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), ])
    username = StringField('Username', validators=[DataRequired(), ])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Pasword', validators=[DataRequired(), EqualTo('password'), ])