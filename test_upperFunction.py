def toUpperCase(name):
    return name.upper()

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

uppercased_first_name = toUpperCase(first_name)
uppercased_last_name = toUpperCase(last_name)

print("Input - First Name: " + first_name.title() )
print("Your first name has been converted to uppercasing below:\n" + uppercased_first_name)

print("Input - Last Name: " + first_name.title() )
print("Your last name has been converted to uppercasing below:\n" + uppercased_last_name)

print("------------------------")

print("Hello, " + first_name.title() + " " + last_name.title() + "!")
print("Number of letters in first name: ", len(first_name) )
print("Number of letters in last name: " , len(last_name) )