from fastapi import APIRouter, HTTPException
from DataBase.SQLoperations import SQLoperations
from models import usuario

router = APIRouter()
db = SQLoperations()
validar = usuario.Usuario


@router.post("/login/")
def validar_usuario(correo: str, contraseña: str): 
    if validar.es_gmail_valido(correo) is True:
        
        if validar.es_contrasenia_segura(contraseña) is True:
            
            if db.validacion_usuario(correo, contraseña):
                return {"mensaje": "Usuario validado correctamente."}
            
            else:
                raise HTTPException(tatus_code=401, detail='"correo invalido, su correo debe ser ejemplo@ej.com"')
        
        else:  
            raise HTTPException(status_code=400, detail="muy debil, su contraseña debe tener al menos 8 caracteres, una mayuscula, una minuscula, un numero y un caracter especial")


@router.post("/singup/")
def insertar_usuario(correo: str, contraseña: str):
    resultado = db.insertar_usuario(correo, contraseña)
    return resultado



