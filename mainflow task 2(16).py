def count_vowels_consonants(input_string):
    vowels = set('aeiouAEIOU')  # Set of vowels (both lowercase and uppercase)
    vowels_count = 0
    consonants_count = 0
    
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    
    return vowels_count, consonants_count

# Example usage
input_string = "Hello, World!"
vowels, consonants = count_vowels_consonants(input_string)
print("Vowels:", vowels)
print("Consonants:", consonants)
