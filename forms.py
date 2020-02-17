from flask__wtf import FlaskForm 
from wtforms import StringField
from wtfforms.validators import DataRequired, Length , Email


class RegistrationForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired(), Length(min=3,max=15)])

    email = StringField('Email', validators=[DataRequired(),Email()])

    password= PasswordField('Password', validators=[DataRequired()])