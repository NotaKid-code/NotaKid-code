print("Taschenrechner Test!")
print("")
print("Dies ist ein Taschenrechner der bei der ein oder anderen Mathe aufgaben helfen kann")
print("")
print("Wähle bitte eine Rechenartm, benutze eine von den folgenden 4 Arten")
user_input = int(input("[1]Addieren [2]Subtrahieren [3]Multiplizieren [4]Dividieren:"))
print("")
print("Jetzt gebe bitte die Zahlen ein")
erste_zahl = int(input("Erste Zahl:"))
zweite_zahl = int(input("Zweite Zahl:"))
if user_input == 1:
    print("Dein Ergebnis lautet:", erste_zahl + zweite_zahl)
if user_input == 2:
    print("Dein Ergebnis lautet:", erste_zahl - zweite_zahl)
if user_input == 3:
    print("Dein Ergebnis lautet:", erste_zahl * zweite_zahl)
if user_input == 4:
    print("Dein Ergebnis lautet:", erste_zahl / zweite_zahl)
print("")
print("Danke das sie den Taschenrechner benutzt haben")
print("")
input("Drücken sie Enter um den Vorgang zu beenden")