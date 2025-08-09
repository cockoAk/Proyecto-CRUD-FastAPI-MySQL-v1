import mysql.connector
from models.usuario import Usuario
class SQLoperations:


    def __init__(self):
        self.usuariosDB = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="gestionar_de_clientes"
        )
        self.cursor = self.usuariosDB.cursor()



    def insertar_usuario(self, correo, contraseña):
        try:
            self.cursor.execute(
                "insert into usuarios (correo, contraseña) values (%s, %s)",
                (correo, contraseña)
            )
            self.usuariosDB.commit()
            print("Usuario insertado correctamente.")
            return {True, "Usuario creado correctamente."}
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
            self.usuariosDB.rollback()
            return {"error": str(e)}



    def mostrar_usuario(self, por: str, valor: str):
        try:
            #
            query = f"select * from usuarios WHERE {por} = %s"
            self.cursor.execute(query, (valor,))
            usuarios = self.cursor.fetchall()
            for usuario in usuarios:
                usuario_model = Usuario(correo=usuario[1], contraseña=usuario[2])
                conjunto = usuario_model.model_dump()
                return conjunto
            return {"mensaje": "Usuario no encontrado"}
        except Exception as e:
            print(f"Error al mostrar usuarios: {e}")
            return {"error": str(e)}



    def mostrar_todos_usuarios(self):
        try:
            self.cursor.execute("select * from usuarios")
            usuarios = self.cursor.fetchall()
            lista_usuarios = []
            for usuario in usuarios:
                usuario_model = Usuario(correo=usuario[1], contraseña=usuario[2])
                conjunto = usuario_model.model_dump()
                lista_usuarios.append(conjunto)
            return lista_usuarios
        except Exception as e:
            print(f"Error al mostrar todos los usuarios: {e}")
            return {"error": str(e)}        


    def validacion_usuario(self, correo: str, contraseña: str):
        try:
            self.cursor.execute(
                "select * from usuarios where correo = %s and contraseña = %s",
                (correo, contraseña)
            )
            usuario = self.cursor.fetchone()
            if usuario:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al validar usuario: {e}")
            return False


    def eliminar_usuario(self, correo: str):
        try:
            self.cursor.execute("delete from usuarios where correo = %s", (correo,))
            self.usuariosDB.commit()
            if self.cursor.rowcount > 0:
                return {"mensaje": "Usuario eliminado correctamente."}
            else:
                return {"mensaje": "Usuario no encontrado."}
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            self.usuariosDB.rollback()
            return {"error": str(e)}
        
    
    def actualizar_usuario(self, correo: str, nueva_contrasenia: str):
        try:
            self.cursor.execute(
                "update usuarios set contraseña = %s where correo = %s",
                (nueva_contrasenia, correo)
            )
            self.usuariosDB.commit()
            if self.cursor.rowcount > 0:
                return {"mensaje": "Usuario actualizado correctamente."}
            else:
                return {"mensaje": "Usuario no encontrado."}
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            self.usuariosDB.rollback()
            return {"error": str(e)}

