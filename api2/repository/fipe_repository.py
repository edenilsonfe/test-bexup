from typing import List

import requests

from api2.services.base_config import BASE_URL


from api2.models.models import ModelsOut


class FIPERepository:
    def __init__(self):
        self.base_url = BASE_URL

    def get_data_by_brand(self, brand: str) -> List[ModelsOut]:
        url = f"{self.base_url}carros/marcas/{brand}/modelos"
        response = requests.get(url)
        data = response.json()
        return data
