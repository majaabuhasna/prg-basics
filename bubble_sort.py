def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

    return array
        

arr = [2,5,1,4,8,9,2,4,0,6,3]

print(bubble_sort(arr))