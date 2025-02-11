def sum_of_digits(n):

    num_str = str(n)
    
    total = 0
    
    
    for char in num_str:
        
        total += int(char)
    
    return total

n = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(n))