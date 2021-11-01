#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Error and Exception Handling - https://docs.python.org/3.8/tutorial/errors.html


# In[5]:



def add(n1,n2):
    print(n1+n2)


# In[6]:


add(10,20)


# In[7]:


number1 = 10


# In[ ]:


number2 = input("Please provide a number?")


# In[ ]:


add(number1,number2)


# In[ ]:


try: 
    #want to attempt this code may have an error
    result = 10 + 10
    
except:
    print("Hey, looks like you arent adding correctly!")
    
else:
    print("Add went well")
    print("result equals {}" .format(result))


# In[ ]:


#Built in exceptions useful for errors
#https://docs.python.org/3.8/library/exceptions.html#OSError


# In[ ]:


try: 
    f = open('testfile','r')
    f.write("write to test line")
except TypeError:
    #https://docs.python.org/3.8/library/exceptions.html#TypeError
    print('There was a type error')
except OSError:
    #https://docs.python.org/3.8/library/exceptions.html#OSError
    print('There was a OS error')
except:
    print('All other errors')


finally:
    print('i always run')


# In[ ]:


def ask_for_int():
    try:
        result = int(input("Please provide a number: "))
        print("the number you entered is {}" .format(result))
    except:
        print("Whoops, thats not a number")
    finally:
        print("End of try/except/finally")


# In[ ]:


ask_for_int()


# In[ ]:


def ask_for_int2():
    
    while True:
        try:
            result = int(input("Please provide a number: "))
            print("the number you entered is {}" .format(result))
        except:
            print("Whoops, thats not a number")
            continue
        else:
            print("Yes, thank you for the number")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end")


# In[ ]:


ask_for_int2()


# In[ ]:





# In[ ]:


# Errors and Exceptions Homework


# In[ ]:


# Problem 1 - Handle the exception thrown by the code below by using try and except blocks.
#
#for i in ['a','b','c']:
#    print(i**2)


# In[ ]:


try:
    for i in ['a','b','c']:
        print(i**2)
    
except:
    print("Cannot mulitple ")


# In[ ]:


# Problem 2 - Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'


# In[ ]:


try:
    x = 5
    y = 0

    z = x/y


    
except:
    print("division by zero not allowed")
    
finally:
    print("This is the end of the script")


# In[ ]:


# Problem 3 - Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            number = int(input("Please provide a number: "))
            result = number * number
            
            print("Thank you, your number squared is {}" .format(result))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            print("Yes, thank you for the number")
            break      
        


# In[ ]:


ask()


# In[ ]:





# In[ ]:


#Update for Pylist Users 

#Just a quick update on the Pylint library. To see the same report that I do in the video, in the newest version of PyLint 
#you need to add -r y (report yes) at the end of the command, so the full command should be:
# pylint myexample.py -r y

#If you check out the video I only wrote pylint myexample.py , you will need to add on -r y
#Check out the previously answered QA Forum posts if you get stuck on this, thanks!

# pylint simple1.py -r y


# In[ ]:


# Unit testing - can use pylint and unittest


# In[ ]:


#unittest scripts
def cap_text(text):
    return text.title()  # replace .capitalize() with .title()


# In[ ]:


import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
    def test_with_apostrophes(self):
        text = "monty python's flying circus"
        result = cap.cap_text(text)
        self.assertEqual(result, "Monty Python's Flying Circus")
        
if __name__ == '__main__':
    unittest.main()


# In[ ]:


#pylint

"""
A very simple script.
"""

def myfunc():
    """
    An extremely simple function.
    """
    first = 1
    second = 2
    print(first)
    print(second)

myfunc()


# In[ ]:


"""
A very simple script.
"""

def myfunc():
    """
    An extremely simple function.
    """
    first = 1
    second = 2
    print(first)
    print('second')

myfunc()


# In[ ]:




