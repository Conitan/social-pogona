from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

# Configuracion
from config import config

# Modelo y BD
from db import agregarUsuario, comprobarUsuario, obtenerUsuario, updateUsuario, updateUsuarioDos, comprobarUsuarioDos
from models.entities.usuario import User

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

csrf = CSRFProtect()
login_app = LoginManager(app)

@login_app.user_loader
def load_user(id):
    # datos = obtenerUsuario(id)
    # User(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])
    return obtenerUsuario(id)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        login_usuario = comprobarUsuario(request.form['emailUsuarioUno'], request.form['contraUsuarioUno'])
        if login_usuario != None:
            login_user(login_usuario)
            return render_template('auth/perfil.html')
        else:
            flash('Datos Incorrectos')
            return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        if agregarUsuario(request.form['emailUsuario'], request.form['nombreUsuario'], User.crear_hash_password(request.form['contraUsuario']), 'usuario') == 'error':
            flash('Datos Incorrectos')
            return render_template('index.html')
        else:
            flash('Registro Exitoso')
            return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/update', methods=['GET','POST'])
@login_required
def update():
    if request.method=='POST':
        if request.form['contraUsuario'] != 'Nueva Contraseña':
            if updateUsuario(request.form['correoUsuario'], request.form['nombreUsuario'], User.crear_hash_password(request.form['contraUsuario']), request.form['rollUsuario'], request.form['teledonoUsuario'], request.form['edadUsuario'],) != 'error':
                login_usuario = comprobarUsuarioDos(request.form['correoUsuario'])
                if login_usuario != None:
                    login_user(login_usuario)
                    return render_template('auth/perfil.html')
                else:
                    return render_template('auth/perfil.html')
            else:
                flash('Error al actualizar')
                return render_template('auth/perfil.html')
        else:
            if updateUsuarioDos(request.form['correoUsuario'], request.form['nombreUsuario'], request.form['rollUsuario'], request.form['teledonoUsuario'], request.form['edadUsuario'],) != 'error':
                login_usuario = comprobarUsuarioDos(request.form['correoUsuario'])
                if login_usuario != None:
                    login_user(login_usuario)
                    return render_template('auth/perfil.html')
                else:
                    return render_template('auth/perfil.html')
            else:
                flash('Error al actualizar')
                return render_template('auth/perfil.html')
    else:
        return render_template('index.html')


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return redirect(url_for('login'))


if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()