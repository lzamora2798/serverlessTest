import sys 
sys.path.append('src')
import unittest
import exerciseOne as target

class Testing(unittest.TestCase):
    def test_file(self):
        file = open("resources/ex1.csv","r")
        c = target.buildStadistics(file)
        file.close()
        b = {'SuccessCount': 3, 'Total': 9, 'ErrorCount': 5}
        self.assertEqual(c, b)

    def test_no_file(self):
        c = target.buildStadistics()
        b = {}
        self.assertEqual(c, b)

    def test_different_file_one(self):
        file = open("resources/ex1-no-format-1.csv","r")
        c = target.buildStadistics(file)
        file.close()
        b = {"status":"invalid file"}
        self.assertEqual(c, b)

    def test_different_file_two(self):
        file = open("resources/ex1-no-format-2.csv","r")
        c = target.buildStadistics(file)
        file.close()
        b = {"status":"invalid file"}
        self.assertEqual(c, b)
if __name__ == '__main__':
    unittest.main()