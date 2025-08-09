from pydantic import BaseModel
import re
class Usuario(BaseModel):
    correo: str
    contraseña: str


    def es_gmail_valido(correo: str) -> bool:
        patron = r"^[a-zA-Z0-9_.+-]+@gmail\.com$"
        return re.match(patron, correo) is not None


    def es_contrasenia_segura(contrasenia: str) -> bool:
        
        if len(contrasenia) < 8:
            return False
        if not re.search(r"[A-Z]", contrasenia):
            return False
        if not re.search(r"[a-z]", contrasenia):
            return False
        if not re.search(r"[0-9]", contrasenia):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasenia):
            return False
        return True
