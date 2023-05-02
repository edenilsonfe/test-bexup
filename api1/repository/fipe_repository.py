import json
from typing import List
from pprint import pprint

import requests

from api1.models.brand_models import BrandOut, BrandWithModelsOut
from api1.services.base_config import BASE_URL

from typing import List
from api1.database.mongo_database import MongoDBConnection


class FIPERepository:
    def __init__(self):
        self.base_url = BASE_URL
        self.connection = MongoDBConnection().conn()

    def get_brand(self, carro_id: str) -> BrandOut:
        url = f"{self.base_url}carros/marcas/{carro_id}/modelos"
        response = requests.get(url)
        data = response.json()
        return BrandOut(**data)

    def get_all_brands(self) -> List[BrandOut]:
        url = f"{self.base_url}carros/marcas"
        response = requests.get(url)
        data = response.json()
        return [BrandOut(**item) for item in data]

    def get_all_brands_from_database(self) -> List[BrandOut]:
        brands = self.connection.find("brands", query={})
        brands = [
            BrandOut(codigo=item.get("codigo"), nome=item.get("nome"))
            for item in brands
        ]
        return brands

    def get_all_brands_with_models_from_database(self) -> List[BrandWithModelsOut]:
        brands = self.connection.find("brands", query={})
        brands = [
            BrandWithModelsOut(
                codigo=item.get("codigo"),
                nome=item.get("nome"),
                modelos=[json.loads(modelo) for modelo in item.get("modelos")],
            )
            for item in brands
            if len(item) > 0
        ]
        return brands

    def get_vehicle_by_brand_id(self, brand_id: str) -> BrandWithModelsOut:
        vehicle = self.connection.find_one("brands", query={"codigo": brand_id})
        return BrandWithModelsOut(
            codigo=vehicle.get("codigo"),
            nome=vehicle.get("nome"),
            modelos=[json.loads(modelo) for modelo in vehicle.get("modelos")],
        )
