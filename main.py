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

# List slicing
# lists are mutable, strings are not mutable
'''
cart = [
"apples",
"oranges",
"banana",
"grapes"
]

cart[0] = 'berry'
new_cart = cart[:]
new_cart[0] = 'cherries'

print(new_cart)
print(cart)
'''

#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
'''
new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)
'''
# Matrix
'''
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
  ]

access = matrix[2][1]

print(matrix)
print(access)

# access "Oranges" and print it:
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
print(basket[1][1][0])
'''

# List Method 2
# list actions - https://www.w3schools.com/python/python_ref_list.asp
'''
numbers1 = [1,2,3,4,5,6]
#adding
numbers1.append(100)

new_list = numbers1

print(numbers1)
print(new_list)

#insert
numbers2 = [1,2,3,4,5,6]

numbers2.insert(4, 100)

print(numbers2)

#Extend
numbers3 = [1,2,3,4,5,6]
print(numbers3)

numbers3.extend([102,103,104])

print(numbers3)

#Remove (pop), removes end of list
numbers4 = [1,2,3,4,5,6]
print(numbers3)

numbers4.pop()

print(numbers4)

numbers4.pop(0)

print(numbers4)

#clear
numbers5 = [1,2,3,4,5,6]
numbers5.clear()
print(numbers5)
'''

# List Method 2
# Python Keywords - https://www.w3schools.com/python/python_ref_keywords.asp
'''
basket = [1,2,3,4,5,6]
print(basket.index(6))

items = ["apples","banana","orange"]

print(items.index('apples', 0 , 3))

#returns boolean result using python keyword "in"
print('orange' in items)

print('him' in 'This is a story of a girl')

#count how many times string "orange" appears in the list
print(items.count("orange"))
'''

# List Method 3
#
'''
basket = [2,2,1,8,7,4,6,5]

basket.sort()

#print(sorted(basket))
print(basket)

basket.reverse()
print(basket)
'''

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
'''
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

#friends.sort()

print(friends)

new_friend = ['Stanley']

friends.extend(new_friend)
print(sorted(friends))

#new_list = friends + new_friend
#print(new_list)
'''

#Common list patterns
'''
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

#new_list = list(range(1,101))

#print(new_list)

#sentence = " "

#new_sentence = sentence.join(['hi','this','is','shadi'])

new_sentence = ' '.join(['hi','this','is','shadi'])


print(new_sentence)

'''

# List Unpacking
'''
a,b,c,d = [1,2,3,4]
print(a)
print(b)
print(c)
#print(other)
print(d)
'''

# None
'''
a = None
print(a)
'''

# Dictionary
# dictionary is an unordered key value pair
'''dictionary = { "a": 1, 
              "b": 2, 
              "x": 3,
              "d": [1,2,3],
              "e": "hello world",
              "f": True
             
             } 

print(dictionary["d"][2])

print(dictionary)
'''

#Dictionary Keys
#
'''
dictionary = { "a": 1, 
  123: 2, 
  True: 3,
  "d": [1,2,3],
  "e": "hello world",
  "f": True

 } 

print(dictionary[True])

'''

#Dictionary Methods
# Available methods - https://www.w3schools.com/python/python_ref_dictionary.asp
'''
user = {
  'basket': [1,2,3],   
  True: 3,
  "greet": 'hello',
  'age': 50
  
 } 

#print(user['greet'])
# if the "age" key isnt present in the dictionary, we will default to the value "20"
print(user.get('age', 20))
'''

#Dictionary Methods 2
'''
user = {
  'basket': [1,2,3],   
  True: 3,
  "greet": 'hello',
  'age': 50

 } 

print('basket' in user)
#check just the values in the dictionary
print('basket' in user.values())
#check just the keys in the dictionary
print('basket' in user.keys())

#empty dictionary
#print(user.clear())

user2 = user.copy()
print(user)
print(user2)

#removes last key:value pair that was inserted into the dictionary
print(user.popitem())

print(user)
'''

# Exercise Dictionary Methods
'''
# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    'age': 0,
    'username': ' ',
    'weapons': None,
    'is_active': False,
    'clan': None
}

# 2 iterate and print all the keys in the above user.
print(user_profile.keys())

# 3 Add a new weapon to your user
user_profile['weapons'] = 'Katana'

# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})

# 5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True

# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({'age': 50, 'username': 'User2'})
print(user_profile)
print(user2)

'''

#Tuple
#immutable lists
'''
my_tuple = ('apple','grapes','mango', 'grapes')

print(type(my_tuple))

print(my_tuple[2])

print("mango" in my_tuple)
'''

#Tuple
# Tuple method - https://www.w3schools.com/python/python_ref_tuple.asp
'''
my_tuple = (1,2,3,4,5,5,5)

new_tuple = my_tuple[1:2]

print(new_tuple)

#method to count how many times a value appears in the tuple
print(my_tuple.count(5))

'''

# Sets
# unordered collections of unique objects (NO duplicates)
'''
my_set = {1,2,3,4,5,6,5}
my_set.add(100)
print(type(my_set))
print(my_set)

print(1 in my_set)

my_set.pop()
print(my_set)

print(1 in my_set)

my_set.clear()
print(my_set)

'''

# Set 2
# Python set methods - https://www.w3schools.com/python/python_ref_set.asp

#my_set = {1,2,3,4,5,6,5}
#your_set = {4,5,6,7,8,9,10}

#print(my_set.difference(your_set))

#print(my_set.discard(5))
#print(my_set)

#print(my_set.difference_update(your_set))
#print(my_set)

#print(my_set.intersection(your_set))
#print(my_set)

#print(my_set.isdisjoint(your_set))
#print(my_set)
#print(your_set)

#print(my_set.issubset(your_set))
#print(my_set)
#print(your_set)

#print(my_set.issuperset(your_set))
#print(my_set)
#print(your_set)

#print(my_set.union(your_set))
#print(my_set)
#print(your_set)

#Scroll to bottom to see solution
# You are working for the school Principal. We have a database of school students:
'''
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list. 
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!


print(school.difference(attendance_list))
'''

# Conditional Logic
'''
is_old = True
is_license = True

if is_old and is_license:
 print("you are old enough to drive")


#if is_old:
 # print("you are old enough to drive")

#elif is_license:
 # print("you can drive now with your license")

else: 
  print("you are not old enough to drive")

print("end")
'''


# truthy or Falsy 
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false
'''
print(bool(5)) # True
print(bool("hello")) # True
print(bool("")) # False
print(bool(0)) # False
'''


#Ternary Operator
# or conditional expressions
'''
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)
'''

# Short Circuiting
'''
is_friend = True
is_user = True

if is_friend or is_user:
  print("best friends forever")
'''

# Logical operations
# AND
# OR
# > , < , <= , >= , ==
# !=
# NOT
'''
print( 4 == 5)
print( 4 > 5)
print( 4 >= 5)
print( 4 <= 5)
print( 4 < 5)
print(not(1 == 1))
'''

# Exercise Logical operations
'''
is_magician = True
is_expert = False 

if is_magician and is_expert:
  print("You are a master magician!!!")
elif is_magician and not is_expert:
  print("at least your getting there")
elif not is_magician:
  print("you need magic powers")
'''


# is vs ==
'''
print(True == 1) # True
print("" == 1) # False
print([] == 1) # false
print(10 == 10.0) # True
print([] == []) # true


print(True is 1) # false
print("" is 1) # False
print([] is 1) # false
print(10 is 10.0) # false
print([] is []) # false
'''
# For Loops

#for items in 'Zero to Mastery':
 # print(items)

'''
for i in range(1,10):
  print(i)

for i in range(1,5):
  for n in ['a', 'b', 'c', 'd', 'e']:
    for o in ["x","y","z"]:
      print(i , n, o)
'''


# iterable

# these objects are iterable:
# Lists, Dictionary, Tuples, Sets, Strings
'''
user = {
'name': 'golem',
'age': 5005,
'can_swim': False
}

for i in user.items():
  print(i)

for i in user.values():
  print(i)

for i in user.keys():
  print(i)


for key, value in user.items():
  print(value, key)

'''

#Exercise: Tricky Counter
# https://github.com/aneagoie/ztm-python-course-exercises
'''
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0

for item in my_list:
  counter = counter + item

print(counter)
'''




