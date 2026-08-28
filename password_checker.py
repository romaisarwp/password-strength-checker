print("Password Strength Checker")
password = input("Enter your password: ")
print("You entered:", password)
# Starting score
score = 0
# Check password length
length = len(password)
print("Password length:", length)
if length >= 8:
    print("Length check: Passed")
    score += 1
else:
    print("Length check: Failed")
# Check for uppercase letters
has_uppercase = False
for character in password:
    if character.isupper():
        has_uppercase = True
if has_uppercase:
    print("Uppercase check: Passed")
    score += 1
else:
    print("Uppercase check: Failed")
# Check for numbers
has_number = False

for character in password:
    if character.isdigit():
        has_number = True

if has_number:
    print("Number check: Passed")
    score += 1
else:
    print("Number check: Failed")

# Check for symbols
symbols = "!@#$%^&*?"
has_symbol = False
for character in password:
    if character in symbols:
        has_symbol = True

if has_symbol:
    print("Symbol check: Passed")
    score += 1
else:
    print("Symbol check: Failed")
# Display score
print("Password score:", score, "/ 4")
# Determine password strength
if score <= 1:
    print("Password strength: Weak")
elif score <= 3:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")