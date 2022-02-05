class Node:  # a node always has 2 parts: value and next
    def __init__(self, value):  # that is why it's initialized here
        self.value = value  # value is it's value
        self.next = None  # next is None - for now


class Stack:
    def __init__(self):  # we want the stack to start at the head
        self.head = None  # so we instantiate it with attribute head
        self.num_nodes = 0

    def push(self, value):  # we create the push method for the stack
        # we create a variable of new_node and assign it the value of Node's class attribute
        new_node = Node(value)

        if self.head is not None:  # if there is an existing head:
            # new_node.next (the next node) is the (new) head
            new_node.next = self.head

        self.head = new_node  # otherwise, the new node is head
        self.num_nodes += 1  # we increase the count

    def pop(self):
        if self.head == None:
            return None  # if there is no node to pop off, then this is null

        pop_node = self.head.value  # otherwise pop_node is the new value of head
        # head is the next head inline (last in, first out)
        self.head = self.head.next
        self.num_nodes -= 1  # decrement 1 from the count
        return pop_node  # return the new value of head


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.num_nodes == 5) else "Fail")
stack.push(5)
print("Pass" if (stack.num_nodes == 5) else "Fail")

print("Pass" if (stack.pop() == 5) else "Fail")
print("Pass" if (stack.pop() == 4) else "Fail")
