from schemas import ProdutoSchema, CategoriaSchema, QuerySchema, CategoriaObtSchema
from fastapi import HTTPException 

produtos = []
categorias = {}

class ProdutoService:
    @staticmethod
    def listar_produtos(page_limit):
        lista_completa = list(categorias.values()) 
        total = len(lista_completa)
        start = (page_limit.page - 1) * page_limit.limit
        end = start + page_limit.limit
        if produtos == []:
            return {"mensagem": "Nenhum produto cadastrado"}
        return {"items": lista_completa[start:end], "page": page_limit.page, "limit": page_limit.limit, "total": total}
    
    @staticmethod
    def adicionar_produto(produto_schema):
        if produto_schema.categoria_id not in categorias:
            raise HTTPException(status_code=404, detail='Categoria não encontrada')
        if any (produto.nome == produto_schema.nome for produto in produtos):
             raise HTTPException(status_code=400, detail="Produto já existe")
        if any (produto.id == produto_schema.id for produto in produtos):
             raise HTTPException(status_code=409, detail="ID do produto já existe")
        if produtos == []: 
            produtos.append(produto_schema)
            return{'mensagem': 'Produto adicionado com sucesso', 'produto': produto_schema}
        produtos.append(produto_schema)
        return{'mensagem': 'Produto adicionado com sucesso','produto': produto_schema}
    
    @staticmethod
    def obter_produto(produto):        
        for p in produtos:
            if p.id == produto.id:
                return p
        raise HTTPException(status_code=404, detail='Produto não encontrado')

    @staticmethod
    def produto_atualizar(produto):
        if any (p.nome == produto.nome for p in produtos):
             raise HTTPException(status_code=409, detail="Produto já existe")
        for index, p in enumerate(produtos):
            if p.id == produto.id:
                produtos[index] = produto
                return {'message':'produto atualizado com sucesso'}
        raise HTTPException(status_code=404, detail='produto não encontrado')
    
    @staticmethod
    def deletar_produto(del_produto):
        for index, p in enumerate(produtos):
            if p.id == del_produto.id:
                produtos.pop(index)
                return {'mensagem':'produto deletado com sucesso'}
        raise HTTPException(status_code=404, detail='Produto não encontrado')

class CategoriaService:
    @staticmethod
    def listar_categorias(page_limit):
        lista_completa = list(categorias.values()) 
        total = len(lista_completa)
        start = (page_limit.page - 1) * page_limit.limit
        end = start + page_limit.limit
        if categorias == {}: return {'mensagem': 'Nenhum produto cadastrado'}
        return {"items": lista_completa[start:end], "page": page_limit.page, "limit": page_limit.limit, "total": total}
    
    @staticmethod
    def adicionar_categoria(categoria):
        if categoria.id in categorias:
            raise HTTPException(status_code=409, detail="ID da categoria já existe")  
        if any (cat.nome == categoria.nome for cat in categorias.values()):
            raise HTTPException(status_code=409, detail="Categoria já existe")
        if categorias == {}: 
            categorias[categoria.id] = categoria
            return{'mensagem': 'Categoria adicionada com sucesso', 'categoria': categoria}
        categorias[categoria.id] = categoria
        return{'mensagem': 'Categoria adicionada com sucesso','categoria': categoria}
    
    @staticmethod
    def obter_categoria(categoria):
        resultado = categorias.get(categoria.id)
        if resultado:
            return resultado
        else: 
            raise HTTPException(status_code=404, detail='categoria não encontrada')
        
    @staticmethod
    def atualizar_categoria(atu_categoria):
        resultado = categorias.get(atu_categoria.id)
        if any (c.nome == atu_categoria.nome for c in categorias.values()):
            raise HTTPException(status_code=409, detail='Já existe uma categoria com este nome')
        if resultado:
            categorias[atu_categoria.id] = atu_categoria
            return{'mensagem': 'categoria atualizada com sucesso'}
        else: 
            raise HTTPException(status_code=404, detail='categoria não encontrada')
    
    @staticmethod
    def delete_categoria(del_categoria):
        if del_categoria.id not in categorias:
            raise HTTPException(status_code=404, detail='Categoria não encontrada')
        if any(produto.categoria_id == del_categoria.id for produto in produtos):
            raise HTTPException(status_code=409, detail='Não é possível deletar a categoria pois ela possui produtos associados')
        del categorias[del_categoria.id]
        return {'mensagem': 'categoria deletada com sucesso'}
