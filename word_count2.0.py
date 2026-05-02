# Muatasim Miller
# Word Count Program (Part 2)

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
file_name = input("Enter the file path: ")


# ask a user for word to count 
counting_word = input("Enter the word you'd like to count: ")


# ask user if the count should be case-sensitive
sensitivity_choice = input("Do you want to enable case-sensitive counting?: yes/no ")


# try to open and read the file
# if the file path is wrong, give the user one more chance
try:
    with open(file_name, mode ="r") as file_object:
        file_text = file_object.read()
except:
    print("That file wasn't found. Try again.")

    file_name = input("Enter the file path again: ")

    with open(file_name, mode="r") as file_object:
        file_text = file_object.read()

# change text to lowercase if the user does not want case-sensitive counting
if sensitivity_choice == "no":
    file_text = file_text.lower()
    counting_word = counting_word.lower()
elif sensitivity_choice == "yes": 
    print("Case-sensitive counting selected.")
else:
    print("Invalid choice. Case-sensitive counting will be used.")


# count how many times the word appears
word_count = file_text.count(counting_word)


# create and print the result message
msg_result = "The word " + counting_word + " was counted " + str(word_count) + " times in the file: " + file_name
print(msg_result)

# write the result message to an output file
with open("wordcount_results.txt", mode="w") as output_file:
    output_file.write(msg_result)
    
    
        
