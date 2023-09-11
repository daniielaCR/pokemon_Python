from flask import render_template, redirect, flash, url_for
from app.clientes import clientes
import app
from .forms import NewClienteForm, EditClienteForm

@clientes.route('/crear', methods=['GET','POST'])
def crear(): 
    p = app.models.Cliente()
    form = NewClienteForm()
    if form.validate_on_submit():
        #guardar en base de datos
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        return redirect('/clientes/listarCli')
    flash("cliente registrado correctamente")
    return render_template('new_cliente.html',
                           form=form)  
    
@clientes.route('/listarCli')
def listar2(): 
    #seleccionar los productos
    clientes = app.models.Cliente.query.all()
    return render_template("listar_clientes.html", clientes = clientes)


@clientes.route('/editar/<cliente_id>',
                 methods =['GET' , 'POST'])
def editar(cliente_id):
    c = app.models.Cliente.query.get(cliente_id)
    form = EditClienteForm(obj = c)
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.commit()
        flash('cliente actualizado')
        return redirect('/clientes/listarCli')
    return render_template('new_cliente.html',
                    form = form, c = c)

   

@clientes.route('/eliminar/<cliente_id>' , methods = ['GET', 'POST'])                
def eliminar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('cliente eliminado')
    return redirect('/clientes/listarCli')