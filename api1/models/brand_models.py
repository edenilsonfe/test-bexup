from pydantic import BaseModel
from typing import List


class BrandIn(BaseModel):
    id: int
    codigo: str
    nome: str


class BrandOut(BaseModel):
    codigo: str
    nome: str


class ModelsOut(BaseModel):
    codigo: str
    nome: str


class BrandWithModelsOut(BrandOut):
    modelos: List[ModelsOut]
