def partition(unsorted_array,first_index,last_index):
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index

    greater_than_pivot_index = first_index + 1
    less_than_pivot_index = index_of_last_element

    while True:
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1

        if greater_than_pivot_index < less_than_pivot_index:
            unsorted_array[greater_than_pivot_index],unsorted_array[less_than_pivot_index] = unsorted_array[less_than_pivot_index],unsorted_array[greater_than_pivot_index]
        else:
            break
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot
    print('intermediate\t',unsorted_array)
    return less_than_pivot_index

def QuickSort(unsorted_array,first,last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted_array,first,last)
        QuickSort(unsorted_array,first,partition_point-1)
        QuickSort(unsorted_array,partition_point+1,last)
    return unsorted_array


if __name__ == '__main__':
    item_list = [43,3,20,89,4,77]
    print(QuickSort(item_list,0,5))


