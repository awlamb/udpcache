import unittest
from udpkv.stack import Stack

class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        assert self.stack.add('key1','value1') == True

if __name__ == '__main__':
    unittest.main()
