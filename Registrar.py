from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms import SubmitField
from wtforms.validators import DataRequired

class RegistroForm(FlaskForm):
    cedula = IntegerField("Cédula", validators=[DataRequired()])
    nombres = StringField("Nombres", validators=[DataRequired()])
    celular = IntegerField("Celular", validators=[DataRequired()])
    direccion = StringField("Dirección", validators=[DataRequired()])
    submit = SubmitField('Registrar')