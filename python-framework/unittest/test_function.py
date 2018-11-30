import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def tearDown(self):
        pass

    def test_choice(self):
        #从序列seq中随机选取一个元素
        element = random.choice(self.seq)

        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq,20)
        for element in random.sample(self.seq,5):
            self.assertTrue(element in self.seq)

class TestDicValueFormatFuntions(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        '''随机打乱seq的顺序'''
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq,range(10))
        #验证执行函数时抛出的TypeError异常
        self.assertRaises(TypeError,random.shuffle,(1,2,3))



if __name__ == '__main__':
    #根据给定测试类，获取其中的所有以test开头的测试方法，并返回一个测试套件
    #TestLoader类：用例加载器，返回一个用例集合
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testcase2 = unittest.TestLoader().loadTestsFromTestCase(TestDicValueFormatFuntions)

    suite = unittest.TestSuite([testCase1,testcase2])
    #verbosity =0 输出结果不提示执行成功数
    #verbosity =1 输出结果仅以(.)表示执行成功数
    #verbosity =2 输出结果仅以(详细内容)表示执行成功数
    unittest.TextTestRunner(verbosity=2).run(suite)
