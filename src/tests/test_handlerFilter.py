import sys 
sys.path.append('..')
import unittest
import exerciseTwo as target
import requests
import json

class Testing(unittest.TestCase):

    API_ENDPOINT = "http://localhost:3000/filter"
    def test_filter(self):   
        filters = {"timestamp":"20211101T00:00-20211106T20:00","application":"app2"}
        r = requests.post(url = self.API_ENDPOINT, data = json.dumps(filters))  
        r = json.loads(r.text)
        b = [
            "20211105T00:02 - APP2 - ERROR [3]: Severe error.",
            "20211102T00:00 - APP2 - SUCCESS: No problem here.",
            "20211106T00:02 - APP2 - ERROR [1]: Non-severe error."
        ]
        self.assertEqual(r, b)
    def test_category_filter(self):   
        filters = {"timestamp":"20211101T00:00-20211106T20:00","category":"success"}
        r = requests.post(url = self.API_ENDPOINT, data = json.dumps(filters))  
        r = json.loads(r.text)
        b = [
            "20211102T00:00 - APP1 - SUCCESS: No problem here.",
            "20211102T00:00 - APP2 - SUCCESS: No problem here.",
            "20211102T00:00 - APP1 - SUCCESS: No error this time."
        ]
        self.assertEqual(r, b)    
    def test_no_filter(self):   
        filters = {}
        r = requests.post(url = self.API_ENDPOINT, data = json.dumps(filters))  
        r = json.loads(r.text)
        b = {"message": "No Data"}
        self.assertEqual(r, b) 
if __name__ == '__main__':
    unittest.main()



