from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from modelos.clientes import Cliente, ClienteCrear
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear
from modelos.transacciones import Transaccion, TransaccionCrear

@@ -14,40 +14,60 @@

# --- ENDPOINTS CLIENTES ---
@app.get("/clientes", response_model=List[Cliente])
def listar_clientes():
async def listar_clientes():
    return lista_clientes

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def listar_cliente(cliente_id: int):
async def listar_cliente(cliente_id: int):
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            return cliente
    return {"mensaje": "Cliente no encontrado"}
    raise HTTPException(status_code=400, detail=f"El cliente con ID {cliente_id} no existe")

@app.post("/clientes", response_model=Cliente)
def crear_cliente(cliente_crear: ClienteCrear):
async def crear_cliente(cliente_crear: ClienteCrear):
    id_cliente = len(lista_clientes) + 1
    val = Cliente.model_validate(cliente_crear.model_dump())
    val.id = id_cliente
    lista_clientes.append(val)
    return val

@app.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, objeto_cliente in enumerate(lista_clientes):
        if objeto_cliente.id == cliente_id:
            val = Cliente.model_validate(datos_cliente.model_dump())
            val.id = cliente_id
            lista_clientes[i] = val
            return val
    raise HTTPException(status_code=400, detail=f"El cliente con ID {cliente_id} no existe")

@app.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, objeto_cliente in enumerate(lista_clientes):
        if objeto_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(status_code=400, detail=f"El cliente con ID {cliente_id} no existe")

# --- ENDPOINTS FACTURAS ---
@app.get("/facturas", response_model=List[Factura])
def listar_facturas():
async def listar_facturas():
    return lista_facturas

@app.post("/facturas", response_model=Factura)
def crear_factura(factura_crear: FacturaCrear):
async def crear_factura(factura_crear: FacturaCrear):
    val = Factura.model_validate(factura_crear.model_dump())
    lista_facturas.append(val)
    return val

# --- ENDPOINTS TRANSACCIONES ---
@app.get("/transacciones", response_model=List[Transaccion])
def listar_transacciones():
async def listar_transacciones():
    return lista_transacciones

@app.post("/transacciones", response_model=Transaccion)
def crear_transaccion(transaccion_crear: TransaccionCrear):
async def crear_transaccion(transaccion_crear: TransaccionCrear):
    val = Transaccion.model_validate(transaccion_crear.model_dump())
    lista_transacciones.append(val)
    return val