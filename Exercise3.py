# counts the input string
def count(input_string):
    
    letter_count = {}
    
# goes through ecach character from the input
    for char in input_string:
        if char.islower():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    
    return letter_count

user_input = input("Enter a string: ")
# call the count functiuon
result = count(user_input)
print(result)
