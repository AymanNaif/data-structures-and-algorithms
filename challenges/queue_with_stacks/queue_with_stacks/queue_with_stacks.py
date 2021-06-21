from ..assets.stacks_and_queues import Stack, Node

# assets/stacks_and_queues.py


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
    pss.enqueue('^___^')
    # print(pss.enqueue(5))
    # print(stack)
    pss.dequeue()
    pss.dequeue()
    pss.dequeue()
    pss.dequeue()
    print(stack)
