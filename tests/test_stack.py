import unittest
from udpkv.stack import Stack

class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_add(self):
        assert self.stack.add('key1','value1') == True

    def test_pop(self):
        self.stack.add('key1','value1')
        assert self.stack.pop('key1') == 'value1'

if __name__ == '__main__':
    unittest.main()
