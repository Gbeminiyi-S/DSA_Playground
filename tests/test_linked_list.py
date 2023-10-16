from linked_list import Linked_List
from node import Node
import unittest

class TestLinkedList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a Linked_List instance once for all test cases in this class."""
        cls.linked_list = Linked_List()

    def test_insert_at_beginning(self):
        """Test inserting a node at the beginning of the linked list."""
        self.linked_list.insertAtBeginning(42)
        self.assertEqual(self.linked_list.head.data, 42)


    def test_insert_at_index(self):
        """Test inserting a new node at a specified index in the linked list."""
        linked_list = Linked_List()
        linked_list.insertAtBeginning(42)
        linked_list.insertAtBeginning(95)
        linked_list.insertAtBeginning(55)

        linked_list.insertAtIndex(101, 2)
        current_node = self.get_position(linked_list.head, 2)
        self.assertEqual(current_node.data, 101)

        with self.assertRaises(IndexError):
            linked_list.insertAtIndex(100, -2)

    def test_insert_at_end(self):
        """Test inserting a new node at the end of the linked list."""
        linked_list = Linked_List()
        linked_list.insertAtBeginning(42)
        linked_list.insertAtBeginning(95)
        linked_list.insertAtBeginning(55)

        linked_list.insertAtEnd(-5)
        current_node = self.get_position(linked_list.head, 3)
        self.assertEqual(current_node.data, -5)

    def test_update_node(self):
        """Test updating a node's data in the linked list."""
        linked_list = Linked_List()
        linked_list.insertAtBeginning(42)
        linked_list.insertAtBeginning(95)
        linked_list.insertAtBeginning(55)

        linked_list.updateNode(1000, 2)
        current_node = self.get_position(linked_list.head, 2)
        self.assertEqual(current_node.data, 1000)

        with self.assertRaises(IndexError):
            linked_list.updateNode(100, -2)

    def get_position(self, node, index):
        """Get the node at a specified index in the linked list."""
        current_node = node
        position = 0
        while position != index:
            current_node = current_node.next
            position += 1
        return current_node

if __name__ == '__main__':
    unittest.main()
