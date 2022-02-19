import json
from src.utils import buildFormDic

def buildDic(data):
    newList = data["file"][0].decode('UTF-8').split("\n")
    newDic = {}
    for i in newList:
        tmpData = i.strip().split(" - ")[2].split(":")[0].lower()
        if "error" in tmpData:
            newDic["ErrorCount"] = newDic.get("ErrorCount",0)+1
        elif "success" in tmpData:
            newDic["SuccessCount"] = newDic.get("SuccessCount",0)+1
        newDic["Total"] = newDic.get("Total",0)+1
    return newDic

def statistics(event, context):
    try:
        form_data = buildFormDic(event)
        finalDic = buildDic(form_data)
        response = {"statusCode": 200, "body": json.dumps(finalDic)}
        return response
    except Exception as ex: 
        body = {
            "message": "Error on the lambda"
        }
        print(ex)
        return {"statusCode": 500, "body": json.dumps(body)}