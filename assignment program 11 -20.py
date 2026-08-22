# 11. write a program to extract values between quotation marks of a string.

def extract_quotes(text):
    parts = text.split('"')
    return parts[1::2]

input_str = 'Python is a powerful high level programming language.'
result = extract_quotes(input_str)

print('Original Text:', input_str)
print('Extracted Values:', result)

# 12. write a program to convert snake case string to camel case string.

def snake_to_camel(text):
    words = text.split('_')
    camel_words = [words[0]]+[word.capitalize() for word in words[1:]]
    return ''.join(camel_words)

input_str = 'python_programming_language'
result = snake_to_camel(input_str)

print('Original Text: ',input_str)
print('CamelCase: ',result)

# 13. write a program to determine whether a given year is a leap year.

def is_leap_year(year):
    #True if divisible by 400, OR (divisible by 4 and NOT divisible by 100)
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

#Test the program
years = [2000,2024,1901,2026]
for y in years:
    if is_leap_year(y):
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is NOT a leap year.")

# 14. write a program to convert a string to datetime.

from datetime import datetime

date_string = "2026-08-22 15:30:00"

date_time = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

print(date_time)

# 15. write a function that accepts a string and calculate the number of upper case letter and lower case letters.

def count_case_letters(text):
    uppercase = 0
    lowercase = 0

    for char in text:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1

    return uppercase, lowercase


# Example
text = "Hello World!"
upper, lower = count_case_letters(text)

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

# 16. write a function that takes a list and returns a new list with unquie elements of the first list.

def unique_elements(items):
    unique = []

    for item in items:
        if item not in unique:
            unique.append(item)

    return unique


# Example
numbers = [1, 2, 2, 3, 4, 4, 5]

print(unique_elements(numbers))

# 17.write a function that takes a number as a parameter and check the number is prime or not.

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
# Example
print(is_prime(7))   # True
print(is_prime(10))  # False

# 18. write a program to print the even numbers fron a given list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(number)

# 19. write a function to check whether a number is perfect or not.

def is_perfect(number):
    if number <= 1:
        return False

    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    return total == number

# Example
print(is_perfect(6))   # True
print(is_perfect(10))  # False

# 20. write a program to reverse a string word by word.

def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)


# Example
text = "Hello world from python"
print(reverse_words(text))




