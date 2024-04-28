from models.usuario import Usuario as UsuarioModel
from schemas.usuario import Usuario

class UsuarioService():

    def __init__(self, db) -> None:
        self.db = db
    
    def get_usuarios(self):
        result = self.db.query(UsuarioModel).all()
        return result
    
    def get_usuario(self, cedula: int):
        result = self.db.query(UsuarioModel).filter(UsuarioModel.cedula == cedula).first()
        return result
    
    def create_usuario(self, usuario: Usuario):

        new_usuario = UsuarioModel(**usuario.dict())
        self.db.add(new_usuario)
        self.db.commit()
        return
    
    def update_usuario(self, cedula: int, data: Usuario):
        usuario = self.db.query(UsuarioModel).filter(UsuarioModel.cedula == cedula).first()
        usuario.nombre = data.nombre
        usuario.telefono = data.telefono
        usuario.email = data.email
        usuario.pais = data.pais
        usuario.ciudad = data.ciudad
        self.db.commit()
        return
    
    def delete_usuario(self, cedula: int):
        self.db.query(UsuarioModel).filter(UsuarioModel.cedula == cedula).delete()
        self.db.commit()
        return
    
    def get_usuario_by_name(self, nombre: str):

        result = self.db.query(UsuarioModel).filter(UsuarioModel.nombre == nombre).all()
        return result
    
    def get_usuario_by_email(self, email: str):

        result = self.db.query(UsuarioModel).filter(UsuarioModel.email == email).first()
        return result
    
    
    



