# Function that requires two numbers that will then be added 
def addingCalculator (x,y):
    x_number = int(x)
    y_number = int(y)

    result = x_number + y_number

    return result

firstNum = input("What is the first number: ")
secondNum = input("What is the second number: ")

answer = addingCalculator(firstNum,secondNum)

print(f"You are adding {firstNum} and {secondNum} together.")
print("Your answer is: " ,answer)
if (answer == 69):
    print("\tNice!!!")
else:
    print("\tNot bad. But it could have been better!")