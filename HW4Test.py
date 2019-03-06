import unittest
from HW4 import GitZeHub

class testHW4GitHub(unittest.TestCase):
    def testUser1(self):
        self.assertEqual(gitHubAPI("nudeagba"), [ ('GitAPITesting', 1), ('TriTesting', 5), ('GEDcom', 1), ('starterweb', 3)])  
    
    def testUser2(self):
        self.assertEqual(gitHubAPI("richkempinski"), [('hellogitworld', 30), ('helloworld', 2), ('Project1', 2), ('threads-of-life', 1)])

if __name__ == '__main__':
    print('Testing...')
    unittest.main(exit = False)
