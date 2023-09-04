from flask import render_template
from app.productos import productos
import app
import os
from .forms import NewProductForm

@productos.route('/create', methods=['GET','POST'])
def crear(): 
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        #guardar en base de datos
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        #subir en carpeat de imagenes 
        # campo imagen ( filestorage): 
        archivo= form.imagen.data
        archivo.save(os.path.abspath(os.getcwd()+"/app/productos/imagenes/"+p.imagen))
        return "producto registrado"
    return render_template('new.html',
                           form=form)