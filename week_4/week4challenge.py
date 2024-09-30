#################################Extracting Sub-Strings###################################
# Extracting Sub-Strings Practice #1
# Extract the first word of the following sentence using slicing, and display it on the screen:
# Hint: "Controlling" is 11 characters long.

my_text = 'Controlling complexity is the essence of programming'
result = my_text 
print(result.find('Controlling'))
print(result[0:11])

# Extracting Sub-Strings Practice #2
# Take every third character starting from the ninth to the end of the sentence, and print the result.
# "Never trust a computer you can't throw out a window"


text = "Never trust a computer you can't throw out a window"
result = text
print(text[9::3])

# Extracting Sub-Strings Practice #3
# Reverses the position of all the characters in the following sentence and displays the result on the screen.
# "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"

text = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
result = text
print(text[::-1])