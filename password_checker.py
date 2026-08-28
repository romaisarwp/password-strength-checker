print("Password Strength Checker")
password = input("Enter your password: ")
print("You entered:", password)

# Check password length

length = len(password)
print("Password length:", length)
if length >= 8:
    print("Length check: Passed")
else:
    print("Length check: Failed")

# Check for uppercase letters

has_uppercase = False

for character in password:
    if character.isupper():
        has_uppercase = True

if has_uppercase:
    print("Uppercase check: Passed")
else:
    print("Uppercase check: Failed")