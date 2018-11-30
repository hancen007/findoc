import unittest
from test_demo import myTest
from test_demo0 import youTest

#构造一个场景
suites  = unittest.TestSuite()
suites.addTest(myTest('test_verify_2_3'))
suites.addTest(youTest('test_case_b_1'))

if __name__ == '__main__':
    #unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suites)
