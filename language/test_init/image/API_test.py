import unittest

class StringTestCase(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.test_string = "This is a string"

    def testUpper(self):
        # Act and Assert
        self.assertEqual("THIS IS A STRING", self.test_string.upper())

if __name__ == '__main__':
    unittest.main()
