def toLowerCase(name):
    return name.lower()

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
codex = input("What is the codex? ")

lowercased_first_name = toLowerCase(first_name)
lowercased_last_name = toLowerCase(last_name)

print("Input - First Name: " + first_name)
print("Your first name has been converted to lowercasing below:\n" + lowercased_first_name + "\n")

print("Input - Last Name: " + last_name)
print("Your last name has been converted to lowercasing below:\n" + lowercased_last_name)

print("------------------------")

# Note you couldnt "+ len() because you are not concatenating a string. 
# In order to use this method you would need to use the str() function "
print("Hello, " + first_name.title() + " " + last_name.title() + "!")
print("Number of letters in first name: ", len(first_name) )
print("Number of letters in last name: " , len(last_name) )
print("Number of letters in codex: " + str(len(codex)) )