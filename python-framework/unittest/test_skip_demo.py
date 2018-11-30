import unittest

'''
unittest.skip(reason) 无条件地跳过装饰的测试，说明跳过测试的原因。
unittest.skipIf(condition, reason) 跳过装饰的测试，如果条件为真时。
unittest.skipUnless(condition, reason) 跳过装饰的测试，除非条件为真。
unittest.expectedFailure 测试标记为失败。不管执行结果是否失败，统一标记为失败
'''
class MyTest(unittest.TestCase):

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(3 > 2, "当条件为 True 时跳过测试")
    def test_skip_if(self):
        print('test bbb')

    @unittest.skipUnless(3 > 2, "当条件为 True 时执行测试")
    def test_skip_unless(self):
        print('test ccc')

    @unittest.expectedFailure
    def test_expected_failure(self):
        assertEqual(2, 3)

if __name__ == '__main__':
    unittest.main()
