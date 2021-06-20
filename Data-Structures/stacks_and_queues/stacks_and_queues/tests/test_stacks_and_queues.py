from inspect import stack
from stacks_and_queues import __version__
from stacks_and_queues.stacks_and_queues import Stack, Queue
import pytest


def test_version():
    assert __version__ == '0.1.0'


# Can successfully push onto a stack

def test_push(stack_4_vals):  # 1
    actual = stack_4_vals.peek()
    expected = 'r'
    assert actual == expected

# Can successfully push multiple values onto a stack


def test_multiple_push(stack_4_vals):  # 2
    stack_4_vals.push('w')
    actual = stack_4_vals.peek()
    expected = 'w'
    assert actual == expected

# Can successfully pop off the stack


def test_pop(stack_4_vals):  # 3
    stack_4_vals.pop()
    actual = stack_4_vals.peek()
    expected = 'd'
    assert actual == expected

# Can successfully empty a stack after multiple pops


def test_multiple_pop(stack_4_vals):  # 4
    stack_4_vals.pop()
    stack_4_vals.pop()
    stack_4_vals.pop()
    actual = stack_4_vals.pop()
    expected = 3
    assert actual == expected

# Can successfully peek the next item on the stack


def test_peek_next_item(stack_4_vals):  # 5
    actual = stack_4_vals.peek()
    expected = 'r'
    assert actual == expected

# Can successfully instantiate an empty stack


def test_is_empty_stack():  # 6
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

# Calling pop or peek on empty stack raises exception


def test_pop_raise_empty():  # 7
    stack = Stack()
    actual = stack.pop()
    expected = 'empty stack'
    assert actual == expected


# Can successfully enqueue into a queue

def test_enqueue(queue_vals):  # 8
    assert queue_vals.rear.value == 6
    assert queue_vals.front.value == 8

# Can successfully enqueue multiple values into a queue


def test_multiple_enqueue(queue_vals):  # 9
    queue_vals.enqueue('well')
    assert queue_vals.rear.value == 'well'
    assert queue_vals.front.value == 8

# Can successfully dequeue out of a queue the expected value


def test_dequeue(queue_vals):  # 10
    actual = queue_vals.dequeue()
    expected = 8
    assert actual == expected

# Can successfully peek into a queue, seeing the expected value


def test_queue_peek(queue_vals):  # 11
    actual = queue_vals.peek()
    expected = 8
    assert actual == expected

# Can successfully empty a queue after multiple dequeues


def test_multiple_dequeues(queue_vals):  # 12
    queue_vals.dequeue()
    queue_vals.dequeue()
    actual = queue_vals.dequeue()
    expected = -4
    assert actual == expected


# Can successfully instantiate an empty queue

def test_is_empty_queue():  # 13
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

# Calling dequeue or peek on empty queue raises exception


def test_dequeue_raise_empty():  # #14
    queue = Queue()
    actual = queue.dequeue()
    expected = 'empty queue'
    assert actual == expected


@pytest.fixture
def stack_4_vals():
    stack = Stack()
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    stack.push('r')
    return stack


@pytest.fixture
def queue_vals():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    return queue
