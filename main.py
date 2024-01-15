#beginning - just revisit simple basics
''' age = input("How old are you? ")
name = input("what is your name? ")
age = int(age)
name = str(name)
print(f"{age}")
print(f"{name}")

val1 = 5
val2 = 7
donation = val1 + val2 + age
print(f'Thanks {name}, I will received ${donation} in donations')
'''

#data type
#int and float

'''print(type(123))
print(type(2 + 4))# int
print(type(2 - 4)) # int
print(type(2 * 4)) # int
print(type(2 /4 )) # float

print(2 ** 4) # 2 to the power of 4
print(2 // 4) # rounded down operator to an integer
print(5 % 4) # remainder / modular numbers.
'''

# Int and Float 
# Maths functions - https://www.programiz.com/python-programming/modules/math
'''print(round(5.9)) # round out the number to closest int
print(abs(20)) # whats the absolute value of a number, ie no negative numbers
'''

# Operator precedence
# Order of execution

# 1. () brackets
# 2. ** exponent
# 3. * / // % (left to right)

#binary representation 
'''print(bin(5.5)) # changes the number to binary 
'''

#Variables -
# python keywords - https://www.w3schools.com/python/python_ref_keywords.asp

'''iq = 140
user_age = iq/4
another = user_age

print(another)

a,b,c = 1,2,3

print(a)
print(b)
print(c)
'''

# Augmented Assignment Operator

'''some_value = 5
some_value += 5

print(some_value)

# Exercise Augmented Assignment Operator
# Guess what happens here before you click RUN!
counter = 0

counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *= 2

print(counter) #what will this print?
'''

#String
'''

name = "shadi ferris"
location = "australia"

print(type(name))
print(f"My name is {name} and I live in {location}")

first_name = "shadi"
last_name = "ferris"
full_name = first_name + " " + last_name

print(full_name)
'''

#string concentration
'''
print('hello' + ' ' + 'world')
print('hello' + ' ' + '5')
'''

#type conversion
'''
a = str(100)
b = int(a)
c = type(b)

print(c)

'''

#escape sequences
'''
weather = "it\'s \"kind of\" sunny"
print(weather)

tab = "\t there is a \"tab\" at the beginning"
print(tab)

new_line = "\n there is a \"new line\" at the beginning"
print(new_line)
'''

#formatting strings
#f string

'''name = "Shadi"
age = 35
print(f'Hi {name}, how are you? you need to be {age} years old')
'''

# string indexes

# [start:stop:stepover]

'''index = "Hello World!"

print(index[::2]) # prints every other character
print(index[-1]) # prints the last character
print(index[::-1]) # prints the string backwards
print(index[::-2]) # prints the string backwards every other character



print(index[-2])
'''

#Immutability

# [start:stop:stepover]

'''selfish = "01234567"

selfish = selfish + 8

print(selfish)
'''
#Built in functions + methods

#Functions - https://docs.python.org/3/library/functions.html
# String methods - https://www.w3schools.com/python/python_ref_string.asp
'''
greet = "Hello World"
shake = "to be or not to be"
print(len(greet))

new = greet.upper()
new2 = shake.replace('be', 'you')
print(new)
print(new2)
'''

# Boolean
# True or False
'''
name = "Shadi"
print(bool(1))
'''

# Exercise Type Conversion

'''birth_year = input("what year were you born? ")
name = input("what is your name? ")
status = input("what is your status? ")

#can use either 'birth_year = int(birth_year)' or "int(birth_year)"

age = 2024 - int(birth_year)

print(f"Hi {name}, you are {age} years old and you are {status}")
'''

# Exercise Password Checker
'''
username = input("What is your username? ")
password = input("what is your password? ")

password_length = len(password)

length = "*" * int(password_length)

print(f'Your {username}, of {length} is {password_length} characters long')

'''

# List

# Data Structure
'''
numbers = [1,2,3,4,5,6]
letters = ['a','b','c']
random = [1,2,'c','hello']

print(numbers[1])
print(letters[2])
print(random[3])
'''








