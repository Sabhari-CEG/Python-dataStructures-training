def nearest_mid(list_item,search_item,first_index,last_index):
    last = list_item[last_index]
    first = list_item[first_index]
    x = int(first_index + ((last_index - first_index)/(last - first)) * (search_item - first))
    #print(x)
    return x

def BinarySearchItterative(list_item,search_item):
    first_index = 0
    last_index = len(list_item) - 1
    while first_index <= last_index:
        midpoint = nearest_mid(list_item,search_item,first_index,last_index)
        if midpoint > last_index or midpoint < first_index:
            return None
        mid = list_item[midpoint]
        if mid == search_item:
            return  midpoint
        elif mid > search_item:
            last_index = midpoint - 1
        elif mid < search_item:
            first_index = midpoint + 1
    return None


if __name__ == '__main__':
    list_item = [2,4,5,12,43,54,60,77]
    print("The given element is at\n",BinarySearchItterative(list_item,4))
    print(BinarySearchItterative(list_item,500))

