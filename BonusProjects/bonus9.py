password = input("Enter a password: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for char in password:
    if char.isdigit():
        digit = True

result.append(digit)

uppercase = False
for char in password:
    if char.isupper():
        uppercase = True

result.append(uppercase)

if all(result):
    print("Strong password")
else:
    print("Weak password")