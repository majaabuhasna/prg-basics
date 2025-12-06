def bubblesort(array):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]

    return array

print(bubblesort([3,6,1,5,9]))
print(bubblesort([9,6,5,7,7,1,3]))
print(bubblesort([1,5,2,9,0,4]))