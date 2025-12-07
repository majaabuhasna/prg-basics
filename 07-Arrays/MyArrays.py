def second_largest_number(array):
    array = set(array)

    largest = float('-inf')
    second_largest_number = float('-inf')

    for digit in array:
        if digit > largest:
            second_largest_number = largest
            largest = digit
        elif digit > second_largest_number and digit != largest:
            second_largest_number = digit

    return second_largest_number

def difference_smallest_largest(array):
    largest = float('-inf')
    smallest = float('inf')

    for digit in array:
        if digit > largest:
            largest = digit

        if digit < smallest:
            smallest = digit

    difference = largest - smallest
    return difference

def median_of_numbers(array):
    array = sorted(array)
    median = 0

    n = len(array)

    if n % 2 != 0:
        median = array[(n - 1)//2]

    else:
        first = array[n//2 - 1]
        second = array[n//2]
        median = ( first + second) / 2

    return median

def two_element_array(array):
    new_array = []

    new_array.append(min(array))
    new_array.append(max(array))

    return new_array

def array_string(array):
    
    str_array = [str(i) for i in array]
    string = '-'.join(str_array)

    return string