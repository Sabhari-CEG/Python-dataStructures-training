#This involves breaking the problem into smaller sub problems, recursively solving them, and then somehow combining the results.

def MergeSort(A):
    #first we check whether it is a larger or smaller problem.
    #if it is large problem split it to smaller problem
    if len(A) > 1:
        print("Larger problem. splitting happens here\n",A)
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        print("The splitted left and right are\n",left,right)
        MergeSort(left)
        MergeSort(right)

        #initialise 3 variables to hold the reference of left,right and original list
        i = j = k = 0

        #check whether both left and right has elements to be compared
        while i < len(left) and j < len(right):
            #if elements are present and left is small
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            #if right is small
            else:
                A[k] = right[j]
                j += 1
            k+=1

        #for left out values in left or right splits
        while i < len(left):
            A[k] = left[i]
            i +=1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

        print("merging \n",A)
        return A


if __name__ == '__main__':
    l = list()
    while True:
        print("Enter numbers and '-1' to quit")
        no = int(input())
        if no == -1:
            break
        l.append(no)
    print("The final result is\n",MergeSort(l))