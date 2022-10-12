import sqlite3 as sql
from flask import g

from models.entities.usuario import User

DATABASE = 'app\AppImages.db'

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

# @app.teardown_appcontext
# def close_connection(exception):
#     db = getattr(g, '_database', None)
#     if db is not None:
#         db.close()

def agregarUsuario(email, nombre, contra, rol):
    try:
        con = sql.connect(DATABASE)
        cur = con.cursor()
        cur.execute("INSERT INTO Usuario (nombre_Usuario, correo_Usuario, contra_Usuario, rol_Usuario) VALUES (\'"+ nombre +"\',\'"+ email +"\',\'"+ contra +"\',\'"+ rol +"\');")
        con.commit()
        con.close()
    except Exception as ex:
        return "error"

def comprobarUsuario(email, contra):
    datos = None
    try:
        con = sql.connect(DATABASE)
        cur = con.cursor()
        cur.execute("SELECT contra_Usuario, ID_Usuario, nombre_Usuario, correo_Usuario, rol_Usuario, edad_Usuario, cel_Usuario FROM Usuario WHERE correo_Usuario=\'"+ email +"\';")
        con.commit()
        datos = cur.fetchone()
        if datos != None:
            if User.comprobar_password(datos[0], contra):
                return User(datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])
                # return datos
        else:
            return None
    except Exception as ex:
        con.close()
        return None

def obtenerUsuario(id):
    datos = None
    try:
        con = sql.connect(DATABASE)
        cur = con.cursor()
        cur.execute("SELECT contra_Usuario, ID_Usuario, nombre_Usuario, correo_Usuario, rol_Usuario, edad_Usuario, cel_Usuario FROM Usuario WHERE ID_Usuario=\'"+ id +"\';")
        con.commit()
        datos = cur.fetchone()
        if datos != None:
            con.close()
            return User(datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])
            # return datos
        else:
            con.close()
            return "error"

    except Exception as ex:
        con.close()
        return None


def updateUsuario(email, nombre, contra, rol, telefono, edad):
    try:
        con = sql.connect(DATABASE)
        cur = con.cursor()
        cur.execute("UPDATE Usuario SET nombre_Usuario = \'"+ nombre +"\', contra_Usuario = \'"+ contra +"\', rol_Usuario = \'"+ rol +"\', edad_Usuario = \'"+ edad +"\', cel_Usuario = \'"+ telefono +"\' WHERE correo_Usuario = \'"+ email +"\';")
        con.commit()
        con.close()
    except Exception as ex:
        return "error"


def updateUsuarioDos(email, nombre, rol, telefono, edad):
    try:
        con = sql.connect(DATABASE)
        cur = con.cursor()
        cur.execute("UPDATE Usuario SET nombre_Usuario = \'"+ nombre +"\', rol_Usuario = \'"+ rol +"\', edad_Usuario = \'"+ edad +"\', cel_Usuario = \'"+ telefono +"\' WHERE correo_Usuario = \'"+ email +"\';")
        con.commit()
        con.close()
    except Exception as ex:
        return "error"


def comprobarUsuarioDos(email):
    datos = None
    try:
        con = sql.connect(DATABASE)
        cur = con.cursor()
        cur.execute("SELECT contra_Usuario, ID_Usuario, nombre_Usuario, correo_Usuario, rol_Usuario, edad_Usuario, cel_Usuario FROM Usuario WHERE correo_Usuario=\'"+ email +"\';")
        con.commit()
        datos = cur.fetchone()
        if datos != None:
            return User(datos[1], datos[2], datos[3], datos[4], datos[5], datos[6])
        else:
            return None

    except Exception as ex:
        con.close()
        return None