print("Password Strength Checker")
password = input("Enter your password: ")
print("You entered:", password)
length = len(password)
print("Password length:", length)
if length >= 8:
    print("Length check: Passed")
else:
    print("Length check: Failed")