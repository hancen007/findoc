import unittest

class youTest(unittest.TestCase):

    #ACsII码
    def mutiadd(self,a,b):
        '''被测试的代码或者程序'''
        return a + b

    def test_case_b_1(self):
        '''这个一个测试用例'''
        a = 3
        b = 3
        self.assertEqual(self.mutiadd(a,b),6)

    def test_case_b_2(self):
        '''这个一个测试用例'''
        a = 2
        b = 3
        self.assertEqual(self.mutiadd(a,b),6)
if __name__ == '__main__':
    unittest.main(verbosity=2)
