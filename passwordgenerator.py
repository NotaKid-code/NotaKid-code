import random
print("Password generator V2")
print("")
print("Dein passwort:")
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!%$&§?()'
password = ''
for x in range(32):
    password += random.choice(chars)
print(password)
print("")