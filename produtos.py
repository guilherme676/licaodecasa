from fastapi import APIRouter, Query
from services import ProdutoService
from schemas import ProdutoSchema, QuerySchema, ProdutoObtSchema
from typing import Annotated

produto_router = APIRouter()

@produto_router.get("/produtos")
async def get_produtos(params: Annotated[QuerySchema, Query()]):
    return ProdutoService.listar_produtos(params)

@produto_router.post("/produtos")
async def add_produto(produto: ProdutoSchema):
    return ProdutoService.adicionar_produto(produto)
    
@produto_router.get('/produtos/{id}')
async def obter_produto(produto: Annotated[ProdutoObtSchema, Query()]):
    return ProdutoService.obter_produto(produto)

@produto_router.put('/produtos/{id}')
async def atualizar_produto(params: Annotated[ProdutoSchema, Query()]):
    return ProdutoService.produto_atualizar(params)

@produto_router.delete('/produtos')
async def del_produto(produto: ProdutoObtSchema):
    return ProdutoService.deletar_produto(produto)