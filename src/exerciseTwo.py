from datetime import datetime
from operator import le
import re
set_of_categorys = ("ERROR", "SUCCESS", "INFO")

dic_of_keys = {  # dic of index 
    "TIMESTAMP": 0, 
    "APPLICATION":1,
    "CATEGORY":2,
    "SEVERITY":3
}

def compareDates(date,d):
    date_format = "%Y%m%dT%H:%M"
    date_d = datetime.strptime(d,date_format)
    if "-" in date:
        d1,d2 = date.split("-")
        date_obj1 = datetime.strptime(d1,date_format)
        date_obj2 = datetime.strptime(d2,date_format)
        
        if date_obj1 <= date_d <= date_obj2:
            return True
        return False
    else: 
        date_t = datetime.strptime(date,date_format)
        if date_d == date_t:
            return True
        return False

def buildFilter(file,kwargs=""): 
    list = []
    if len(kwargs) ==0:
        return list
    try:    
        for i in file:
            tmpRow = i.strip().split(" - ")
            tmpCategory = re.search("^,*.*:",tmpRow[2]).group() #regular Expression
            tmpDicKeys = {}
            for k,v in kwargs.items():
                tmpDicKeys[k] =False # default false for filter propuse
                filter_index = dic_of_keys.get(k.upper(),None)
                if filter_index ==0:
                    if compareDates(v,tmpRow[0]):
                        tmpDicKeys[k]=True
                elif filter_index == 1:
                    if tmpRow[1].upper() ==v.upper():
                        tmpDicKeys[k]=True
                elif filter_index == 2:
                    if v.upper() in tmpCategory:
                        tmpDicKeys[k]=True
                elif filter_index == 3:            
                    tmpSeverity = re.search("\d{1,5}",tmpRow[2]) #regular Expression
                    if(tmpSeverity):
                        tmpSeverity= tmpSeverity.group()
                        if str(v) == tmpSeverity:
                            tmpDicKeys[k]=True
            if False not in tmpDicKeys.values(): #verify all the conditions
                list.append(i.strip())
        return list
    except IndexError as ex:
        return {"status":"invalid file"}
