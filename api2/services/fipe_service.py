import re
from typing import List

import requests

from api2.models.models import BrandIn, ModelsIn
from api2.services.base_config import BASE_URL


def get_models_by_brand(brand: BrandIn):
    try:
        response = requests.get(BASE_URL + f"carros/marcas/{brand.codigo}/modelos")
        models = [
            ModelsIn(codigo=model["codigo"], nome=model["nome"]).json()
            for model in response.json()["modelos"]
        ]
        return models
    except Exception as e:
        # Add policy to retry
        print("Error: ", e)
        return []
