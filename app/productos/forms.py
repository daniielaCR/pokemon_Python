from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,StringField

class NewProductForm(FlaskForm):
    nombre =  StringField("Ingrese nombre producto")
    precio = IntegerField("Ingrese precio de el  producto")
    submit = SubmitField("Guardar")