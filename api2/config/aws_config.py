import os

import boto3

sqs = boto3.client(
    "sqs",
    region_name="us-east-1",
    aws_access_key_id="xxx",
    aws_secret_access_key="xxx",
)
