import re

password = input("Enter a password: ")

length_ok = False
uppercase_ok = False
lowercase_ok = False
number_ok = False
special_ok = False

if len(password) >= 8:
    length_ok = True

if re.search("[A-Z]", password):
    uppercase_ok = True

if re.search("[a-z]", password):
    lowercase_ok = True

if re.search("[0-9]", password):
    number_ok = True

if re.search("[!@#$%^&*]", password):
    special_ok = True

score = 0

if length_ok:
    score += 1

if uppercase_ok:
    score += 1

if lowercase_ok:
    score += 1

if number_ok:
    score += 1

if special_ok:
    score += 1

if score == 5:
    print("Password Strength: Strong")
elif score >= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")