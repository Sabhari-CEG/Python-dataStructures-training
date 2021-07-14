def BinarySearchItterative(list_item,search_item):
    first_index = 0
    last_index = len(list_item) - 1
    while first_index <= last_index:
        midpoint = (first_index + last_index) // 2
        if list_item[midpoint] == search_item:
            return  midpoint
        elif list_item[midpoint] > search_item:
            last_index = midpoint - 1
        elif last_index[midpoint] < search_item:
            first_index = midpoint + 1
    return None

def BinarySearchRecursive(list_item,search_item,first_index ,last_index ):
    #print(list_item)

    if last_index < first_index:
        print('entered')
        print(first_index,last_index)
        return None
    else:
        midpoint = first_index + ((last_index - first_index)//2)
        #print(midpoint)

        if list_item[midpoint] == search_item:
            print("Found at index",midpoint)
            return midpoint

        if list_item[midpoint] > search_item:
            #print("calling midpoint is greater")
            return BinarySearchRecursive(list_item,search_item,first_index,midpoint-1)
        elif list_item[midpoint] < search_item:
            return BinarySearchRecursive(list_item,search_item,midpoint+1,last_index)


if __name__ == '__main__':
    list_item = [2,4,5,12,43,54,60,77]
    print(BinarySearchItterative(list_item,4))
    ind= BinarySearchRecursive(list_item,4,0,len(list_item)-1)
    print(ind)
