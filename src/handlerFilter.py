import json
from multiprocessing import Event
from src.exerciseTwo import buildFilter


def getLastLogs(): #assuming this returns last logs 
    return open("resources/ex1.csv","r")

def filterLogs(event, context):
    try:
        last_logs = getLastLogs()
        filter_dic = json.loads(event["body"])
        finalList = buildFilter(last_logs,filter_dic)
        if len(finalList) > 0:
            response = {"statusCode": 200, "body": json.dumps(finalList)}
        else:
            response = {"statusCode": 400, "body": json.dumps({"message":"No Data"})}
        return response
    except Exception as ex: 
        body = {
            "message": "Error Processing the lambda"
        }
        return {"statusCode": 500, "body": json.dumps(body)}
    finally:
        last_logs.close()