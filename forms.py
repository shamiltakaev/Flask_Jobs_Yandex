from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    userid = StringField('Id астронавта', validators=[DataRequired()])
    password_1 = PasswordField(
        'Пароль астронавта', validators=[DataRequired()])
    cap_id = StringField('Id капитана', validators=[DataRequired()])
    password_2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')
