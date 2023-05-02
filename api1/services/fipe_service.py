from typing import List
from api1.messaging.publisher import RabbitMQPublisher
from api1.models.brand_models import BrandOut
from api1.services.base_config import BASE_URL

publisher = RabbitMQPublisher("brands")


async def send_brand_to_queue(brands: List[BrandOut]) -> None:
    for brand in brands:
        publisher.publish(brand.json())
        print(f"brand sent to queue: {brand.json()}")
