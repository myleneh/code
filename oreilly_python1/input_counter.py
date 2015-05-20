#!/usr/local/bin/python3

# Create an empty set and dict.
words = set()
words_value = {}
text = " "

while text != "":
# If the user presses Enter without any text, print "Finished" and exit.
    text = input("Enter text: ")
    if text == "":
        print("Finished")
        break

# While loop that repeatedly creates a list of words from a line of input from the user.
# Loop through the list of words and add each one to the set.  
# If the set increases in size (the word has not been processed before),
# add the word to the dict as a key with the value being the new length of the set.
    else:
        text_split = text.lower().split()
        for word in text_split:
            original_num = len(words)
            words.add(word)
            if len(words) > original_num:
                words_value[word] = len(words)

# Using another loop, display the words in the dict along with their value, which represents the order in which they were discovered by the program.
        for word2 in words_value:
            print(word2, words_value[word2])