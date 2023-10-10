from node import Node
import unittest

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        data = 42
        node = Node(data)
        self.assertEqual(node.data, data)
        self.assertIsNone(node.next)

if __name__ == '__main__':
    unittest.main()
