from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    email: str
    descripcion: str

class Cliente(ClienteBase):
    id: int
    id: int | None = None

class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(ClienteBase):
    pass