import pika


class RabbitMQPublisher:
    def __init__(self, queue_name):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                "rabbitmq", credentials=pika.PlainCredentials("rabbitmq", "rabbitmq")
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
        self.queue_name = queue_name

    def publish(self, message):
        self.channel.basic_publish(
            exchange="", routing_key=self.queue_name, body=message
        )
        print(f" [x] Sent {message}")

    def close_connection(self):
        self.connection.close()
