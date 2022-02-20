import json
import boto3
from dotenv import load_dotenv
from src.exerciseTwo import buildFilter
import warnings
warnings.simplefilter("ignore", ResourceWarning)
load_dotenv()

BUCKET_NAME = "local-bucket"

def notify(email,text):
   print( "Sending email to {0} with the name of the log \n '{1}'".format(email,text) )

def listOfSubscribers():
    return ["luis.zv27@gmail.com-APP2-SUCCESS","luis.zv27@gmail.com-APP2-ERROR"]

def createClient():
    try:
        client = boto3.client('s3', endpoint_url='http://localhost:4002',aws_access_key_id='S3RVER',
            aws_secret_access_key= 'S3RVER')
        return client
    except Exception:
        return Exception

def email(event, context):
    object_info = event["Records"][0]["s3"]["object"]
    object_name = object_info["key"]
    try:
        s3 = createClient()
        file = s3.get_object(Bucket=BUCKET_NAME,Key=object_name).get("Body",False)
        subs_list = []
        if file:
            list_Subscribers = listOfSubscribers()
            file = file.read().decode().split("\n")
            for i in list_Subscribers:
                data = i.strip().split("-")
                filter_dic = {"APPLICATION":data[1],"CATEGORY":data[2]}
                listContent = buildFilter(file,filter_dic)
                if len(listContent) >0:
                    tmpdic={data[0]:listContent}
                    listContent = "\n".join(listContent)
                    # use for sending email
                    #notify(data[0],listContent) 
                    subs_list.append(tmpdic)
            return json.dumps(subs_list)
        return None
    except Exception as ex:
        return None