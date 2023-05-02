from pydantic import BaseModel


class ModelsIn(BaseModel):
    codigo: str
    nome: str


class ModelsOut(BaseModel):
    codigo: str
    nome: str


class BrandIn(BaseModel):
    codigo: str
    nome: str
