from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,StringField
from wtforms.validators import InputRequired,NumberRange
from flask_wtf.file import FileField , FileRequired,FileAllowed
class NewProductForm(FlaskForm):
    nombre =  StringField("Ingrese nombre producto",validators=[InputRequired(message='Nombre requerido')])
    precio = IntegerField("Ingrese precio de el  producto",validators=[InputRequired(message='Precio requerido'),NumberRange(message='precio fuera de rango', min=10000, max=100000)])
    imagen= FileField("Imagen del  producto", 
                      validators=[
                          FileRequired(message="Se requiere una imagen"),
                          FileAllowed(["jpg" ,"png"],
                                      "Solo se acpetan imagenes")
                      ])
    submit = SubmitField("Guardar") 
    
    