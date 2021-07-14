#Counter is a subclass of a dictionary,
# where each dictionary key is a hashable object and the associated value is an integer count of that object.
from collections import Counter
if __name__ == '__main__':
    c1 = Counter('sequence')
    print("sequence to counter\n",c1)
    c2 = Counter({'a':3,'B':1})
    print("Dictionary to counter\n",c2)
    c3 = Counter(a=1,b=3,c=5)
    print("Tuple to counter\n",c3)
    #we can create a empty instance of counter object
    ct = Counter()
    print("Empty counter\t",ct)
    ct.update('abcdaybc')
    print("sequence added\n",ct)
    #update adds the count instead of changing its value
    ct.update({'a':3})
    print("After updating a as 3\n",ct)
    #the item not in the dictionary is assigned 0
    print("The 'z' is not in dictionary and its value is\t",ct['z'])

    #elements() returns an iterable
    print(sorted(ct.elements()))
    print("Most common\n",ct.most_common())
    ct.subtract({'a': 1})
    print("subtract\n",ct)