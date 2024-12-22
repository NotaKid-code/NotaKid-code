print(".---------------------------------------------------.")
print("| _____               _         _     _     _       |")
print("||_   _|__         __| | ___   | |   (_)___| |_ ___ |")
print("|  | |/ _ \ _____ / _` |/ _ \  | |   | / __| __/ _ \|")
print("|  | | (_) |_____| (_| | (_) | | |___| \__ \ ||  __/|")
print("|  |_|\___/       \__,_|\___/  |_____|_|___/\__\___||")
print("'---------------------------------------------------'")
print("")

todos = []


for _ in range(100000):
    print("Was willst du tun?")
    print("(1) To-dos anzeigen")
    print("(2) To-dos hinzufügen")

    option = input("Bitte auswählen: ")

    if int(option) == 1:
        print("Meine Liste hat diese Elemente:")

        for todo in todos:
            print(f"- {todo}")

    if int(option) == 2:
        newitem = input("Was möchtest du hinzufügen? ")
        todos.append(newitem)

    print("")
    print("")

print("Programm beendet.")