from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, nombreUsuario, correoUsuario, rolUsuario, edadUsuario, telefonoUsuario) -> None:
        self.id = id
        self.nombreUsuario = nombreUsuario
        self.correoUsuario = correoUsuario
        self.edadUsuario = edadUsuario
        self.telefonoUsuario = telefonoUsuario
        self.rolUsuario = rolUsuario

    @classmethod
    def comprobar_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @classmethod
    def crear_hash_password(self, password):
        return generate_password_hash(password)
