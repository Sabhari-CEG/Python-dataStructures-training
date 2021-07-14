import time
def LinearUnorderedSearch(list_item,search_item):
    for i in range(len(list_item)):
        if search_item == list_item[i]:
            return i
    return None

def LinearOrderedSearch(list_item,search_item):
    for i in range(len(list_item)):
        if search_item == list_item[i]:
            return i
        elif search_item < list_item[i]:
            return  None
    return None

if __name__ == '__main__':
    list_item = [60,1,88,10,11,100]
    t1 = time.time()
    print("Find 11\n",LinearUnorderedSearch(list_item,11))
    print('time is\t',time.time()-t1)

    list_item.sort()
    t1 = time.time()
    print("Find 11\n", LinearOrderedSearch(list_item, 11))
    print('time is\t', time.time() - t1)
