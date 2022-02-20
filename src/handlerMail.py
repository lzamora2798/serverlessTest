import json
from tkinter.messagebox import NO
import boto3
from dotenv import load_dotenv
import datetime 
from src.exerciseTwo import buildFilter
load_dotenv()

BUCKET_NAME = "local-bucket"

def notify(email,text):
   print( "Sending email to {0} with the name of the log \n '{1}'".format(email,text) )

def listOfSubscribers():
    return open("resources/subscriptions.csv","r")


def upload(event,context):
    s3 = boto3.client('s3', endpoint_url='http://localhost:4002')
    #structure for the name of the log object appName-TimeStamp
    log_name = 'log-{:%Y%m%dT%H:%M:%S}'.format(datetime.datetime.now())
    with open("resources/ex1.csv","rb") as f:
        s3.upload_fileobj(f,BUCKET_NAME, log_name)
    body = {"message": notify("luis.zv27@gmail.com","app2-log")}
    return {"statusCode": 200, "body": json.dumps(body)}

def email(event, context):
    object_info = event["Records"][0]["s3"]["object"]
    object_name = object_info["key"]
    s3 = boto3.client('s3', endpoint_url='http://localhost:4002')
    file = s3.get_object(Bucket=BUCKET_NAME,Key=object_name).get("Body",False)
    subs_dic = {}
    if file:
        list_Subscribers = listOfSubscribers()
        file = file.read().decode().split("\n")
        for i in list_Subscribers:
            data = i.strip().split("-")
            filter_dic = {"APPLICATION":data[1],"CATEGORY":data[2]}
            listContent = buildFilter(file,filter_dic)
            if len(listContent) >0:
                listContent = "\n".join(listContent)
                subs_dic[data[0]] = listContent
                notify(data[0],listContent)
        list_Subscribers.close()
        return subs_dic
    return None
