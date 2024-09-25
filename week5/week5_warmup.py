# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',

# a. Retrieve the 5th character.

my_text1 = "abracadabra"
print (my_text1.find("abracadabra"))
print (my_text1 [5])


# b. Retrieve the second to last character.
my_text2 = "abracadabra"
(my_text2.find("abracadabra"))
print(my_text2[-2])

# c. Find the first occurrence of the letter 'c'.

my_text3 = "abracadabra"
print(my_text3.find("abracadabra"))
print(my_text3[4])



# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',

# a. Extract the letters 'hij'.

my_text4 = "abcdefghijklmnopqrstuvwxyz"
print (my_text4.find("abcdefghijklmnopqrstuvwxyz"))
print (my_text4[7:10])

# b. Extract every second letter starting from 'a' to 'm'.

my_text5 = 'abcdefghijklmnopqrstuvwxyz'
my_text6 = (my_text5[0:13])
print(my_text6[::2])

# c. Reverse the entire string using slicing.
my_text7 = "abcdefghijklmnopqrstuvwxyz"
my_text8 = (my_text7[::-1])
print(my_text8)

# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

my_text9 = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy "
my_text10 = (my_text9[-16:-1])
print(my_text10)

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.

my_text11 = "Python is fun. Fun is good. Good is subjective."
my_text12 = (my_text11[-11:-1])
print(my_text12)

# b. Extract every third word.

my_text13 = "Python is fun. Fun is good. Good is subjective."
my_text14 = (my_text13[::2])
print(my_text14)

# c. Reverse the positions of the words, but keep the characters in each word in the same order.

my_text15 = "Python is fun. Fun is good. Good is subjective."
my_text16 = (my_text15[::-1])
print(my_text16)

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."

star_wars = "MAY THE FORCE BE WITH YOU."
star_wars2 = str.lower("MAY THE FORCE BE WITH YOU.")
print(star_wars2)

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.

a = "Make"
b = "haste"
c = "slowly"
d = " ".join([a, b, c])
print(d)

# b. Now, split the string at every occurrence of the letter 'a'.



# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".

new_text = "Life is what happens when you are busy making other plans."
my_text20 = (new_text.replace("busy", "plans"))
print("Life is what happens when you are distracted making mistakes")

# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

Concatenation = "Iteration" * 5
print(Concatenation)

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".


# b. Count the number of times the letter 'i' appears in the same word/phrase.

