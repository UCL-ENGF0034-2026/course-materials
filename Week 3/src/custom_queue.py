from simple_node import Node


class Queue:
    """A FIFO (First-In, First-Out) Queue implemented via a singly-linked list."""
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        """Enqueue an item at the tail in O(1) time."""
        n = Node(value)
        if self.head is None:
            self.head = n
        else:
            self.tail.append(n)
        self.tail = n

    def pop(self):
        """Dequeue the front item from the head in O(1) time."""
        if self.head is None:
            raise ValueError("Attempt to pop from empty queue")

        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            # We've removed the last item: reset tail to None (preserve class invariant)
            self.tail = None

        return value

    def is_empty(self):
        """Return True if queue is empty, False otherwise."""
        return self.head is None


def test_queue():
    q = Queue()
    try:
        q.pop()
    except ValueError as err:
        assert "Attempt to pop from empty queue" in str(err)

    lst = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    for item in lst:
        q.add(item)

    lst2 = []
    while not q.is_empty():
        lst2.append(q.pop())

    assert lst2 == lst

    try:
        q.pop()
    except ValueError as err:
        assert "Attempt to pop from empty queue" in str(err)


if __name__ == "__main__":
    test_queue()
    print("All Queue (custom_queue.py) tests passed successfully!")

