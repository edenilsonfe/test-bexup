import json
from typing import List

from api2.config.aws_config import sqs
from api2.services.base_config import BASE_URL


class AWSRepository:
    def __init__(self):
        self.base_url = BASE_URL

    def get_items_from_sqs(self) -> List[str]:
        queue_url = "https://sqs.us-east-1.amazonaws.com/324884266075/BrandsQueue"
        response = sqs.receive_message(
            QueueUrl=queue_url, MaxNumberOfMessages=1, WaitTimeSeconds=10
        )
        messages = response.get("Messages", [])

        messages = (
            [json.loads(message["Body"]) for message in messages] if messages else []
        )

        print(f"Number of messages received: {len(response.get('Messages', []))}")
        return messages
