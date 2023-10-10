from linked_list import Linked_List
from node import Node
import unittest


class TestLinked_List(unittest.TestCase):
    """
    This test suite includes test cases for various methods and behaviors of the
    Linked_List class.
    """

    def setUp(self) -> None:
        """Create a new Linked_List instance before each test"""
        self.linked_list = Linked_List()

    def tearDown(self) -> None:
        """Reset the state of the linked list after each test"""
        self.linked_list = None

    def test_insertAtBeginning(self) -> None:
        """Test inserting a node at the beginning of the linked list.

        - First, insert a node in an empty list and assert the expected behavior.
        - Second, insert another node and verify that it becomes the new head of the
          list.
        """
        # first insert in list
        data = 42
        self.linked_list.insertAtBeginning(data)
        self.assertEqual(self.linked_list.head.data, data)
        self.assertIsNone(self.linked_list.head.next)

        # second insert in list
        data = 95
        self.linked_list.insertAtBeginning(data)
        self.assertEqual(self.linked_list.head.data, data)

        # third insert in list
        data = 55
        self.linked_list.insertAtBeginning(data)
        self.assertEqual(self.linked_list.head.data, data)


    def test_insertAtIndex(self) -> None:
        """Test inserting a new node at a specified index in the linked list."""
        self.test_insertAtBeginning()
        index, data = 2, 101
        self.linked_list.insertAtIndex(data, index)

        current_node = self.getposition(index)
        self.assertEqual(current_node.data, data)


    def getposition(self, index:int) -> Node:
        """
        Get the node at a specified index in the linked list.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Node: The node at the specified index.
        """
        current_node = self.linked_list.head
        position = 0
        while position != index:
            current_node = current_node.next
            position += 1
        return current_node


if __name__ == '__main__':
    unittest.main()
