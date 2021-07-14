class HashItem():
    def __init__(self,key,value):
        self.key = key
        self.value = value

class HashTable():
    def __init__(self):
        self.size = 256
        self.count = 0
        self.slots = [None for i in range(self.size)]

    def _hash(self,key):
        multi = 1
        hash_value = 0
        for character in key:
            hash_value += multi * ord(character)
            multi += 1
        return hash_value % self.size

    def put(self,key,value):
        item = HashItem(key,value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item

    def get(self,key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h = (h + 1) % self.size
        return None

if __name__ == '__main__':
    ht = HashTable()
    ht.put('one',1)
    ht.put('two',2)
    ht.put('three',3)
    ht.put('ad','no conflict')
    ht.put('ga','no conflict here also')

    for key in ('one','two','three','ad','ga','invalid'):
        print(ht.get(key))

