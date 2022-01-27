from typing import NoReturn

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from market.models import User


class RegisterForm(FlaskForm):
    username = StringField(
        label='User name:', validators=[Length(min=2, max=30), DataRequired()]
    )
    email = StringField(
        label='Email:', validators=[Email(), DataRequired(), DataRequired()]
    )
    password1 = PasswordField(
        label='Password:', validators=[Length(min=8), DataRequired()]
    )
    password2 = PasswordField(
        label='Confirm password:', validators=[EqualTo('password1'), DataRequired()]
    )
    submit = SubmitField(label='SUBMIT')

    def validate_username(self, username_to_check: str) -> NoReturn:
        user = User.query.filter_by(username=username_to_check.data).first()

        if user:
            raise ValidationError('Username already exists!')

    def validate_email(self, email_to_check: str) -> NoReturn:
        email = User.query.filter_by(email=email_to_check.data).first()

        if email:
            raise ValidationError('Email already exists!')


class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = StringField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
