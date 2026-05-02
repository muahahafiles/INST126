# Muatasim Miller
# Word Count Program (Part 1)
# Steps:
# 1. Show directory info
# 2. Get user input
# 3. Read file
# 4. Count word
# 5. Display and save results

import os


# show current working directory so users can find files 
current_directory = os.getcwd()
print("Current directory:")
print(current_directory)


# show contents of current directory
directory_contents = os.listdir()
print("Contents:")
print(directory_contents)


# ask a user for file path
file_name = input("Enter the file path:")


# ask a user for word to count 
counting_word = input("Enter the word you'd like to count: ")


# open the file and read all text
with open(file_name, mode="r") as file_object:
    file_text = file_object.read()


# count how many times the word appears
word_count = file_text.count(counting_word)


# create a result message
msg_result ="The word " + counting_word + " is counted " + str(word_count) + " times in the file: " + file_name


# print the result to the terminal
print(msg_result)


# write the result to an output file
with open("wordcount_results.txt", mode="w") as output_file: 
    output_file.write(msg_result)