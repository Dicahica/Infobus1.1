from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class Formulario_Cuentas(FlaskForm):
	Nombre = StringField('Username', validators=[DataRequired()])
	Numero_Cuenta = IntegerField('numero', validators=[DataRequired()])
	Descripcion = StringField('descripcion', validators=[DataRequired()])
	Saldo = StringField('saldo', validators=[DataRequired()])
	tipo = SelectField(
        choices=[('1', 'Corriente'), ('2', 'Dinero'), ('3', 'Ahorros'), ('4', 'Inversion'), ('5', 'cheque')]
    )
	submit = SubmitField('Guardar')
	submit2 = SubmitField('Volver')