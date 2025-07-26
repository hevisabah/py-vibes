def merge_sort(array):
    if len(array) <= 1:
        return # it will return the sorted array 
    
    middle_point = len(array) // 2 # it will divide the array into two halves
    left_part = array[:middle_point] # it will take left half of the array as the first half
    right_part = array[middle_point:] # it will take right half of the array as the second half

    merge_sort(left_part) # it will call the merge_sort function on the left half of the array
    merge_sort(right_part) #this one will call the right half of the array

    # it will merge the two halves of the array
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part): # it will check if both the halves are not empty
        if left_part[left_array_index] < right_part[right_array_index]: 
            array[sorted_index] = left_part[left_array_index] # it will add the left half of the array to the sorted array
            left_array_index += 1 # it will increase the left half of the array index
        else:
            array[sorted_index] = right_part[right_array_index] # it will add the right half of the array to the sorted array
            right_array_index += 1 # it will increase the right half of the array index
        sorted_index += 1 # it will increase the sorted array index

    # it will add the remaining elements of the left half of the array to the sorted array
    while left_array_index < len(left_part): # it will add the left half of the array to the sorted array
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # it will add the remaining elements of the right half of the array to the sorted array
    while right_array_index < len(right_part): # it will add the right half of the array to the sorted array
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

# it will call the merge_sort function on the array
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array:') 
    print(numbers) # it will print the unsorted array
    merge_sort(numbers) # it will call the merge_sort function on the array
    print('Sorted array: ' + str(numbers)) # it will print the sorted array 🔥
    
