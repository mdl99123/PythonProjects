def bubbleSort(array):
     
    n = len(array)
    #outer for is to push the wall forwards, all swaps are done by the inner for
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
                    
def insertion_sort(array): 
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key
    return array
             
                 
def selection_sort(array):
    # Traverse through all array elements
    for i in range(len(array)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        array[i], array[min_idx] = array[min_idx], array[i]
    # Return the sorted array
    return array


def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = []
    right = []
    middle = []
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            middle.append(item)
    return quicksort(left) + middle + quicksort(right)


def mergesort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

option="-1"

while(option!="6"):
    print("------------Main Menu------------")
    print("1.- Bubble Sort")
    print("2.- Selection Sort")
    print("3.- Insertion Sort")
    print("4.- Merge Sort")
    print("5.- Quicksort")
    print("6.- Exit")
    option=input()
    if(int(option)<=1 or int(option)<=5):
        arr = [ 2, 1, 10, 23 ]
        print("The unsorted list is:", arr) 
        size=len(arr)
        if(option=="1"):
            bubbleSort(arr)
            print("Sorted array is:")
            print(arr)
        elif(option=="2"):
            selection_sort(arr)
            print('Sorted Array in Ascending Order is :')
            print(arr)
        elif(option=="3"): 
            insertion_sort(arr)
            print("The sorted new list is:" )
            print(arr)
        elif(option=="4"):
            mergesort(arr)
            print("\n\nSorted array is")
            for i in range(size):
             print("%d" % arr[i],end=" ")
            print(" ")
        elif(option=="5"):
            quicksort(arr)
            print('Sorted Array in Ascending Order:')
            print(arr)