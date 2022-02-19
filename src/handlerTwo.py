import json
import re
from src.utils import buildFormDic, compareDates

dic_of_keys = {  # dic to filter 
    "TIMESTAMP": 0, 
    "APPLICATION":1,
    "CATEGORY":2,
    "SEVERITY":2
}

set_of_keys = ("ERROR", "SUCCESS", "INFO")



def buildList(data):    
    newList = data["file"][0].decode('UTF-8').split("\n")
    value = data["value"][0].decode('UTF-8').upper()
    filter_txt = data["type"][0].decode('UTF-8').upper()
    finalList = []
    if filter_txt in dic_of_keys:
        dic_key = dic_of_keys[filter_txt]
        for i in newList:
            tmpData = i.strip().split(" - ")[dic_key].upper()
            if dic_key==0: # is a timestamp
                date1,date2 = value.split("-") # expenting range date with this format date1-date2
                if compareDates(date1,date2,tmpData):
                    finalList.append(i.strip())
            if dic_key==2: # is a category or error
                category_data = re.search(".*:", tmpData).group()
                if filter_txt == "CATEGORY" and value in category_data and value in set_of_keys:
                    finalList.append(i.strip())
                elif filter_txt == "SEVERITY" and value in category_data:
                    finalList.append(i.strip())
            else:
                if value == tmpData:
                    finalList.append(i.strip())
        return finalList
    return Exception

def filter(event, context):
    try:
        form_data = buildFormDic(event)
        finalList = buildList(form_data)
        if len(finalList) > 0:
            response = {"statusCode": 200, "body": json.dumps(finalList)}
        else:
            response = {"statusCode": 400, "body": json.dumps({"message":"No Data"})}
        return response
    except Exception as ex: 
        body = {
            "message": "Error Processing the lambda"
        }
        print(ex)
        return {"statusCode": 500, "body": json.dumps(body)}