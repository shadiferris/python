#PYTHON DECORATORS

def func():

    return 1

func()

1

def hello():

    return "hello!!!"

hello

<function __main__.hello()>

greet = hello

greet()

'hello!!!'

hello()

'hello!!!'

del hello

hello()

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-139-a75d7781aaeb> in <module>
----> 1 hello()

NameError: name 'hello' is not defined

greet()

'hello!!!'

def hello(name='Jose'):

    print('The hello() function has been executed')

    

    def greet():

        return '\t This is the greet() func inside hello!!'

    

    def welcome():

        return '\t This is the welcome() func inside hello!!'

​

    

    print(greet())

    print(welcome())

    print("This is the end of the hello function")

hello()

The hello() function has been executed
	 This is the greet() func inside hello!!
	 This is the welcome() func inside hello!!
This is the end of the hello function

def hello(name='Jose'):

    print('The hello() function has been executed')

    

    def greet():

        return '\t This is the greet() func inside hello!!'

    

    def welcome():

        return '\t This is the welcome() func inside hello!!'

​

    

    print("Im going to return a function")

    

    if name == 'Jose':

        return greet

    else:

        return welcome

my_new_func = hello('Jose')

The hello() function has been executed
Im going to return a function

print(my_new_func())

	 This is the greet() func inside hello!!

​

def hello():

    return 'Hi Jose!'

def other(some_def_func):

    

    print('Other code runs here')

    print(some_def_func())

#running the function hello() within the other() function

other(hello)

Other code runs here
Hi Jose!

​

def new_decorator(original_func):

    

    def wrap_func():

        

        print('Some extra code, before original function')

        

        original_func()

        

        print('Some extra code, after original function')

        

    return wrap_func()

@new_decorator

def func_needs_decorator():

    print("This function is in need of a Decorator")

Some extra code, before original function
This function is in need of a Decorator
Some extra code, after original function

func_needs_decorator()

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-58-ce136c761ae1> in <module>
----> 1 func_needs_decorator()

TypeError: 'NoneType' object is not callable

# Reassign func_needs_decorator

func_needs_decorator = new_decorator(func_needs_decorator)

​

Some extra code, before original function

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-59-fd09f6a256df> in <module>
      1 # Reassign func_needs_decorator
----> 2 func_needs_decorator = new_decorator(func_needs_decorator)

<ipython-input-39-bbb3b6cdfb59> in new_decorator(original_func)
      9         print('Some extra code, after original function')
     10 
---> 11     return wrap_func()

<ipython-input-39-bbb3b6cdfb59> in wrap_func()
      5         print('Some extra code, before original function')
      6 
----> 7         original_func()
      8 
      9         print('Some extra code, after original function')

TypeError: 'NoneType' object is not callable

func_needs_decorator()

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-60-ce136c761ae1> in <module>
----> 1 func_needs_decorator()

TypeError: 'NoneType' object is not callable

decorated_func()

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-52-1aea9b2206a1> in <module>
----> 1 decorated_func()

TypeError: 'NoneType' object is not callable

