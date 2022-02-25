

def buildStadistics(file=[]):  
    newDic = {}
    try:
        for i in file:
            tmpData = i.strip().split(" - ")[2].split(":")[0].lower()
            if "error" in tmpData:
                newDic["ErrorCount"] = newDic.get("ErrorCount",0)+1
            elif "success" in tmpData:
                newDic["SuccessCount"] = newDic.get("SuccessCount",0)+1
            newDic["Total"] = newDic.get("Total",0)+1
        return newDic
    except IndexError as ex:
        return {"status":"invalid file"}
