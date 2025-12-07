import MyArrays

arr = [7,3,8,5,2]

print('Numbers: ',end='')
print(*arr, sep=',')

print('Second largest number:',MyArrays.second_largest_number(arr))

print('Median:',MyArrays.median_of_numbers(arr))

print('Smallest and largest number:',MyArrays.two_element_array(arr))

print('Numbers as a string:',MyArrays.array_string(arr))