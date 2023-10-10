from linked_list import Linked_List
import unittest


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        """Create a new Linked_List instance before each test"""
        self.linked_list = Linked_List()

    def tearDown(self) -> None:
        """Reset the state of the linked list after each test"""
        self.linked_list = None

    def test_insert_at_beginning(self) -> None:
        """Test inserting a node at the beginning of the linked list.

        - First, insert a node in an empty list and assert the expected behavior.
        - Second, insert another node and verify that it becomes the new head of the list.
        """
        # first insert in list
        data = 42
        self.linked_list.insert_at_beginning(data)
        self.assertEqual(self.linked_list.head.data, data)
        self.assertIsNone(self.linked_list.head.next)

        # second insert in list
        data = 95
        self.linked_list.insert_at_beginning(data)
        self.assertEqual(self.linked_list.head.data, data)

        # third insert in list
        data = 55
        self.linked_list.insert_at_beginning(data)
        self.assertEqual(self.linked_list.head.data, data)

    def test_insertAtIndex(self) -> None:
        self.test_insert_at_beginning()
        index, data = 2, 101
        self.linked_list.insertAtIndex(data, index)

        current_node = self.getposition(index)
        self.assertEqual(current_node.data, data)

    def getposition(self, index:int):
        current_node = self.linked_list.head
        position = 0
        while position != index:
            current_node = current_node.next
            position += 1
        return current_node


if __name__ == '__main__':
    unittest.main()
