class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,):
        self.top = None

    def push(self, item):

        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            return 'empty stack'
        else:
            pop_item = self.top
            self.top = self.top.next
        return pop_item.value

    def is_empty(self):
        return self.top == None

    def __str__(self):

        strr = ''
        current = self.top
        while current is not None:
            if current.next is None:
                strr = strr + f'[{current.value}]'
                current = current.next
            else:
                strr = strr + f'[{current.value}]->'
                current = current.next

        return strr


class PseudoQueue:
    def __init__(self):
        self.stack = Stack()
        self.second_stack = Stack()
        self.count = 0

    def enqueue(self, value):
        self.stack.push(value)
        return f'[{value}]'

    def dequeue(self):
        new_stack = Stack()

        while self.stack.top:  # revers the stack ..
            new_stack.push(self.stack.pop())

        removed_item = new_stack.pop()  # remove the Top

        while new_stack.top:
            self.enqueue(new_stack.pop())

        return removed_item


if __name__ == "__main__":
    stack = Stack()
    stack.push(7)
    stack.push(6)
    stack.push('g')
    stack.push('q')
    pss = PseudoQueue()
    pss.stack = stack
    pss.enqueue('u')
    pss.enqueue('t')
    pss.enqueue('  ^___^')
    # print(pss.enqueue(5))
    # print(stack)
    pss.dequeue()
    pss.dequeue()
    pss.dequeue()
    pss.dequeue()
    print(stack)
