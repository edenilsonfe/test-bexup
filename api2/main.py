from fastapi import FastAPI

from api2.messaging.subscriber import Subscriber

app = FastAPI()
# repo = AWSRepository() # Used to get the data from the SQS
messaging = Subscriber("brands")
messaging.start_consuming()
