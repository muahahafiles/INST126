import os 
from word_tools import count_word

# show current working directory 
current_dir = os.getcwd()
print("Current directory:")
print(current_dir)

# show current directory contents
contents_dir = os.listdir()
print("Contents:")
print(contents_dir)

# get search path from user
search_path = input("Enter the file or directory path: ")


# ask user for word to count
counter_word = input("Enter the word you'd like to count: ")
og_counter_word = counter_word

# ask user case sensitivity preferences 
sens_pref = input("Would you like to enable case-sensitive counting? (y/n): ")

# repeat until user enters a valid file or directory 
valid_path = False 

while valid_path == False:
    if os.path.isfile(search_path):
        valid_path = True 
    elif os.path.isdir(search_path):
        valid_path = True
    else: 
        print("Path not found. Try again.")
        search_path = input("Enter the file or directory path: ")
    
    
# list to store the result messages   
msg_results = []

# if path is a file, search only that file 
if os.path.isfile(search_path):
    with open(search_path, mode="r") as file_obj: 
        file_txt = file_obj.read()
    
    if sens_pref == "y":
        print("Case sensiive counting is active.")
    elif sens_pref != "n":
        print("Invalid option. Case sensitive counting is active.")
        
    word_count = count_word(file_txt, counter_word, sens_pref)
    
    msg_result = "The word " + og_counter_word + " was found " + str(word_count) + " times in this file: " + search_path
    print(msg_result)
    
    msg_results.append(msg_result)
    
    
# if path is directory, search every file in the directory
elif  os.path.isdir(search_path):
    file_list = os.listdir(search_path)
    
    if sens_pref == "y":
        print("Case-sensitive counting active.")
    elif sens_pref != "n":
        print("Invalid option. Case-sensitive counting active.")
    
    # loop through each file in the directory
    for file_name in file_list: 
        file_path = search_path + "/" + file_name 
        
        # only process if item is a file
        if os.path.isfile(file_path):
            with open(file_path, mode="r") as file_obj:
                file_txt = file_obj.read()
                
            word_count = count_word(file_txt, counter_word, sens_pref)
                
            
             # create and print result message
            msg_result ="The word " + og_counter_word + " was found " + str(word_count) + " times in this file: " + file_name
            print(msg_result)
            
            # store result message in list
            msg_results.append(msg_result)
            
            
# add all results to the results file
with open("wordcount_results.txt", mode="w") as output_file: 
    for message in msg_results:
        output_file.write(message + "\n")

    