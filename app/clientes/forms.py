from flask_wtf import FlaskForm
from wtforms import SubmitField,PasswordField,StringField, EmailField
from wtforms.validators import InputRequired,Length

class ClienteForm():
    username =  StringField("Ingrese nombre cliente",
                            validators=[InputRequired(message='Nombre requerido')])
    password = PasswordField("Ingrese la contraseña",
                            validators=[InputRequired(message='password'), Length(min=10, max=20)])
    email = EmailField('Ingresa un correo', validators=[InputRequired(message='Requerido')])

class NewClienteForm(FlaskForm, ClienteForm): 
     submit = SubmitField("Guardar") 
     
class EditClienteForm(FlaskForm,
                      ClienteForm):
    submit = SubmitField("Actualizar")