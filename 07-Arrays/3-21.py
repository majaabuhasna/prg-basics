arr1 = [1,3,5,7,2,3,9]
arr2 = [1,5,3]
arr3 = [4,4,8]

def subset_array(array1,array2):
    flag = 0

    for digit in array2:
        if digit not in array1:
            flag += 1

    if flag > 0:
        return False
    return True

print(subset_array(arr1,arr2))
print(subset_array(arr1,arr3))