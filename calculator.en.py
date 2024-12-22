print("Calculator test!")
print("")
print("This is a calculator that can help with some math problems")
print("")
print("Please choose a calculation method, use one of the following 4 types")
print("")
user_input = int(input("[1]Plus [2]Minus [3]Multiply [4]Divide:"))
print("")
print("Now please enter the numbers")
first_number = int(input("First number:"))
second_number = int(input("Second number:"))
if user_input == 1:
    print("Your result is:", first_number + second_number)
if user_input == 2:
    print("Your result is:", first_number - second_number)
if user_input == 3:
    print("Your result is:", first_number * second_number)
if user_input == 4:
    print("Your result is:", first_number / second_number)
print("")
print("Thanks for using the Calculator")
print("")
input("Press Enter to finish the process")