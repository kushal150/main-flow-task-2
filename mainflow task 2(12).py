def reverse_list(lst):
    # Initialize pointers
    left = 0
    right = len(lst) - 1
    
    # Swap elements until pointers meet
    while left < right:
        # Swap elements at left and right pointers
        lst[left], lst[right] = lst[right], lst[left]
        # Move pointers
        left += 1
        right -= 1
    
    return lst

# Example usage:
input_list = [1, 2, 3, 4, 5]
print("Original list:", input_list)
reversed_list = reverse_list(input_list)
print("Reversed list:", reversed_list)