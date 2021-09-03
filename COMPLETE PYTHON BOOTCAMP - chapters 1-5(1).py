#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hlloworld')


# cool
# 

# Variable Assignments

# In[4]:


my_dog = 2


# In[5]:


a = 5


# In[6]:


a


# In[7]:


a =10


# In[8]:


a


# In[9]:


a + a 


# In[10]:


a = a + a


# In[11]:


a


# In[12]:


a = a + a


# In[13]:


a


# In[15]:


type(a)


# In[1]:


a


# In[8]:


my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate


# In[7]:


my_taxes


# In[9]:


print(my_taxes)


# Strings

# In[10]:


'hello'


# In[11]:


"world"


# In[12]:


"This is a string"


# In[14]:


print("hello world1")
print("hello world2")


# In[18]:


print("hello \tworld")


# In[19]:


len('hello')


# String Indexing and slicing

# In[20]:


mystring =  "hello world"


# In[21]:


mystring


# In[26]:


mystring[-4]


# In[28]:


mystring = "abcdefghijk"


# In[29]:


mystring[2:]


# In[30]:


mystring[:3]


# In[34]:


mystring[1:3]


# In[40]:


mystring[2:7:2]


# In[41]:


mystring[::-1]


# In[43]:


mystring2 = 'Hello World'


# In[45]:


mystring2[8]


# In[46]:


string2 = "tinker"


# In[48]:


string2[1:4]


# Immutibility - string properties and Methods

# In[49]:


name = "Sam"


# In[52]:


name[1:]


# In[53]:


last_letters = name[1:]


# In[54]:


last_letters


# In[55]:


'P' + last_letters


# In[62]:


x = 'Hello world'


# In[63]:


x = x + ' isnt it beautiful outside today'


# In[64]:


x


# In[1]:


letters = 'z'


# In[2]:


letters * 10


# In[5]:


'2' + '3'


# In[6]:


x = "hello world"


# In[9]:


x.split()


# In[8]:


x


# Print formating with strings

# In[10]:


my_name = "john"


# In[11]:


print("hello" + my_name)


# In[13]:


print('this is a {} string '.format('INSERTED'))


# In[14]:


print('The {} {} {}'.format('help', 'me', 'out'))


# In[15]:


print('The {2} {0} {1}'.format('help', 'me', 'out'))


# In[19]:


print('The {0} {0} {0}'.format('fox', 'me', 'out'))


# In[18]:


print('The {a} {c} {b}'.format(a='help', b='me', c='out'))


# In[34]:


result = 1200/777


# In[35]:


result


# In[36]:


print("the result is {}".format(result))


# In[37]:


print("the result is {r}".format(r=result))


# In[41]:


print("the result is {r:10.3f}".format(r=result))


# In[42]:


name = "john"


# In[48]:


print(f'my name is {name}')


# In[50]:


age = 5
height = 180


# In[51]:


print(f'My name is {name} and I am {age} years old. I am currently {height}cm tall')


# Lists in Python

# In[24]:


my_list = [1,2,3]


# In[25]:


my_list_1 = ['string', 100, 23.4, 5]


# In[26]:


len(my_list_1)


# slice a list

# In[27]:


my_list_1[0:]


# In[28]:


another_list = ['helloworld', "combine"]


# In[29]:


my_list + another_list


# In[30]:


final_list = my_list + another_list


# In[11]:


final_list


# In[12]:


#changing values within a list
final_list[0] = 'ALLLLL CAPS'


# In[13]:


final_list


# In[14]:


#adding/appending new item to a list
final_list.append('New')


# In[15]:


final_list


# In[16]:


final_list.count(5)


# In[17]:


final_list.append('seven')


# In[18]:


final_list


# In[19]:


#to remove an item from a list
final_list.pop()


# In[20]:


popped_item = final_list.pop()


# In[21]:


popped_item


# In[22]:


#to remove an item from a list
final_list.pop(0)


# In[26]:


alpha = ['a', 'e' , 'd', 'g' , 'b']
number = [1, 3, 89, 2, 68, 44]


# In[27]:


#order a list
alpha.sort()


# In[28]:


alpha


# In[31]:


#order a list in reverse
number.reverse()


# In[32]:


number


# Dictionaries

# In[37]:


my_dict = {'key1':'value1','key2':'value2'}


# In[38]:


my_dict['key1']


# In[44]:


price_lookup ={'apples':1.50,'orange':3.4}


# In[46]:


price_lookup['apples']


# In[47]:


my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}


# tuples

# In[48]:


t = (1,2,3)


# In[49]:


mylist = [1,2,3]


# In[50]:


type(t)


# In[51]:


type(mylist)


# In[54]:


mylist[0] = 'NEW'


# In[56]:


mylist


# In[57]:


t[0] ='NEW'


# In[ ]:


t


# Sets 

# In[1]:


myset = set()


# In[2]:


myset


# In[3]:


myset.add(1)


# In[4]:


myset


# In[5]:


myset.add(2)


# In[6]:


myset


# In[7]:


myset.add(2)


# In[8]:


myset


# In[9]:


mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]


# In[10]:


set(mylist)


# BOOLEANS

# In[13]:


True


# In[14]:


False


# In[15]:


type(False)


# In[16]:


1 > 2


# In[18]:


2 == 2


# In[21]:


b = None


# Input / Output FILES

# In[1]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'Hello this is a text file\nhello world\nwhat is going on today')


# In[2]:


myfile = open('myfile.txt')


# In[5]:


myfile.read()


# In[15]:


myfile.seek(0)


# In[14]:


#reading file
myfile.read()


# In[16]:


contents = myfile.read()


# In[17]:


contents


# In[18]:


myfile.seek(0)


# In[19]:


myfile.readlines()


# In[21]:


#closing file
myfile.close()


# In[25]:


with open('myfile.txt') as my_new_file:
    contents = my_new_file.readlines()


# In[26]:


contents


# In[30]:


#SHIFT + TAB option at the beginning of the first brackets 
#allows you to view more options 
with open('myfile.txt', mode='r' ) as my_new_file:
    contents = my_new_file.readlines()


# In[31]:


contents


# In[33]:


with open('myfile.txt', mode='w' ) as my_new_file:
    contents = my_new_file.readlines()


# 00 - Objects and Data Structures Assessment Test

# In[1]:


4 * (6 + 5)


# In[2]:


4 * 6 + 5 


# In[3]:


4 + 6 * 5


# In[4]:


a =  3 + 1.5 + 4


# In[5]:


type(a)


# In[18]:


#square root
100 ** 0.5


# In[21]:


#square
10 ** 3


# In[22]:


s = 'hello'
s[1]


# In[31]:


s[::-1]


# In[33]:


s[4]


# In[35]:


s[-1]


# In[36]:


list1 = [0,0,0]


# In[37]:


list1


# In[38]:


[0]*3


# Comparison Operators 

# In[1]:


2 == 2


# In[2]:


2 == 4


# In[3]:


2 > 1


# In[4]:


2 >= 5


# In[5]:


2.0 == 2


# In[6]:


2.0=2


# In[10]:


#not equal
3 != 3


# In[8]:


4 != 3


# Chaining Comparison Operators

# if, elif, else Statements
# 

# In[ ]:


#if case1:
#    perform action1
#elif case2:
#    perform action2
#else: 
#    perform action3


# In[ ]:


if True:
    print('It was true!')


# In[ ]:


x = False

if x:
    print('x was True!')
else:
    print('I will be printed in any case where x is not true')


# In[ ]:


loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print('Where are you?')


# In[ ]:


person = 'Sammy'

if person == 'Sammy':
    print('Welcome Sammy!')
else:
    print("Welcome, what's your name?")


# In[2]:


person = 'George'

if person == 'Sammy':
    print('Welcome Sammy!')
elif person =='George':
    print('Welcome George!')
else:
    print("Welcome, what's your name?")


# In[5]:


2 == 2


# for Loops

# In[6]:


# We'll learn how to automate this sort of list in the next lecture
list1 = [1,2,3,4,5,6,7,8,9,10]


# In[7]:


for num in list1:
    print(num)


# In[11]:


for num in list1:
    #check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')


# In[17]:


list_sum = 0

for num in list1:
    list_sum = list_sum + num

    #print(list_sum)
print(list_sum)


# In[21]:


mystring = 'Hello world'

for i in mystring:
    print(i)


# In[23]:


#tuples for loop
tup = (1,2,3,4,5)

for t in tup:
    print(t)


# In[25]:


# for loop with paired tuples
list2 = [(1,2),(3,4),(5,6)]
for tup in list2:
    print(tup)


# In[29]:


#tuple unpacking example
list2 = [(1,2),(3,4),(5,6)]
for (a,b) in list2:
    print(a)
    print(b)


# In[28]:


#tuple unpacking example
list2 = [(1,2),(3,4),(5,6)]
for a,b in list2:
    print(b)


# In[32]:


#dictionary for loop
d = {'k1':1,'k2':2,'k3':3}

for items in d:
    print(items)


# In[34]:


#dictionary for loop
d = {'k1':1,'k2':2,'k3':3}

for items in d.items():
    print(items)


# In[37]:


d = {'k1':1,'k2':2,'k3':3}

for key,value in d.items():
    print(value)


# While Loops

# In[40]:


#while some_boolean_condition:
#do something
#else
#do something else


# In[4]:


x = 0

while x < 5:
    print (f'The current value of x is {x}')
    ##x = x + 1
    x += 1
else:
    print("X IS NOT LESS THAN 5")


# In[11]:


#how to skip a letter in a for loop
mystring = "sammy"

for letters in mystring:
    if letters == 'm':
        break
    #if letters == 'm':
    #    continue
    print(letters)


# In[18]:


x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1


# Useful Operators 
# 

# In[19]:


#range - pre load numbers


# In[21]:


for num in range(10):
    print(num)


# In[22]:


#range - start from 3, all the way up to 10, not including 10
for num in range(3,10):
    print(num)


# In[32]:


#range - start from 0, all the way up to 10, not including 10. And print every second number
for num in range(0,10, 2):
    print(num)


# In[33]:


#Alternative way to print out range of numbers as seen above
list(range(0,100, 6))


# In[34]:


index_count = 0

for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1


# In[35]:



for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))


# In[38]:


word = 'abcde'

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')


# In[47]:


#zip function, combine two lists together

mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c','d','e']
mylist3 = [100,200,300,400,500]


# In[48]:


zip(mylist1,mylist2)


# In[51]:


list(zip(mylist1,mylist2,mylist3))


# In[50]:


for item in zip(mylist1,mylist2,mylist3):
    print(item)


# In[52]:


#search through lists using the "in" function
'x' in ['x','y','z']


# In[53]:


'x' in [1,2,3]


# In[4]:


string = input("What is your name? " )
char_num = len(string)
if (char_num % 2) == 0:
   message = "Hello " +string + ", your name is even!"
else:
   message = "Hello " +string + ", your name is odd!"

for i in range(char_num):
  print(message)


# In[1]:


mylist = [10,20,30,40,100]


# In[2]:


min(mylist)


# In[3]:


max(mylist)


# In[8]:


from random import shuffle


# In[17]:


mylist = [10,20,30,40,100]


# In[18]:


shuffle(mylist)


# In[19]:


mylist


# In[20]:


from random import randint


# In[22]:


randint(0,100)


# In[23]:


mynum = randint(0,100)


# In[24]:


mynum


# In[25]:


input('Enter Something into this box: ')


# In[ ]:


result = input('favourite number: ')


# In[ ]:


type(result)


# In[ ]:


float(result)


# In[ ]:


#List comprehensions in Python


# In[1]:


mystring = 'hello'


# In[2]:


mylist = []

for letters in mystring: 
    mylist.append(letters)


# In[4]:


print(mylist)


# In[5]:


mylist


# In[6]:


#shortcut version of for loop within a variable


# In[14]:


mylist2 = [letter for letter in mystring]


# In[15]:


mylist2


# In[16]:


mylist3 = [cool for cool in 'mylist']


# In[17]:


mylist3


# In[18]:


mylist4 = [ num for num in range(0,11)]


# In[19]:


mylist4


# In[37]:


mylist5 = [ num**2 for num in range(0,11)]

#Other maths can be performed in the num**2 space


# In[21]:


mylist5


# In[34]:


#squareroots each number and only shows numbers which are even
mylist6 = [x**2 for x in range(0,11) if x%2==0]

#change if x%2==1 if you want odd numbers


# In[35]:


mylist6


# In[39]:


celcius = [0,10,20,35.4]

fahrenheit = [( (9/5)*temp + 32) for temp in celcius]


# In[40]:


fahrenheit


# In[ ]:




