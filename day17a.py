class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class SpinLock:
    # Make this a CIRCULAR LINKED LIST...
    def __init__(self) -> None:
        self.head = None
        self.count = 0
        self.directory = {}

    def insert(self, val: int, after_target: int):
        new_node = Node(val)

        prev_node = self.get_node(after_target)
        new_node.next = prev_node.next
        prev_node.next = new_node

        self.directory[val] = new_node

    def get_node(self, val):
        if not self.directory[val]:
            raise KeyError("?????")
        return self.directory[val]

    def append(self, val):
        new_node = Node(val)
        self.directory[val] = new_node

        if not self.head:
            self.head = new_node
            return
        
        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        self.count += 1

ll = SpinLock()
ll.append(0) # head
ll.insert(5, 0)
