from linked_list.linked_list import LinkedList
import sys
sys.path.append(
    "/home/ayman/course401/data-structures-and-algorithms/Data-Structures/linked-list")


class Hashtable:
    def __init__(self):
        self.buckets = [None] * 1024

    def hash(self, key):
        prime_value = 599
        hashed_key = sum([ord(char) for char in key]) * prime_value
        hashed_key = hashed_key % 1024

        return hashed_key

    def add(self, key, value):
        index = self.hash(key)
        if self.buckets[index] == None:
            bucket = LinkedList()
        else:
            bucket = self.buckets[index]

        bucket.append(
            {
                'key': key,
                'value': value,
            }
        )

        self.buckets[index] = bucket

    def get(self, key):
        idx = self.hash(key)

        bucket = self.buckets[idx]
        if bucket == None:
            raise KeyError('Key not in hash table')
        current = bucket.head
        while current:
            if current.value['key'] == key:
                return current.value['value']
            current = current.next

        raise KeyError('Key not in hash table')

    def contains(self, key):
        idx = self.hash(key)
        bucket = self.buckets[idx]
        if bucket == None:
            return None
        current = bucket.head
        while current:
            if current.value['key'] == key:
                return True
            current = current.next

        return None
