def SelectionSort(item_list):
    for i in range(len(item_list)):
        for j in range(i+1,len(item_list)):
            if item_list[j] < item_list[i]:
                item_list[i],item_list[j] = item_list[j],item_list[i]
    return item_list

if __name__ == '__main__':
    item_list = [9, 1, 5, 2, 3, 7, 4, 8, 6]
    result = SelectionSort(item_list)
    print(result)