class Node:
    """
    Node class for implementing a singly linked list.

    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the linked list.
    """

    def __init__(self, data) -> None:
        """
        Initializes a new node with the given data.

        Args:
            data: The data to be stored in the node.

        Example:
            node = Node(42)  # Creates a new node with data value 42.
        """
        self.data = data
        self.next = None
