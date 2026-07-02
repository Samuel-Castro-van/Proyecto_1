from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.modelos.facturas import Factura

class TransaccionBase(SQLModel):
    cantidad: float
    valor_unitario: float

class Transaccion(TransaccionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    factura_id: int = Field(foreign_key="factura.id")
    factura: Optional["Factura"] = Relationship(back_populates="transacciones")

class TransaccionCrear(TransaccionBase):
    pass

class TransaccionEditar(SQLModel):
    cantidad: Optional[float] = None
    valor_unitario: Optional[float] = None

class TransaccionLeer(TransaccionBase):
    id: int
    factura_id: int