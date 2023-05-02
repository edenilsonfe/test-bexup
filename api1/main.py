from typing import Any, List

from fastapi import FastAPI

from api1.repository.fipe_repository import FIPERepository
from api1.messaging.publisher import RabbitMQPublisher

from api1.services.fipe_service import send_brand_to_queue

app = FastAPI()
repo = FIPERepository()
publisher = RabbitMQPublisher("brands")


@app.get("/load_brands_from_api", status_code=200)
async def load_brands_from_api() -> Any:
    brands = repo.get_all_brands()
    await send_brand_to_queue(brands)
    return brands


@app.get("/brands", status_code=200)
async def load_brands_from_db() -> Any:
    brands = repo.get_all_brands_from_database()
    return brands


@app.get("/load_brands_with_models_from_database", status_code=200)
async def load_brands_with_models_from_database() -> Any:
    print("loading brands from db")
    brands = repo.get_all_brands_with_models_from_database()
    return brands


@app.get("/vehicle/{brand_id}", status_code=200)
async def get_vehicle_by_brand(brand_id: str) -> Any:
    print("loading brands from db")
    brands = repo.get_vehicle_by_brand_id(brand_id)
    print(brands)
    return brands
