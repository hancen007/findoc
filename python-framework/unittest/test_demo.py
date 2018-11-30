import unittest


class myTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('--这是一个类级别是的初始化--')
    @classmethod
    def tearDownClass(cls):
        print('--这个一个类级别的结束--')

    def setUp(self):
        print('--这个是一个方法级别的初始化')
    def tearDown(self):
        print('--这个是一个方法级别的结束')


    def mutiadd(self,a,b):
        '''被测试的代码或者程序'''
        return a + b

    def test_verify_3_3(self):
        '''这个一个测试用例'''
        a = 3
        b = 3
        print('这个verfiy2-3')
        self.assertEqual(self.mutiadd(a,b),6)

    def test_verify_2_3(self):
        '''这个一个测试用例'''
        a = 2
        b = 3
        self.assertEqual(self.mutiadd(a,b),6)

    def test_verify_1_3(self):
        '''这个一个测试用例'''
        a = 1
        b = 3
        self.assertTrue(self.mutiadd(a,b),5)


if __name__ == '__main__':
    unittest.main(verbosity=2)

    pytest.main(["-s,test_dddd.py"])
