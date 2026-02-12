def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr) // 2
    pivot_value = arr[pivot_index]

    smaller_elements = []
    equal_elements = []
    larger_elements = []

    for element in arr:
        if element < pivot_value:
            smaller_elements.append(element)
        elif element == pivot_value:
            equal_elements.append(element)
        else:
            larger_elements.append(element)

    sorted_left_side = quick_sort(smaller_elements)
    sorted_right_side = quick_sort(larger_elements)

    full_sorted_list = sorted_left_side + equal_elements + sorted_right_side
    
    return full_sorted_list

test_array = [82, 45, 12, 9, 104, 27, 45, 1, 63]
result = quick_sort(test_array)
print(result)