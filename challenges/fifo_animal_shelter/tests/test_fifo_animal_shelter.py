from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import Queue, Node, AnimalShelter


def test_version():
    assert __version__ == '0.1.0'


def test_enqueue():
    actual = []
    animal = AnimalShelter()
    animal.enqueue('bobi', 'dog')
    actual += [animal.dog.peek()]
    animal.enqueue('lara', 'cat')
    actual += [animal.cat.peek()]
    excepted = ['bobi', 'lara']
    assert actual == excepted


def test_enqueue_fail():
    animal = AnimalShelter()
    actual = animal.enqueue('fast', 'horse')
    excepted = 'you can just choose dog or cat'
    assert actual == excepted


def test_dequeue():
    animal = AnimalShelter()
    animal.enqueue('bobi', 'dog')
    animal.enqueue('lara', 'cat')
    actual = [animal.dequeue('dog'), animal.dequeue('cat')]
    excepted = ['bobi', 'lara']
    assert actual == excepted


def test_dequeue_fail():
    animal = AnimalShelter()
    actual = animal.dequeue('horse')
    excepted = 'you can just choose dog or cat'
    assert actual == excepted
