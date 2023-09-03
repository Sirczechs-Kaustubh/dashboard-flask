from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired

username_required = "Please provide a username"
password_required = "Please provide a password"
text_required = "Please provide "

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired(message=username_required)])
    password = PasswordField('Password',validators=[InputRequired(message=password_required)])
    remember = BooleanField(False)

class SignupForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired(message=username_required)])
    password = PasswordField('Password',validators=[InputRequired(message=password_required)])
    first_name = StringField('First Name',validators=[InputRequired(message=text_required)])
    last_name = StringField('Last Name')
    email = StringField('Email')
    active = BooleanField('Active')
