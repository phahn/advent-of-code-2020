from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.first = None
        self.D = {}

    def find_node(self, val):
        return self.D[val]

    def insert_after(self, ref_node, val):
        new_node = Node(val)
        self.D[val] = new_node
        new_node.prev = ref_node
        new_node.next = ref_node.next
        new_node.next.prev = new_node
        ref_node.next = new_node

    def insert_at_end(self, val):
        if self.first is None:
            new_node = Node(val)
            self.D[val] = new_node
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, val)

    def remove(self, node):
        val = node.data
        if self.first.next == self.first:
            self.first = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if self.first == node:
                self.first = node.next
        return val


def day23(numbers, moves, target):
    n = CircularDoublyLinkedList()

    for num in numbers:
        n.insert_at_end(int(num))

    for x in range(len(numbers), target):
        n.insert_at_end(x + 1)

    current = n.first

    for _ in range(moves):

        # picking up 3 clockwise of current
        r = deque()
        for _ in range(3):
            r.append(n.remove(current.next))

        # calculate destination
        destinationLabel = current.data - 1
        while destinationLabel in r or destinationLabel < 1:
            destinationLabel = destinationLabel - 1
            if destinationLabel < 1:
                destinationLabel = target
        dest = n.find_node(destinationLabel)

        # add cups after destination
        while r:
            n.insert_after(dest, r.pop())

        current = current.next

    res = []
    c = n.find_node(1)
    for x in range(8):
        res.append(str(c.next.data))
        c = c.next
    print('part 1:', "".join(res))

    one = n.find_node(1)
    print('part 2:', one.next.data * one.next.next.data)


# day23('389125467', 100, 9)
# day23('389125467', 10000000, 1000000)

day23('538914762', 100, 9)
day23('538914762', 10000000, 1000000)
