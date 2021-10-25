#!/usr/bin/env python
# coding: utf-8

# In[158]:


#Attribues and Class Keywords


# In[166]:


mylist = [1,2,3]


# In[168]:


#hit tab to view other attributes and methods
mylist


# In[169]:


myset = set()


# In[170]:


#type(mylist)
type(myset)


# In[171]:


class Sample():
    pass


# In[172]:


my_sample = Sample()


# In[173]:


type(my_sample)


# In[174]:


class Dog():
    
    def __init__(self,breed,name,spots):
        
        #Atrribues
        # we take in the argument
        #assing it using self.atteribute_name
        self.breed = breed
        self.name = name
        
        #expect boolean true/false
        self.spots = spots
        
        


# In[175]:


my_dog = Dog(breed='Lab', name='Sam', spots=False)


# In[176]:


type(my_dog)


# In[177]:


my_dog.breed
#my_dog.name
#my_dog.spots


# In[178]:


#Class Object Attributes and Methods


# In[179]:


class Dog():
    
    #class object attribnutes
    #same for any instance of a class
    
    species = 'mammal'
    
    
    
    def __init__(self,breed,name):
        
        #Atrribues
        # we take in the argument
        #assing it using self.atteribute_name
        self.breed = breed
        self.name = name

    #operations/actions ---> Methods
    def bark(self,number):
        
        print("WOOF!! My name is {} and the number is {}".format(self.name,number))
        #can remove number from the above method and it will also run


# In[180]:


type(my_dog)


# In[181]:


my_dog = Dog('Lab','Sam')


# In[182]:


#my_dog.breed
my_dog.name


# In[183]:


my_dog.bark(100)


# In[ ]:





# In[ ]:





# In[184]:


class Circle():
    
    #class object attribute
    
    pi = 3.14
    
    #radius=1 is the default value
    def __init__(self,radius=1):
        
        self.radius = radius
        self.area = radius*radius*self.pi
        
        
    #Method    
    def get_circumference(self):
        return self.radius * self.pi * 2


# In[185]:


#change the value for the calculations
my_circle = Circle(10)


# In[186]:


my_circle.pi


# In[187]:


my_circle.radius


# In[188]:


my_circle.get_circumference()


# In[189]:


my_circle.area


# In[190]:


#Inheritence and Polymorphism


# In[191]:


#Inheritence 

class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        

    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")


# In[192]:


class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
        
    def eat(self):
        print("I am a dog eating")

    def bark(self):
        print("WOOF!!!")


# In[193]:


mydog = Dog()


# In[194]:


mydog.eat()


# In[195]:


mydog.who_am_i()


# In[196]:


mydog.bark()


# In[197]:


myanimal = Animal()


# In[198]:


myanimal.eat()


# In[199]:


myanimal.who_am_i()


# In[200]:


#Polymorphism


# In[201]:


class Dog():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says woof!"


# In[202]:


class Cat():
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        return self.name + " says meow!"


# In[203]:


niko = Dog("niko")
felix = Cat("felix")


# In[204]:


print(niko.speak())


# In[205]:


print(felix.speak())


# In[206]:


for pet in [niko,felix]:

    print(type(pet))
    print(pet.speak())


# In[207]:


def pet_speak(pet):
    print(pet.speak())


# In[208]:


pet_speak(niko)


# In[209]:


pet_speak(felix)


# In[210]:


class Animal():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# In[211]:


class Dog(Animal):
    
    def speak(self):
        return self.name+ " says woof!!!"


# In[212]:


class Cat(Animal):
    
    def speak(self):
        return self.name+ " says meow!!!"


# In[213]:


fido = Dog("Fido")


# In[214]:


ling = Cat("Ling")


# In[215]:


fido.speak()


# In[216]:


ling.speak()


# In[217]:


#Special (magic/dunder) Methods


# In[218]:


mylist = [1,2,3]


# In[219]:


len(mylist)


# In[220]:


class Sample():
    pass


# In[221]:


sample = Sample()


# In[222]:


print(sample)


# In[223]:


print(mylist)


# In[224]:


class Book():
    
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages
    
    #return string format of the title and author name in str()
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    #return the length of the book in len()
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")


# In[225]:


b = Book('Python Rocks','Jose',200)


# In[226]:


print(b)


# In[227]:


str(b)


# In[228]:


len(b)


# In[229]:


del b


# In[230]:


b


# In[231]:


#Homework Execise


# In[232]:


#Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return (((self.coor2[0]-self.coor1[0])**2) + ((self.coor2[1]-self.coor1[1])**2))**(0.5)
    
    def slope(self):
        return (self.coor2[1]-self.coor1[1]) / (self.coor2[0]-self.coor1[0])


# In[233]:


coor1 = (3,2)
coor2 = (8,10)

li = Line(coor1,coor2)


# In[234]:


li.distance()


# In[235]:


li.slope()


# In[236]:


##Fill in the Line class methods for cylinder

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (3.14*(self.radius)**2)*self.height
    
    def surface_area(self):
        return (2 * (3.14 *(self.radius**2))) + (2 * (3.14 *(self.height*self.radius)))


# In[237]:


c = Cylinder(2,3)


# In[238]:


c.volume()


# In[239]:


c.surface_area()


# In[240]:


#For this challenge, create a bank account class that has two attributes:

#    owner
#    balance

#and two methods:

#    deposit
#    withdraw

#As an added requirement, withdrawals may not exceed the available balance.

#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


# In[241]:


class Simple():
    
        def __init__(self,value):
            self.value = value
        
        def add_to_value(self,amount):
            self.value = self.value + amount
            print('we just added {} to your value'.format(amount))


# In[242]:


myobj = Simple(300)


# In[243]:


myobj.value


# In[244]:


myobj.add_to_value(500)


# In[245]:


myobj.value


# In[263]:


class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    #def acct1():
    #    print('Account balance: {}'.format(self.balance))
    #    print('Account Owner: {}'.format(self.owner))
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print('Deposit Accepted')
        print('Account balance: {}'.format(self.balance))
        print('Account Owner: {}'.format(self.owner))
    
    def withdraw(self,amount):
        self.balance = self.balance - amount
        
        if amount > self.balance:
            print('Funds Unavailable!!!')
        else:
            print('Withdraw Accepted')
            print('Account balance: {}'.format(self.balance))
            print('Account Owner: {}'.format(self.owner))
    
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: ${self.balance}"


# In[264]:


acct1 = Account('Jose',100)


# In[265]:


acct1.balance


# In[266]:


print(acct1)


# In[267]:


acct1.owner


# In[268]:


acct1.balance


# In[269]:


acct1.deposit(50)


# In[270]:


acct1.withdraw(75)


# In[271]:


acct1.withdraw(500)


# In[ ]:





# In[ ]:




