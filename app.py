from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf.csrf import CSRFProtect
from wtforms import SubmitField
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect

class MiFormulario(FlaskForm):
    submit = SubmitField('Registrar')


from Registrar import RegistroForm

from flask import Flask



app = Flask(__name__)

csrf = CSRFProtect(app)

# Configura una clave secreta
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

# Inicializa la protección CSRF
csrf = CSRFProtect(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.icon', mimetype='image/vnd.microsoft.icon')

# -- Redireccionamiento de rutas
@app.route("/articulos/")
def articulos():
    return "Lista de artículos"

@app.route("/acercade")
def acercade():
    return "Página acerca de..."

# ...


# ...


# ...

@app.errorhandler(401)
def page_not_authorized(error):
    return "Página no autorizada...", 401


@app.route("/")
def index():
    return redirect(url_for('principal'))


#--------------------------------------------------------------------------------------

@app.route('/principal')
def principal():
    return render_template("principal.html")


#--------------------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(error):
  return (render_template("error.html", error="Página no encontrada..."),
            404)
#--------------------------------------------------------------------------------------

registros = []

# Ruta principal para el registro de datos
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        form = RegistroForm(request.form)
        if form.validate_on_submit():
            cedula = form.cedula.data
            nombres = form.nombres.data
            celular = form.celular.data
            direccion = form.direccion.data
            # Agregar los datos al arreglo de registros
            registros.append({'cedula': cedula, 'nombres': nombres, 'celular': celular, 'direccion': direccion})
            # Redirigir a la misma página para mostrar el mensaje de éxito
            return redirect(url_for('registro'))
    else:
        form = RegistroForm()

    return render_template('registro.html', form=form)

# Nueva vista para mostrar los registros en una tabla
@app.route('/registros')
def ver_registros():
    return render_template('registros.html', registros=registros)

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html', registros=registros)

#--------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)

