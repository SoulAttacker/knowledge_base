import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        while not self.stack.is_empty():
            self.stack.pop()

    def test_prop(self):
        self.assertFalse(self.stack.__bool__())
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(0, self.stack.size())

    def test_op(self):
        self.stack.push(1)
        self.assertEqual(1, self.stack.peek())
        self.stack.pop()
        self.assertEqual(0, self.stack.size())
        

if __name__ == "__main__":
    unittest.main()
