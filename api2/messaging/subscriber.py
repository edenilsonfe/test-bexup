import json

import pika

from api2.database.mongo_database import MongoDBConnection
from api2.models.models import BrandIn
from api2.services.fipe_service import get_models_by_brand


class Subscriber:
    def __init__(self, queue_name):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                "rabbitmq", credentials=pika.PlainCredentials("rabbitmq", "rabbitmq")
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
        self.queue_name = queue_name
        self.mongodb_connection = MongoDBConnection.conn()

    def callback(self, ch, method, properties, body):
        print(f" [x] Received {json.loads(body)['codigo']} {json.loads(body)['nome']}")
        models = get_models_by_brand(
            BrandIn(codigo=json.loads(body)["codigo"], nome=json.loads(body)["nome"])
        )

        payload = {
            "codigo": json.loads(body)["codigo"],
            "nome": json.loads(body)["nome"],
            "modelos": models,
        }

        self.mongodb_connection.insert_one(collection="brands", data=payload)

    def start_consuming(self):
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self.callback, auto_ack=True
        )
        print(" [*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()

    def close_connection(self):
        self.connection.close()
