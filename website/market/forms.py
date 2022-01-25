from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import  Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='User name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirm password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='SUBMIT')
