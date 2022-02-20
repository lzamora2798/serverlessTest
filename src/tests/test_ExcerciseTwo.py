import sys 
sys.path.append('..')
import unittest
import exerciseTwo as target

class Testing(unittest.TestCase):

    def test_empty_filter(self):   
        file = open("../resources/ex1.csv","r")
        filters = {}
        c = target.buildFilter(file,filters)
        b = []
        file.close()
        self.assertEqual(c, b)
    
    def test_exact_date_filter(self):
        file = open("../resources/ex1.csv","r")
        filters = {"timestamp":"20211102T00:00"}
        c = target.buildFilter(file,filters)
        b = ['20211102T00:00 - APP1 - SUCCESS: No problem here.',
            '20211102T00:00 - APP2 - SUCCESS: No problem here.',
            '20211102T00:00 - APP1 - SUCCESS: No error this time.']
        file.close()
        self.assertEqual(c, b)
    
    def test_range_date_severity_filter(self):
        file = open("../resources/ex1.csv","r")
        filters = {"timestamp":"20211101T00:00-20211106T20:00","severity":"3"}
        c = target.buildFilter(file,filters)
        b = ['20211105T00:02 - APP2 - ERROR [3]: Severe error.']
        file.close() #close file in last test
        self.assertEqual(c, b)
    
    def test_range_date_app_filter(self):
        file = open("../resources/ex1.csv","r")
        filters = {"timestamp":"20211101T00:00-20211106T20:00","application":"app2"}
        c = target.buildFilter(file,filters)
        b = ["20211105T00:02 - APP2 - ERROR [3]: Severe error.",
            "20211102T00:00 - APP2 - SUCCESS: No problem here.",
            "20211106T00:02 - APP2 - ERROR [1]: Non-severe error."]
        file.close() #close file in last test
        self.assertEqual(c, b)
    
    def test_range_date_invalid_filter(self):
        file = open("../resources/ex1.csv","r")
        filters = {"timestamp":"20211101T00:00-20211106T20:00","application":"appi$$"}
        c = target.buildFilter(file,filters)
        b = []
        file.close()
        self.assertEqual(c, b)

    def test_nofilter(self):
        file = open("../resources/ex1.csv","r")
        c = target.buildFilter(file)
        file.close()
        b = []
        self.assertEqual(c, b)

    def test_invalid_file(self):
        filters = {"timestamp":"20211101T00:00-20211106T20:00","application":"app2"}
        file = open("../resources/ex1-no-format-2.csv","r")
        c = target.buildFilter(file,filters)
        file.close()
        b = {'status': 'invalid file'}
        self.assertEqual(c, b)    
if __name__ == '__main__':
    unittest.main()