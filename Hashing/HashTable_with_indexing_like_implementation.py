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
        #print("put called")
        item = HashItem(key,value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
        #print('hash is\t',h)
        #print('assigned\t',self.slots[h].value)

    def get(self,key):
        #print("get called")

        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                #print('getting hash is\t', h)
                #print('will return\t',self.slots[h].value)
                return self.slots[h].value
            h = (h + 1) % self.size
        return None

    def __setitem__(self, key, value):
        self.put(key,value)

    def __getitem__(self, item):
        res = self.get(item)
        return res

if __name__ == '__main__':
    ht = HashTable()
    ht['one'] = 1
    ht['two'] = 2
    ht['three'] = 3
    ht['ad'] = 'no conflict'
    ht['ga'] = 'no conflict here'

    for key in ('one','two','three','ad','ga','invalid'):
        ans = ht[key]
        print(ans)

    print("size is\t",ht.count)


