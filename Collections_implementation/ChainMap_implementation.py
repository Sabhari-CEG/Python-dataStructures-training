#The advantage of using ChainMaps, rather than just a dictionary, is that we retain previously set values.
# Adding a child context overrides values for the same key, but it does not remove it from the data structure.
# This can be useful for when we may need to keep a record of changes so that we can easily roll back to a previous setting.
from collections import ChainMap

if __name__ == '__main__':
    d = {'theme':'Default','language':'eng','showIndex':True}
    print("The given dictionary\n",d)
    #creating the chain map from dictionary
    cm = ChainMap(d)
    print("The chain map formed is\n",cm)
    #using child property to override the chain map
    cm2 = cm.new_child({'theme':'dark'})
    print("The new chain map is\n",cm2)
    #the first dictionary is given higher priority
    print("Theme info\n",cm2['theme'])
    #now we delete the dictionary and rollback to last value
    popped = cm2.pop('theme')
    print("popped elem is",popped,"\n",cm2)
    print("now lets look at theme\n",cm2['theme'])
    #we can update chain map at the begining index
    cm2.maps[0] = {'showIndex':False}
    print(cm2)
    print(cm2['showIndex'])
    print("To view the parent\n",cm2.parents)
