# 1. Data Types
 # 1. Find the data type of every value in a mixed list.
'''
my_list = [10, 10.5, "Hello", True, 5+2j, [1, 2], (3, 4)]

for value in my_list:
    print(value, "=", type(value))
    '''

# 2. Convert a nested list into a tuple of tuples.
'''
my_list = [[1, 2], [3, 4], [5, 6]]

result = tuple(tuple(x) for x in my_list)

print(result)
'''

# 3. Remove all duplicate values from a mixed list while preserving original order.
'''
my_list = [10, 20, "Hello", 10, 30, "Hello", 40]

result = []

for value in my_list:
    if value not in result:
        result.append(value)

print(result)
'''

# 4.Check whether a number is a power of 2 using operators.
'''
n = 16

if n > 0 and (n & (n - 1)) == 0:
    print("Power of 2")
else:
    print("Not a power of 2")
'''

# 5.Swap two numbers using bitwise XOR.
'''
a = 10
b = 20

a = a ^ b
b = a ^ b
a = a ^ b

print("a =", a)
print("b =", b)
'''

#6. Check whether a number is divisible by both 4 and 6 using logical operators.
'''
n = 24

if n % 4 == 0 and n % 6 == 0:
    print("Divisible by both 4 and 6")
else:
    print("Not divisible")
    '''

# 7.Calculate the total electricity bill using different unit rates.
'''
units = 250

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7

else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity Bill =", bill)
'''

# 3. Conditional Statements
# 8. Check whether three sides can form a triangle.
'''
a = 5
b = 6
c = 7

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
    '''

#9. Determine the type of triangle.
'''
a = 5
b = 5
c = 5

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Invalid Triangle")
    '''

# 10.Create a simple ATM menu.
'''
balance = 5000

print("1. Withdraw")
print("2. Deposit")
print("3. Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter amount: "))

    if amount > 0 and amount <= balance:
        balance -= amount
        print("Withdraw successful")
        print("Balance:", balance)
    else:
        print("Invalid amount")

elif choice == 2:
    amount = int(input("Enter amount: "))

    if amount > 0:
        balance += amount
        print("Deposit successful")
        print("Balance:", balance)
    else:
        print("Invalid amount")

elif choice == 3:
    print("Balance:", balance)

else:
    print("Invalid choice")
    '''

 # 11. Calculate income tax based on different tax slabs.
'''
 income = 800000

if income <= 300000:
    tax = 0

elif income <= 700000:
    tax = (income - 300000) * 0.05

elif income <= 1000000:
    tax = (400000 * 0.05) + (income - 700000) * 0.10

else:
    tax = (400000 * 0.05) + (300000 * 0.10) + (income - 1000000) * 0.15

print("Income Tax =", tax)
'''

# 12. Menu-driven calculator using if-elif.
'''
a = 20
b = 10
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Addition =", a + b)

elif choice == 2:
    print("Subtraction =", a - b)

elif choice == 3:
    print("Multiplication =", a * b)

elif choice == 4:
    print("Division =", a / b)

else:
    print("Invalid choice")
    '''

# 4. Loops
# 13. Print all prime numbers between 1 and n.
'''
n = 20
print("Prime numbers between 1 and", n, "are:")

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        '''

# 14. Find factorial using a loop.
'''
n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)
'''
# 15. Print Fibonacci series up to n terms.
'''
n = 7

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    a, b = b, a + b
    '''

# 16. Check whether a number is an Armstrong number.
'''
n = 153

temp = n
power = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp = temp // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
    '''
# 17. Reverse a number and check whether it is a palindrome.
'''
n = 121
temp = n
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reverse =", reverse)

if n == reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome")
    '''
# 18. Find GCD of two numbers.
'''
a = 12
b = 8

while b:
    a, b = b, a % b

print("GCD =", a)
'''

# 19. Write a function to check if a string is a palindrome.
'''
def palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(palindrome("madam"))
'''

# 20. Count vowels and consonants in a string.
'''
def count_letters(text):

    vowels = 0
    consonants = 0

    for ch in text.lower():

        if ch in "aeiou":
            vowels += 1

        elif ch.isalpha():
            consonants += 1

    print("Vowels =", vowels)
    print("Consonants =", consonants)

count_letters("Hello World")
'''
# 21. Function to calculate Simple Interest and Compound Interest.
'''
def factors(n):

    result = []

    for i in range(1, n + 1):

        if n % i == 0:
            result.append(i)

    return result

print(factors(12))
'''

# 22. Function to return all factors of a number.
'''
def factors(n):

    result = []

    for i in range(1, n + 1):

        if n % i == 0:
            result.append(i)

    return result

print(factors(12))
'''

# 23. Find the second-largest number in a list.
'''
def second_largest(numbers):

    unique = list(set(numbers))
    unique.sort()

    if len(unique) < 2:
        return "Second largest not available"

    return unique[-2]

numbers = [10, 20, 30, 40, 50]

print("Second Largest =", second_largest(numbers))
'''

# 6. Lists
# Merge two lists without duplicates.
'''
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged = list(set(list1 + list2))
print("Merged List =", merged)
'''

# 25. Find the second-largest and second-smallest elements.
'''
def second_largest_smallest(numbers):
    unique = list(set(numbers))
    unique.sort()

    if len(unique) < 2:
        return "Second largest or smallest not available"

    return unique[-2], unique[1]

numbers = [10, 20, 30, 40, 50]

second_largest, second_smallest = second_largest_smallest(numbers)
print("Second Largest =", second_largest)
print("Second Smallest =", second_smallest)
'''

#26. Rotate a list to the left by k positions.
'''
def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

numbers = [1, 2, 3, 4, 5]
k = 2
print("Original List =", numbers)
print("Rotated List =", rotate_left(numbers, k))
'''

#27. Separate even and odd numbers into two lists.
'''
def separate_even_odd(numbers):
    even = []
    odd = []

    for n in numbers:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    return even, odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = separate_even_odd(numbers)
print("Even Numbers =", even_numbers)
print("Odd Numbers =", odd_numbers)
'''

# 28. Find common elements between two lists.
'''
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = find_common_elements(list1, list2)
print("Common Elements =", common)
'''

#7. Tuples & Sets
#29. Count the frequency of each element in a tuple.
'''
def count_frequency(t):
    freq = {}
    for item in t:
        freq[item] = freq.get(item, 0) + 1
    return freq

t = (1, 2, 2, 3, 3, 3)
print("Frequency =", count_frequency(t))
'''

# 30. Find union, intersection and difference of two sets.
'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union =", a.union(b))

print("Intersection =", a.intersection(b))

print("Difference =", a.difference(b))
'''

# 31. Check whether one set is a subset of another.
'''
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

if a.issubset(b):
    print("A is a subset of B")
else:
    print("A is not a subset of B")
    '''

#8. Dictionaries
#32. Count the frequency of words in a sentence.
'''
def count_word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence = "the quick brown fox jumps over the lazy dog"
print("Word Frequency =", count_word_frequency(sentence))
'''

#33. Create a dictionary from two lists (keys and values).
'''
def create_dict(keys, values):
    return dict(zip(keys, values))

keys = ['a', 'b', 'c']
values = [1, 2, 3]
print("Created Dictionary =", create_dict(keys, values))
'''

#34. Sort a dictionary by its values.
'''
def sort_dict_by_values(d):
    return sorted(d.items(), key=lambda x: x[1])

d = {'a': 3, 'b': 1, 'c': 2}
print("Sorted Dictionary =", sort_dict_by_values(d))
'''

#9. File Handling
#35. Read a text file and count lines, words and characters.
'''
def count_lines_words_characters(filename):
    with open(filename, 'r') as f:
        content = f.read()
        lines = content.split('\n')
        words = content.split()
        characters = len(content)
    return len(lines) - 1, len(words), characters

filename = "sample.txt"
lines, words, characters = count_lines_words_characters(filename)
print("Lines =", lines)
print("Words =", words)
print("Characters =", characters)
'''

#36. Copy only even-numbered lines from one file to another.
'''
def copy_even_lines(source_file, target_file):
    with open(source_file, 'r') as f:
        lines = f.readlines()

    even_lines = [line for i, line in enumerate(lines) if i % 2 == 1]

    with open(target_file, 'w') as f:
        f.writelines(even_lines)

copy_even_lines("source.txt", "target.txt")
'''
#10. Exception Handling
#37. Handle invalid integer input using try-except.
'''
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    '''

# 38. Handle file-not-found errors while reading a file.
'''
try:

    file = open("hello.txt", "r")

    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:

    print("File not found")
    '''

#11. Modules
#39. Create a random password generator using random and string modules.
'''
import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(8):
    password += random.choice(characters)

print("Generated Password =", password)
'''

# 40. Calculate the number of days between two dates using datetime.
'''
from datetime import date

date1 = date(2026, 1, 1)
date2 = date(2026, 11, 5)

difference = date2 - date1

print("Total Days =", difference.days)
'''

