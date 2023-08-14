#importaciones de el proyecto  dependencias
from flask import Flask, render_template
from config import Config
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SearchField, PasswordField, SubmitField

#INICIALIZAR EL OBJETO FLASK
app = Flask(__name__)
app.config.from_object(Config)
#inicializar el onjeto sqlAlchemy
db=SQLAlchemy(app)  #tops de datos : string number etc...
migrate=Migrate(app,db)

#CREAR FORMULARIO DE REGISTRO CLIENTE

class RegistroClienteFrom(FlaskForm):
    username = SearchField("Nombre de Usuario")
    email = SearchField("Email")
    password = PasswordField("password")
    submit =SubmitField("Registrar Cliente")

#modelos -entidades de el proyeto 
class Cliente(db.Model):
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True)      #para tener el dato como entero se usa el db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100))  #para decir que un dato es unico se usa el unique =true y para llaves primarias se usa el primary_key
    password = db.Column(db.String(200))
    email = db.Column(db.String(100),unique=True)

class Producto(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer,
                    primary_key = True)      #para tener el dato como entero se usa el db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120),
                         unique=True)  #para decir que un dato es unico se usa el unique =true y para llaves primarias se usa el primary_key
    precio = db.Column(db.Numeric(precision=10,
                         scale = 2))
    imagen = db.Column(db.String(120),
                         unique=True)
    
class Venta(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer,
                    primary_key = True)
    fecha = db.Column(db.DateTime ,
                       default = datetime.utcnow ) #Se coloca para que la fecha sea default asi y se coloque la que esta en el sistema 
    cliente_id = db.Column(db.Integer,
                        db.ForeignKey('clientes.id'))

class Detalle(db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer,
                    primary_key = True)
    producto_id = db.Column(db.Integer,
                          db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer,
                          db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)

@app.route('/clientes/create',
           methods = ['GET' , 'POST'])
def crear_cliente():
    #instanciar formulario
    form = RegistroClienteFrom()
    if form.validate_on_submit():
    #crear el nuevo cliente
        c = Cliente(username = form.username.data,
                email = form.email.data,
                password =form.password.data)
        db.session.add(c)
        db.session.commit()
        return "Cliente Registrado"
    return render_template('registro.html',
                           form = form)
@app.route('/clientes',
           methods=['GET'])
def listar():
    #seleccionar todos los clientes
    clientes=Cliente.query.all()
    return render_template('listar.html',
                 clientes = clientes)