
import random

password_list = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

numbers = ["1", '2', '3', '4', '5', '6', '7', '8']

symbols = ['!', '@', '#', '$', '%', '^', '*']

print("welcome to password generator")

try:

    num_letters = int(input("enter how many letters you want?"))
    num_numbers = int(input("enter how many numbers you want?"))
    num_symb = int(input("enter how many symbols you want?"))

    if num_letters <= 0 or num_numbers <= 0 or num_symb <= 0:
        print("enter only positive values")
        exit()

except ValueError as e:
    print("please enter integers only  ")

total_sum = num_letters+num_numbers+num_symb

if total_sum  < 9:
    print("minimum length should be 9,select more")
    exit()

for char in range(0, num_letters):
    random_char = random.choice(letters)
    password_list += random_char

for char in range(0, num_numbers):
    random_char = random.choice(numbers)
    password_list += random_char

for char in range(0, num_symb):
    random_char = random.choice(symbols)
    password_list += random_char

random.shuffle(password_list)
password = "".join(password_list)
print(f"your password is :", password)

strength_Score = 0

if len(password_list) < 9:
    print("add more characters")
else:
    print("length good")
    strength_Score += 1

if num_letters < 4 :
    print("increase letters")
else:
    print("good length of letters")
    strength_Score += 1

if num_symb < 3:
    print("increase symbols")
else:
    print("good length of symbols")
    strength_Score += 1

if num_numbers < 3:
    print("increase numbers")
else:
    print("good length of numbers")
    strength_Score += 1

print(" YOUR PASSWORD STRENGTH IS:")

print(strength_Score)
if strength_Score > 3:
    print("Excellent Password")

elif strength_Score == 3:
    print("Medium Strength")

else:
    print("increase strength")





















