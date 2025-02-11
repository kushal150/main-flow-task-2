def string_length(input_string):
    count = 0
    for char in input_string:
        count += 1
    return count

# Example usage
input_string = "Hello, World!"
result = string_length(input_string)
print(result)
