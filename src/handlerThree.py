import json
import boto3
import os
from src.utils import buildFormDic
from dotenv import load_dotenv
load_dotenv()


def sendEmail(email,text):
   return "Sending email to {0} with the name of the log '{1}'".format(email,text) 

def upload(event,context):
    s3 = boto3.client('s3', endpoint_url='http://localhost:4002')
    with open("resources/ex1.csv","rb") as f:
        s3.upload_fileobj(f, "local-bucket", "OBJECT_NAME")
    body = {"message": sendEmail("luis.zv27@gmail.com","app2-log")}
    return {"statusCode": 200, "body": json.dumps(body)}

def email(event, context):
    object_info = event["Records"][0]["s3"]["object"]
    object_name = object_info["key"]
    print(object_name)