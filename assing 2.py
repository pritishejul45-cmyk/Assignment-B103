#question 1
'''
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(4))
print(is_even(7))
'''

# Question 2
'''
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(10, 20))
'''

# Question 3
'''
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)
'''

#Question 4
'''
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(sum_n(5))
'''

#Question 5
'''
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table(5)
'''
# Question 6
'''
def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count = count + 1
    return count

print(count_even([1, 2, 3, 4, 6]))
'''

# Question 7
'''
def find_max(numbers):
    largest = numbers[0]

    for n in numbers:
        if n > largest:
            largest = n

    return largest

print(find_max([10, 25, 8, 40, 15]))
'''

# Question 8
'''
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade(95))
print(grade(85))
print(grade(72))
print(grade(65))
print(grade(40))
'''
# Question 9
'''
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
'''

# Question 10
'''
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("madam"))
print(palindrome("hello"))
'''

# Question 11
'''
def count_vowels(text):
    count = 0

    for letter in text.lower():
        if letter in "aeiou":
            count = count + 1

    return count

print(count_vowels("Hello World"))
'''

# Question 12
'''
def second_largest(numbers):
    largest = float("-inf")
    second = float("-inf")

    for n in numbers:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n

    if second == float("-inf"):
        return None

    return second

print(second_largest([10, 20, 40, 30, 15]))
'''

# Question 13
'''
import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number from 1 to 10: "))

        if guess == number:
            print("Correct! You won!")
            break
        else:
            print("Try again!")

guessing_game()
'''