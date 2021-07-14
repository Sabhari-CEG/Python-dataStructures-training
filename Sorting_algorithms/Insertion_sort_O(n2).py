def InsertionSort(item_list):
    for index in range(1,len(item_list)):
        search_index = index
        insertion_value = item_list[index]

        while (search_index > 0) and (item_list[search_index - 1] > insertion_value):
            item_list[search_index] = item_list[search_index - 1]
            search_index -= 1
        item_list[search_index] = insertion_value
    return item_list

if __name__ == '__main__':
    item_list = [9, 1, 5, 2, 3, 7, 4, 8, 6]
    result = InsertionSort(item_list)
    print(result)