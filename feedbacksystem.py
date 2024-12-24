print("Feedback system!")
print("")
print("In which language do you want to continue?")
print("")
user_input = int(input("German[1] English[2]: "))  
print("")

if user_input == 1:  # Deutsch
    print("Hat es dir gefallen?")
    response = int(input("Ja[1] Nein[2]: "))  
    if response == 1:
        print("Schön, dass es dir gefallen hat! Wenn du möchtest, zeige deinen Freunden das Programm!")
    elif response == 2:
        reason = input("Warum gefällt es dir nicht? Schreibe bitte auf: ")
        print("Mhm, okay.")

elif user_input == 2:  # English
    print("Do you like it?")
    response = int(input("Yes[1] No[2]: ")) 
    if response == 1:
        print("Glad you liked it! If you want, show the program to your friends!")
    elif response == 2: 
        reason = input("Why don't you like it? Tell us: ")
        print("Mhm, okay.") 

else:
    print("Invalid input. Please restart the program and choose 1 or 2.")

input("Press Enter to close...")

