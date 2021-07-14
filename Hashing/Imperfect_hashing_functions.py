
def impHash(word):
    return sum(map(ord,word))

def modifiedHash(word):
    mult = 1
    hash_value = 0
    for character in word:
        hash_value += mult * ord(character)
        mult += 1
    return hash_value
if __name__ == '__main__':
    words = ['hello world','world hello','gello xorld']

    for word in words:
        print(word)
        print('hash value\t',impHash(word))

    print('alternate hash function')
    for word in words:
        print(word)
        print('hash value\t',modifiedHash(word))

    print('but its not perfect')
    print('hash value for ad\t',modifiedHash('ad'))
    print('hash value for ga\t',modifiedHash('ga'))
