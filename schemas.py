from pydantic import BaseModel, Field

class ProdutoSchema(BaseModel):
    id: int = Field(gt=0)
    nome: str = Field(min_length=2, max_length=100)
    preco: float = Field(gt=0)
    categoria_id: int = Field(gt=0)

class CategoriaSchema(BaseModel):
    id: int = Field(gt=0)
    nome: str = Field(min_length=2, max_length=100)

class QuerySchema(BaseModel):
    page: int = Field(1, ge=1)
    limit: int = Field(20, ge=1, le=100)

class CategoriaObtSchema(BaseModel):
    id: int = Field(gt=0)

class ProdutoObtSchema(BaseModel):
    id: int = Field(gt=0)