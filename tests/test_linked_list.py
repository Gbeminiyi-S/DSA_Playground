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
        self.linked_list.insert_at_beginning(42)
        self.assertEqual(self.linked_list.head.data, 42)
        self.assertIsNone(self.linked_list.head.next)

        # second insert in list
        self.linked_list.insert_at_beginning(95)
        self.assertEqual(self.linked_list.head.data, 95)

if __name__ == '__main__':
    unittest.main()
