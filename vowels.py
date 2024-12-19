n = input('input string: ') # Gets string from user

# Part 1: Prints String
print(n) 

# Part 2: Counts Vowels

# First, i make a list containing the vowel characters
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0 # initialize count

# Itterate over the characters:
for character in n:
    # Itterate over the vowels list
    for vowel in vowels:
        # Compare current character with every vowel in the list
        if character == vowel:
            # Increase count if vowel is found
            count += 1
print(f'--> {count} Vowels')

# Part 3: Reverse It

# Create reversed empty string
reversed = ''
# Itterate over n
for character in n:
    # append a character to the reversed string
    # this will make a 'linked list' type of effect
    # where on each itteration, the previous character is pushed back
    reversed = character + reversed
print(f'--> Reversed: {reversed}')

