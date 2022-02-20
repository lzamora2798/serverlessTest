import sys 
import unittest
sys.path.append('src')
import json
import handlerFilter as target

class Testing(unittest.TestCase):

    API_ENDPOINT = "http://localhost:3000/filter"
    def test_filter(self):   
        filters = {"body":json.dumps({"timestamp":"20211101T00:00-20211106T20:00","application":"app2"})}
        r = target.filterLogs(filters,"")
        r = json.loads(r.get("body"))
        b = ["20211105T00:02 - APP2 - ERROR [3]: Severe error.", 
            "20211102T00:00 - APP2 - SUCCESS: No problem here.", 
            "20211106T00:02 - APP2 - ERROR [1]: Non-severe error."]
        self.assertEqual(r, b)
    
    def test_category_filter(self):   
        filters = {"body":json.dumps({"timestamp":"20211101T00:00-20211106T20:00","category":"success"})}
        r = target.filterLogs(filters,"")
        r = json.loads(r.get("body"))
        b = [
            "20211102T00:00 - APP1 - SUCCESS: No problem here.",
            "20211102T00:00 - APP2 - SUCCESS: No problem here.",
            "20211102T00:00 - APP1 - SUCCESS: No error this time."
        ]
        self.assertEqual(r, b)    
    def test_no_filter(self):   
        filters = {}
        r = target.filterLogs(filters,"")
        r = json.loads(r.get("body"))
        b = {'message': 'Error Processing the lambda'}
        self.assertEqual(r, b) 
if __name__ == '__main__':
    unittest.main()



