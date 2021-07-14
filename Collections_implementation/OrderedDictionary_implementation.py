#The important thing about ordered dictionaries is that they remember the insertion order,
# so when we iterate over them,
# they return values in the order they were inserted
from collections import OrderedDict
if __name__ == '__main__':
    od = OrderedDict()
    od['one'] = 1
    od['two'] = 2
    print("look at the order of the dictionary\n",od)
    #create other dictinary with same elements but with different order
    od1 = OrderedDict()
    od1['two'] = 2
    od1['one'] = 1
    print("new dictionary\n",od1)
    print("check whether they are equal\n",od==od1)
    l = [('three',3),('four',4),('five',5)]
    od.update(l)
    print("The order in which the list is added is preserved\n",od)