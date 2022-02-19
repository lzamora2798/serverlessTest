import json
import cgi
import io
from datetime import datetime
def buildFormDic(event):
    fp = io.BytesIO(event['body'].encode('utf-8'))
    pdict = cgi.parse_header(event['headers']['Content-Type'])[1]
    if 'boundary' in pdict:
        pdict['boundary'] = pdict['boundary'].encode('utf-8')
    pdict['CONTENT-LENGTH'] = len(event['body'])
    form_data = cgi.parse_multipart(fp, pdict)
    return form_data


def compareDates(d1,d2,d):
    date_format = "%Y%m%dT%H:%M"
    date_obj1 = datetime.strptime(d1,date_format)
    date_obj2 = datetime.strptime(d2,date_format)
    date_d = datetime.strptime(d,date_format)
    if date_obj1 <= date_d <= date_obj2:
        return True
    return False