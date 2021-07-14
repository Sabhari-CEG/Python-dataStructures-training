def BubbleSort(item_list):
    for i in range(len(item_list) - 1):
        for j in range(len(item_list) - 1):
            if item_list[j] > item_list[j+1]:
                item_list[j],item_list[j+1] = item_list[j+1],item_list[j]

    return item_list


if __name__ == '__main__':
    item_list = [9,1,5,2,3,7,4,8,6]
    result = BubbleSort(item_list)
    print(result)