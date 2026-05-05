'''
def sum(num1, num2):
    return num1 - num2

num1 = int(input("give me a number? "))
num2 = int(input("give me another number? "))

total = sum(num1, num2)
print(f"total is {total}")
'''

'''
def checkdriverage():
    age = int(input("what is your age? "))
    if age < 18:
        print("you are too young to drive today")
    elif age >= 18 and age <= 65:
        print("You can hold a drivers license!!!")
    else:
        print("you are too old to have a license")

checkdriverage()

'''
'''
with open("dummydata.txt", "r") as file:
    content = file.readlines()
#print(content)

count = 0
for line in content:
    if "error" in line.lower():
        count = count + 1
print(count)
'''

'''
with open("dummydata.txt", "r") as file:
    content = file.read()
#print(content)

for line in content:
    print(line.readline())
'''
'''
with open("dummydata.txt", "r") as file:
    content = file.read(1000)
    print(content)

'''

'''
def append_to_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + '\n')

append_to_file("dummydata.txt", " helloworld123")

'''
'''
def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines() # or read()

#count = 0

for line in read_file("dummydata.txt"):
  print(line)
  #print(len(line))
  #new_line = line.strip()
  #print(new_line)
  #  if "warning" in line:
  #      count += 1

#print(f"number of texts present is {count}")

'''
'''
n = 0
print("n = ", n)
n = "abc"
print("n = ", n)

n, m = 0, "abc"
print(n)
print(m)

n = n + 1

n =+ 1

print(n)
n = 4
if n > 1:
    n +=1
    print("n is now ", n)
elif n < 1:
    print("hello world")

m = 100
if m > 2 and m < 8:
    print("this is m", m)
elif m == 10 or m ==100:
    print("this is a big number")
else:
    print("No number today")

x = 0

while x < 5:
    print(x)
    x += 1

y = 0
print("space here")

for y in range(5,1, -1):
    print(y)


x = 5
y = 2

print(x / y)

print(x // y)

print(int(x / y))

print( x % y)

import math
print(math.floor(5 / 2))
print(math.ceil( 11 / 2))
print(math.sqrt( 4))
print(math.pow(2, 3))



import math

print(math.pow(2, 200))

print(math.pow(2, 200))

arr = [1,2,3]

print(arr[0])
arr.append(4)

print(arr)
arr.pop(2)
print(arr)
arr.insert(1, 7)
print(arr)
arr[0] = 100
print(arr)
arr[3] = 123456
print(arr)


n = 5
arr = [1] * n

print(arr)
print(len(arr))
print(arr[-1])

arr = [1,2,3,4,5,6,7,8]
print(arr[::-1])


for i in range(len(arr)):
    print(arr[i])

for n in arr:
    print(n)

for i, n in enumerate(arr):
    print(i, n)

for i, n in enumerate(range(10)):
    print(i, n)


num1 = [1, 2, 3]
num2 = [3,4,5]

num3 = num1[0] + num2[2]
print(num3)

for i in zip(num1, num2):
    print(i)

nums=[1,2,3]
nums.reverse()

print(nums)

sorted = [1,4,6,3,7,2,9,0]
sorted.sort(reverse=True)
sorted.sort()

print(sorted)

strings = ["john Joe" , "anne li", "frank Ferris", "lucas bucas"]
strings.sort()
print(strings)

#custom sort by length of string
strings.sort(key=lambda x: len(x))

print(strings)

'''
'''

array = [i for i in range(10)]
print(array)

new_string = "Hello world"
print(new_string[2:3])

print(int(123) + int(123))
print(str(123) + str(123))


string = ["ab" , "cd" , "ef"]
string2 = ['python']
print("".join(string))
print(' - '.join(string2))

#sets 
myset = set()
set2 =set()
myset.add(1)
myset.add(2)
set2.add(1)
set2.add(3)
print(myset)
print(set2)
set3 = myset.difference(set2)
print(set3)
print(len(set3))
print(1 in myset)
print(10 in myset)

my_set_2 = {i for i in range(5)}
print(my_set_2)

#hashmaps / Dictionaries

mymap ={}
mymap["joseph"] = 7
mymap["frank"] = 9
mymap["lucas"] = 5

print(mymap)
print(len(mymap))
mymap["frank"] = 10
mymap["Milia"] = 21

print('joseph' in mymap)
print(mymap)
mymap.pop("Milia")
print(mymap)

for key in mymap.keys():
    print(key)
for value in mymap.values():
    print(value)

'''
# tuples
'''

tup = (1, 2, 3)
print(tup)

#functions
def myfunc(n,m):
    return n * m

print(myfunc(4, 5))

def outer(a, b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))
'''
# classes

class myclass:
    #constructor
    def __init__(self, nums):
        #create member variables
        self.nums = nums
        self.size = len(nums)

    #self key work requires as param
    def getlength(self):
        return self.size
    
    def getDouble(self):
        return 2 * self.getlength()


nums = [1, 2, 3, 4]

obj = myclass(nums)   # create instance

print(obj.getlength())   # 4
print(obj.getDouble())   # 8

search_key = "INFO"
'''

with open("dummydata.txt", "r") as f:
    for line in f:
        if search_key in line:
            print(line)


count = 0
with open("dummydata.txt", "r") as f:
    for line in f:
        if search_key in line:
            count += 1
print(count)
'''
'''
search_key = "INFO"

with open("dummydata.txt") as f:
    for line in f:
        if search_key in line:
            parts = line.split()
            print(parts)
'''
'''
count = {}
with open("dummydata.txt") as f:
    for line in f:
        words = line.split()

        for word in words:
            #if "error" in words:
                count[word] = count.get(word,0) + 1

print(count)

count = {}
with open("process.txt") as f:
    for line in f:
        words = line.split()

        for word in words:
            #if "error" in words:
                count[word] = count.get(word,0) + 1

print(count)
'''
'''
string = input("What is your name? " )
char_num = len(string)
if (char_num % 2) == 0:
   message = "Hello " +string + ", your name is even!"
else:
   message = "Hello " +string + ", your name is odd!"

for i in range(char_num):
  print(message)
'''
'''

search_key = "INFO"

with open("dummydata.txt") as f:
    for line in f:
        if search_key in line:
            parts = line.split()
            print(parts[3])

if parts[3] == "Current" or parts[3] == "Initializing":
    print("helloworld123")
elif parts[3] == 'ERROR':
    print("this is the end")
'''

        








        