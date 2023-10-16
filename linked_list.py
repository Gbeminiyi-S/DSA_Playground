from node import Node


class Linked_List:
    """
    A singly linked list implementation.

    Attributes:
        head (Node | None): The head of the linked list, initially None.
    """


    def __init__(self) -> None:
        """
        Initializes an empty linked list.
        """
        self.head = None


    def print(self) -> None:
        """Prints the linked list"""
        current_node = self.head

        if current_node is None:
            print("Linked List is empty")
            return
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next


    def insertAtBeginning(self, data: int) -> None:
        """
        Inserts a new node with the given data at the beginning of the linked list.

        Args:
            data (int): The data to be stored in the new node.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


    def insertAtIndex(self, data: int, index: int) -> None:
        """
        Inserts a new node with the given data at the specified index in the linked list.

        Args:
            data (int): The data to be stored in the new node.
            index (int): The index at which the new node should be inserted.
        """
        new_node = Node(data)
        current_node = self.head
        position = 0

        if position is index:
            self.insert_at_beginning(data)
        else:
            while current_node and position != index - 1:
                current_node = current_node.next
                position += 1

            if current_node == None:
                print("Index out of range")
            else:
                new_node.next = current_node.next
                current_node.next = new_node


    def insertAtEnd(self, data: int) -> None:
        """
        Inserts a new node with the given data at the end of the linked list.

        Args:
            data (int): The data to be stored in the new node.
        """
        new_node = Node(data)
        current_node = self.head

        if self.head is None:
            self.head = new_node
        else:
            while (current_node.next is not None):
                current_node = current_node.next
            current_node.next = new_node


    def updateNode(self, new_data: int, index: int):
        """
        Updates the data of a node at a specified index in the linked list.

        Args:
            new_data (int): The new data.
            index (int): The index of the node.
        """
        current_node = self.head
        position = 0

        if position is index:
            current_node.data = new_data
        else:
            while current_node and position != index - 1:
                current_node = current_node.next
                position += 1

            if current_node == None:
                print("Index out of range")
            else:
                current_node.data = new_data



    def remove_first_node(self):
        """Deletes the first node in the linked list"""
        if (self.head):
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            print("Cannot remove the first node as the list is empty.")


    def remove_first_node(self):
        """Deletes the last node in the linked list"""
        current_node = self.head
    
        if (current_node):
            while current_node.next.next:
                current_node = current_node.next
            del current_node.next
            current_node.next = None
        else:
            print("Cannot remove the last node as the list is empty.")


