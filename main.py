from fastapi import FastAPI
from DataBase.SQLoperations import SQLoperations
from routes import auth
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
db = SQLoperations()  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://127.0.0.1"] si prefieres limitar
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}



@app.get("/mostrar_usuarios/")
def mostrar_usuarios(por: str, valor: str):
    usuarios = db.mostrar_usuarios(por, valor)
    return {"usuarios": usuarios}

@app.get("/mostrar_todos_usuarios/")
def mostrar_todos_usuarios():
    if hasattr(db, "mostrar_todos_usuarios"):
        usuarios = db.mostrar_todos_usuarios()
        return {"usuarios": usuarios}
    return {"error": "Método mostrar_todos_usuarios no implementado"}

@app.post("/insertar_usuario/")
def insertar_usuario(correo: str, contraseña: str):
    resultado = db.insertar_usuario(correo, contraseña)
    return resultado

@app.delete("/eliminar_usuario/")
def eliminar_usuario(correo: str):
    resultado = db.eliminar_usuario(correo)
    return resultado

@app.put ("/actualizar_usuario/")
def actualizar_usuario(correo: str, nueva_contrasenia: str):
    resultado = db.actualizar_usuario(correo, nueva_contrasenia)
    return resultado