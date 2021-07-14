#The defaultdict overrides one method, __missing__(key),
# and creates a new instance variable, default_factory.
from collections import defaultdict
if __name__ == '__main__':
    dd = defaultdict(int)
    words = str.split('red blue green red yellow blue red green green red')
    print("the given words are\n",words)
    #the int returns a default 0 for missing keys
    for word in words:
        dd[word] += 1

    print("the first dictionary\n",dd)

    #we can also use functions to initialise the values

    def isPrimary(c):
        if c == 'red' or c == 'blue' or c == 'green':
            return True
        return False

    dd1 = defaultdict(bool)
    for word in words:
        dd1[word] = isPrimary(word)

    print("the colour is primary or not\n",dd1)