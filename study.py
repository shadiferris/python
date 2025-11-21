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

with open("dummydata.txt", "r") as file:
    content = file.read(100)
    print(content)