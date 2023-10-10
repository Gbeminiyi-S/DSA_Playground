from node import Node
import unittest

class TestNode(unittest.TestCase):
    """Test case for the creation of a node in a linked list."""

    def test_node_creation(self):
        """Tests the creation of a node with data."""
        data = 42
        node = Node(data)
        self.assertEqual(node.data, data)
        self.assertIsNone(node.next)

if __name__ == '__main__':
    unittest.main()
