#their contents must be of a single type of the underlying representation,
# as is determined by the machine architecture or underlying C implementation
import array as arr
if __name__ == '__main__':
    a = arr.array('i', [])
    print(a)
    a.append(5)
    print("After appending \t", a)
    a.insert(0, 4)
    print("After inserting \t", a)
    a.append(6)
    a.append(7)
    a.append(8)
    a.append(7)
    print("After modifications \t", a)
    print("Pop removes element at index, we pop at index 1 \t", a.pop(1))
    print(a)
    print("remove deletes the first occurance, removing the element 7 \t", a.remove(7))
    print(a)
    a.append(9)
    a.append(10)
    print("After modifications \t", a)
    print("searching index of 8 \t", a.index(8))

    print("size comparision of array and list")
    my_array = arr.array('i',range(10**6))
    my_list = list(range(10**6))
    import sys
    print( sys.getsizeof(my_list) / sys.getsizeof(my_array))
    print("list takes about the 2 times the sace of array")
