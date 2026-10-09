## Question 1
'''
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
'''

 ## Question 2
'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    '''

## Question 3
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number is:", a)
else:
    print("Greater number is:", b)
    '''

## Question 4
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest is:", a)
elif b >= a and b >= c:
    print("Greatest is:", b)
else:
    print("Greatest is:", c)
    '''

## Question 5
'''
age = int (input ("Enter your age: "))
if age >= 18: 
    print ("You are eligible to vote.")
else:
    print ("You are not eligible to vote.")
    '''

## Question 6

'''
year = int(input("Enter a year:"))
if year % 4 == 0 :
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.") 
    '''

## Question 7
''''
ch = input("Enter a character: ")

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")
    '''

## Question 8
'''
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")
    '''

## Question 9
'''
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Multiple of 3 and 7")
else:
    print("Not a multiple of 3 and 7")
    '''

## Question 10
'''
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
    '''

## Question 11
'''
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
else:
    print("Lowercase")
    '''

## Question 12
'''
ch = input("Enter a character: ")

if ch == "a":
    print("Vowel")
elif ch == "e":
    print("Vowel")
elif ch == "i":
    print("Vowel")
elif ch == "o":
    print("Vowel")
elif ch == "u":
    print("Vowel")
else:
    print("Consonant")
    '''

## Question 13
'''
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a + b > c and b + c > a and a + c > b:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")
    '''

## Question 14
'''
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
    '''

## Question 15
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

if d > largest:
    largest = d

print("Largest is:", largest)
'''

## Question 16
'''
num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")
    '''
## Question 17
'''
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
else:
    bill = units * 7

print("Electricity bill:", bill)
'''

## Question 18
'''
income = int(input("Enter income: "))

if income <= 250000:
    tax = 0
else:
    tax = income * 0.10

print("Tax:", tax)
'''

## Question 19
'''
maths = int(input("Enter Maths marks: "))
english = int(input("Enter English marks: "))

if maths >= 35 and english >= 35:
    print("Pass")
else:
    print("Fail")
    '''

## Question 20
'''
num = int(input("Enter a number: "))

if num >= 1 and num <= 10:
    print("Number is within range")
else:
    print("Number is outside range")
    '''

## Question 21
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator: ")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")
    '''

## Question 22
'''
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Century leap year")
else:
    print("Not a century leap year")
    '''

## Question 23
'''
month = int(input("Enter month number: "))

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Summer")
elif month == 6 or month == 7 or month == 8 or month == 9:
    print("Monsoon")
elif month == 10 or month == 11:
    print("Winter")
else:
    print("Invalid month")
    '''

## Question 24
'''
month = int(input("Enter month number: "))

if month == 2:
    print("28 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
else:
    print("31 days")
    '''

## Question2 25
'''
password = input("Enter password: ")

if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is valid")
else:
    print("Password is not valid")
    '''

## Question 26
'''
age = int(input("Enter age: "))

if age < 5:
    print("Ticket is free")
elif age < 18:
    print("Ticket price is 50")
else:
    print("Ticket price is 100")
    '''

## Question 27
'''
amount = int(input("Enter purchase amount: "))

if amount >= 1000:
    discount = amount * 0.10
    print("Discount:", discount)
else:
    print("No discount")
    '''

## Question 28
'''
age = int(input("Enter age: "))
eyesight = input("Do you have good eyesight? ")

if age >= 18 and eyesight == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible")
    '''

## Question 29 
'''
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
    '''

## Question 30
'''
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Answer:", a + b)

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Answer:", a - b)

elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Answer:", a * b)

elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Answer:", a / b)

elif choice == 5:
    print("Exit")

else:
    print("Invalid choice")
    '''