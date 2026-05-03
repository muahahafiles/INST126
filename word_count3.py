import os 


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
sensitivity_pref = input("Would you like to enable case-sensitive counting? (y/n): ")

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
    
    
    
msg_results = []

# if path is a file, search only that file 
if os.path.isfile(search_path):
    with open(search_path, mode="r") as file_obj: 
        file_txt = file_obj.read()
        
    if sensitivity_pref == "n":
        file_txt = file_txt.lower()
        search_word = counter_word.lower()
    elif sensitivity_pref == "y":
        print("Case-sensitive counting active.")
        search_word = counter_word
    else:
        print("Invalid option. Case-sensitive counting active.")
        search_word = counter_word
        
    word_count = file_txt.count(search_word)
    
    msg_result = "The word " + og_counter_word + " was found " + str(word_count) + " times in this file: " + search_path
    print(msg_result)
    
    msg_results.append(msg_result)
    
    
# if path is directory, search every file in the directory
elif  os.path.isdir(search_path):
    file_list = os.listdir(search_path)
    
    if sensitivity_pref == "y":
        print("Case-sensitive counting active.")
    elif sensitivity_pref != "n":
        print("Invalid option. Case-sensitive counting active.")
    
    # loop through each file in the directory
    for file_name in file_list: 
        file_path = search_path + "/" + file_name 
        
        # only process if item is a file
        if os.path.isfile(file_path):
            with open(file_path, mode="r") as file_obj:
                file_txt = file_obj.read()
                
            search_word = counter_word
            
            # adjust text and word for case sensitivity
            if sensitivity_pref == "n": 
                file_txt = file_txt.lower()
                search_word = counter_word.lower()
                
            # count word in this file    
            word_count = file_txt.count(search_word) 
            
            # create and print result message
            msg_result ="The word " + og_counter_word + " was found " + str(word_count) + " times in this file: " + file_name
            print(msg_result)
            
            # store result message in list
            msg_results.append(msg_result)
            
            
# add all results to the results file
with open("wordcount_results.txt", mode="w") as output_file: 
    for message in msg_results:
        output_file.write(message + "\n")

    
    








    
