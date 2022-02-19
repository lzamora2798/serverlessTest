import json
import boto3
import os
from src.utils import buildFormDic
from dotenv import load_dotenv
load_dotenv()


def upload(event,context):
    s3 = boto3.client('s3',
        aws_access_key_id='server',
    aws_secret_access_key='server'
    )
    with open("resources/ex1.csv","rb") as f:
        s3.upload_fileobj(f, "local-bucket", "OBJECT_NAME")
    # print(s3.get_available_subresources())
    body = {"message": "hi"}
    return {"statusCode": 200, "body": json.dumps(body)}

def email(event, context):
    print(event,"luis")
    print(context)