# 1. Check whether a number is Even or Odd
'''
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    '''

# 2. Find the Largest of Three Numbers
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number is:", a)
elif b > a and b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
    '''

# 3. Check Whether a Number is Prime
'''
n = int(input("Enter a number: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
    '''

# 4.Print Fibonacci Series up to n Terms
'''
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
'''

# 5.Find Factorial Using a Loop 
'''
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)
'''

# 6.Reverse a String Without Using [::-1]
'''
name = input("Enter a string: ")

reverse = ""

for i in name:
    reverse = i + reverse

print("Reverse string:", reverse)
'''

# 7. Check Whether a String is Palindrome
'''
name = input("Enter a string: ")

reverse = ""

for i in name:
    reverse = i + reverse

if name == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
    '''

# 8. Count Vowels and Consonants
'''
name = input("Enter a string: ")

vowels = 0
consonants = 0

for i in name.lower():
    if i in "aeiou":
        vowels += 1
    elif i.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
'''

# 9.Find Sum of All Elements in a List
'''
numbers = [10, 50, 20, 5, 40]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)
'''

# 10. Find Largest and Smallest Without max() or min()
'''
numbers = [10, 50, 20, 5, 40]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)
'''
# 11.Remove Duplicate Elements from a List
'''
numbers = [10, 20, 10, 30, 20, 40]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)
'''

# 12.Count Each Element Using Dictionary
'''
numbers = [10, 20, 10, 30, 20, 10]

count = {}

for i in numbers:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)
'''

# 13. Find Second-Largest Number in a List
'''
numbers = [10, 50, 30, 20, 40]

largest = numbers[0]
second = None

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i != largest and (second is None or i > second):
        second = i

print("Second largest:", second)
'''

# 14. Write a program to sort a list without using sort() or sorted().
'''
numbers = [50, 20, 40, 10, 30]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Sorted list:", numbers)
'''

# 15. Function to Return Only Even Numbers
'''
def get_even_numbers(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
    '''

# 16. Find Frequency of Each Character in a String
'''
name = "hello"

count = {}

for i in name:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)
'''

# 17. Check Whether Two Strings are Anagrams
'''
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("Anagrams")
else:
    print("Not anagrams")
    '''

# 18. Find All Duplicate Values in a List
'''
numbers = [10, 20, 30, 10, 40, 20, 50]

duplicates = []

for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate values:", duplicates)
'''

# 19. Find the Longest Word in a Sentence
'''
sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word:", longest)
'''

# 20. Student Marks Program
'''
marks = []

for i in range(5):
    m = int(input("Enter subject marks: "))
    marks.append(m)

total = sum(marks)

percentage = total / 5

print("Total marks:", total)
print("Percentage:", percentage)

if any(m < 35 for m in marks):
    print("Result: Fail")

elif percentage >= 90:
    print("Grade: A")
    print("Result: Pass")

elif percentage >= 75:
    print("Grade: B")
    print("Result: Pass")

elif percentage >= 60:
    print("Grade: C")
    print("Result: Pass")

elif percentage >= 35:
    print("Grade: D")
    print("Result: Pass")
    '''