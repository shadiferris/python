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

# Range
'''
for number in range(0, 10):
  print(number)

for number in range(0, 10, 2):
  print(number)

for number in range(10, 0, -2):
  print(number)


#convert a range of 1-10 into a list twice:
for number in range(2):
  print(list(range(10)))

'''

# Enumerate
'''
for i,char in enumerate('hello'):
  print(i, char)

for i,char in enumerate((1,2,3)):
  print(i, char)

for i,char in enumerate([1,2,3]):
  print(i, char)

for i,char in enumerate(list(range(10))):
  print(i, char)
  if char == 5:
    print(f'Index of char is: {i}')

'''

#While loops
'''
i = 0

while i < 10:
  print(i)
  #i = i +1
  i += 1
  #break
else:
  print("done with all the work")
'''

#While loops 2
'''
while True:
  response = input("what do you want to do? ")
  if (response == "bye"):
    break
  
'''

# break, continue, pass
'''
my_list = [1,2,3]

for items in my_list:
  print(my_list)
  #break
  continue



i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1
  #break
  continue
'''

# our first GUI

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
'''
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#for row in picture:
#  for pixel in row:
#    if (pixel == 1):
#      print('*', end='')
#    else:# (pixel == 0):
#      print(' ', end='')
#  print(' ') # need a new line after ever row

fill = "*"
empty = " "
for row in picture:
  for pixel in row:
    if (pixel == 1):
      print(fill, end='')
    else:# (pixel == 0):
      print(empty, end='')
  print(' ') # need a new line after ever row


'''
# Exercise : Find Duplicates
'''
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates =[]
for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates: # lists single value in list.
      duplicates.append(value)
   
print(duplicates)

'''

#Functions
'''
def print_hello():
  print("hellooo!")


print_hello()

'''

#Arguments vs Parameters
'''
#parameters
def print_hello(name, age):
  print(f"hellooo! {name} {age}")


#arguments (aka -  "call" or "invoke")
print_hello("Shadi", "36")
print_hello("Milia", "35")
print_hello("Frank", "5")
print_hello("Joseph", "4")
print_hello("Lucas", "2")
'''

# Defult parameters and keyword arguments
'''

def print_hello(name, age):
  print(f"hellooo! {name} {age}")


#positional arguments (aka -  "call" or "invoke")
print_hello("Shadi", "36")

#keywork arguments (not good practise)
#print_hello(age='23', name='slim')

def print_hello_default(name="slim shady", age="infinite"):
  print(f"hellooo! {name} {age}")


print_hello_default()

'''

# Return
#
# Functions should do something really well
# return something
'''
def sum(num1, num2):
  return num1 + num2
  #print(total)

#total = sum(10,20)
#print(total)
#print(sum(10,total))



no1 = int(input("hi, please provide one number for addition? "))
no2 = int(input("please provide another number? "))

total = sum(no1, no2)
print(f"the total of the two input numbers is {total}")
print(type(total))
'''

# Function Tesla exercise

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
'''
#def checkDriverAge():
  age = input("What is your age? ")
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")


#checkDriverAge()

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.
def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge(92)

'''

# Methods vs Functions
# Library references - https://docs.python.org/3/library/index.html

# Docstrings
'''
def test(a):
  
  #Info: this function tests and print param a
  
  print(a)

#help(test)
# gives information about the function!!!
print(test.__doc__)
'''

# Clean code
'''
def is_odd_or_even(num):
  #num = int(input("pick a number? "))
  return num % 2 != 0


print(is_odd_or_even(5))
'''

# *args and **kwargs
'''
def super_func(*args, **kwargs):
  #print(args)
  #print(kwargs)
  total = 0
  for items in kwargs.values():
    total += items

  return sum(args) + total


print(super_func(1,2,3,4,5, num1=5, num2=10))
'''

# Exercise Functions (my answer)
# Highest Even: Write a function to find the highest even number from the list.
'''
def highest_even(*args):
  new_list = []
  for i in args:
    if i % 2 == 0:
      new_list.append(i)
  
  new_list.sort(reverse=True)
  return new_list[0]


print(highest_even(4,5,7,1,10,11,22))
'''
# Exercise Functions (course answer)
# Highest Even: Write a function to find the highest even number from the list.
'''

def highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
'''

#Walrus Operator
#  :=
'''
a = 'Helllooooooo!!!'

if ((n := len(a)) >= 10):
  print(f"Too long {n} elements")

while ((n := len(a)) >= 1):
  print(n)
  a = a[:-1]

print(a)
'''

# Scope - what variables do i have access too?
# scope rule
# https://www.geeksforgeeks.org/global-local-variables-python/
'''Python Global variables are those which are not defined inside any function and have a global scope whereas Python local variables are those which are defined inside a function and their scope is limited to that function only.

Scope precidence:
1. Start with local
2. Parent Local
3. Global
4. Build in python function

'''

# Global Keyword
# using global variables within functions
'''
total = 0

def count():
  global total
  total += 1
  return total

count()
count()
print(count())
'''

# Nonlocal Keywords
'''
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal1"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
'''
#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions

# Exercise : Imposter syndrome

# Object Oriented Programming
'''

class BigObject: # Class
  pass


obj1 = BigObject() # Instanciate

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))
print(type(obj1))
'''

# Creating Our own Objects
'''
class PlayerCharacter: # class
  def __init__(self, name, age):
    self.name = name
    self.age = age


  def run(self):
    print("run1")
    return "done"

player1 = PlayerCharacter("slim", 22)
player2 = PlayerCharacter("shady", 50)


print(player1)
print(player2)

print(player1.name)
print(player2.name)

print(player1.age)
print(player2.age)

print(player1.run())

'''

# Attributes and Methods
'''
class PlayerCharacter: # class
  #Class object attribute
  membership = True
  
  
  def __init__(self, name, age):
    if (self.membership):
      self.name = name
      self.age = age


  def run(self):
    print("run1")
    return "done"
  
  def shout(self):
    print(f'My name is {self.name}')
    

player1 = PlayerCharacter("slim", 22)
player2 = PlayerCharacter("shady", 50)

print(player1.membership)
print(player2.membership)

print(player1.shout())

#help(dict)
#print(player1)
#print(player2)

#print(player1.name)
#print(player2.name)

#print(player1.age)
#print(player2.age)

#print(player1.run())

'''

# __init__
'''
class PlayerCharacter: # class
  #Class object attribute
  membership = True


  def __init__(self, name="Shadi", age=0):
    if (age > 18):
      self.name = name
      self.age = age
      print("You are old enough!!")

    else:
      self.name = name
      self.age = age
      print("Age is too young!!!")
      

  def run(self):
    print("run1")
    return "done"

  def shout(self):
    print(f'My name is {self.name}')


player1 = PlayerCharacter("slim", 11)
player2 = PlayerCharacter("shady", 50)

print(player1.age)
print(player2.age)

print(player2.membership)

'''

#Exercise - Given the below class:
'''
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def oldest_cat(*args):
      return max(args)

# 1 Instantiate the Cat object with 3 cats

cat1 = Cat("Frank", 6)
cat2 = Cat("Joseph", 4)
cat3 = Cat("Lucas", 2)

print(cat1.name)
print(cat1.age)

print(cat2.name)
print(cat2.age)

print(cat3.name)
print(cat3.age)

# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
  return max(args)



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {Cat.oldest_cat(cat1.age,cat2.age,cat3.age)} years old.")

'''


# @classmethod and @staticmethod
# https://www.makeuseof.com/tag/python-instance-static-class-methods/
'''

class PlayerCharacter:  # class
  #Class object attribute
  membership = True

  def __init__(self, name="Shadi", age=0):
    if (age > 18):
      self.name = name
      self.age = age
      print("You are old enough!!")

  def run(self):
    print("run1")
    return "done"

  def shout(self):
    print(f'My name is {self.name}')
    return self.age

  @classmethod
  def adding_things(cls, num1, num2):
    return num1 + num2
  
  @staticmethod
  def adding_things2(cls, num1, num2):
    return num1 + num2


player1 = PlayerCharacter("slim", 30)
player2 = PlayerCharacter("shady", 50)

print(PlayerCharacter.adding_things(2, 23))
'''


