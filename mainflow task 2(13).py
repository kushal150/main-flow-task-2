def bubble_sort(lst):
    n = len(lst)
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to detect if any swapping happens
        swapped = False
        # Last i elements are already sorted, so no need to check them
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the current element is greater than the next element
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break
    return lst

# Example usage:
input_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", input_list)
sorted_list = bubble_sort(input_list)
print("Sorted list:", sorted_list)