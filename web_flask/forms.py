from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, EqualTo


class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"class": "in-field"})
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={"class": "in-field"})
    email_confirm = EmailField('Confirm Email',
                               validators=[DataRequired(), Email(), EqualTo('email', 'Email mismatch')], render_kw={"class": "in-field"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "in-field"})
    password_confirm = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', 'Password mismatch')], render_kw={"class": "in-field"})
    address = StringField('Address', validators=[DataRequired()], render_kw={"class": "in-field"})
    postal_code = StringField('Postal Code', validators=[DataRequired()], render_kw={"class": "in-field"})
    about = TextAreaField('About', validators=[DataRequired()], render_kw={"class": "in-field"})
    confirm = SubmitField('Confirm', render_kw={"class": "save"})


class LoginFrom(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={"class": "in-field"})
    password = PasswordField('Password', validators=[DataRequired(), Email()], render_kw={"class": "in-field"})
    login = SubmitField('Login', render_kw={"class": "save"})