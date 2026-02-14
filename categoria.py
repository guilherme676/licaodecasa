from fastapi import APIRouter, Depends
from services import CategoriaService
from schemas import CategoriaSchema, QuerySchema, CategoriaObtSchema
from typing import Annotated 

categoria_router = APIRouter()

@categoria_router.get("/categorias")
async def get_categorias(params: Annotated[QuerySchema, Depends()]):
     return CategoriaService.listar_categorias(params)
    

@categoria_router.post("/categorias")
async def add_categoria(categoria: CategoriaSchema):
    return CategoriaService.adicionar_categoria(categoria)
     

@categoria_router.get('/categorias/{id}')
async def obt_categoria(id: Annotated[CategoriaObtSchema, Depends()]):
     return CategoriaService.obter_categoria(id)

@categoria_router.put('/categorias/{id}')
async def atualizar_categoria(params: Annotated[CategoriaSchema, Depends()]):
     return CategoriaService.atualizar_categoria(params)

@categoria_router.delete('/categorias/{id}')
async def del_categoria(del_categoria: CategoriaObtSchema):
     return CategoriaService.delete_categoria(del_categoria)