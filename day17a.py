class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class SpinLock:
    
    def __init__(self) -> None:
        self.head = Node(0)
        self.head.next = self.head
        self.step_size = 366
        self.directory = { 0: self.head }

    def insert(self, val: int, after_target: int) -> Node:
        new_node = Node(val)

        prev_node = self.get_node(after_target)
        new_node.next = prev_node.next
        prev_node.next = new_node

        self.directory[val] = new_node
        return new_node

    def get_node(self, val) -> Node:
        if val not in self.directory:
            raise KeyError("?????")
        return self.directory[val]

    def iterate(self, current_position, next_val) -> Node:
        pos = self.get_node(current_position)
        for _ in range(self.step_size):
            pos = pos.next
        return self.insert(next_val, pos.val)

spinlock = SpinLock()
for i in range(1, 2018):
    spinlock.iterate(i - 1, i)

result: Node = spinlock.get_node(2017).next.val
print(f'Day 17 Part 1: The value in my completed cirular buffer after 2017 is {result}.\n')