print("Hello World")

#VARIABLES AND DATA TYPES

# integer
my_integer = 45

#float
my_float = 3.32

# string
my_string = "hello python"

# boolean
my_bool = True

# Operations with integer and flaots
result = my_integer + my_float
print (result)

# concatenation
greeting = my_string + " " + "is awesome!"
print (greeting)

# boolean operator
is_true = my_bool
is_false = not my_bool
print (is_true, is_false)

#CONTROL FLOW

age = 89
if age < 16:
    print("youre minor")
elif age>= 18 and age < 45:
    print("you are an adult")
else:
    print("you re old")

fruits =["apple", "banana", "cherry"]

for milk in fruits:
    print(milk)

# FUNCTIONS
def meat (name):
    print(f"hello,{name}")

meat ("alice")
meat ("bomoku")

#LISTS AND DATA STRUCTURES

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.remove("banana")

print(fruits[0])
print(fruits[2])
print(fruits[1])

for iteration in fruits:
    print(iteration)

# OBJECT-ORIENTED PROGRAMMING
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old.")

person1 = Person("alice", 30)

person1.greet()


print ('I am learning python' [2:5])

# Variable naming

name = "David"
print(name)

name = 'Nok'
print(name)

# section 1 - 12 in another file


# global scope

player_health = 10 #global scope

    def drink_potion():
        potion_strength = 2
        print(player_health)

drink_potion()
print(player_health)








#PYTHON VARIABLES

name = 7890
print(name)

# LEN FUNCTION

print(len('hello'))

#DATA TYPES

# string = pieces of characters between quotation marks

print("hello"[0])

# if you want first character always write zero. everything starts from zero.

print('123' + '456')

# INTEGERS = WHOLE NUMBERS

print(123 + 456)

# FLOATS = numbers with decimals

print(2.4 + 3.4)

# BOOLEANS = true or false

True
False

#TYPE CHECKING AND TYPE CONVERSION

#name = len(input('what is your name)'))
#print(type(name))

# CONVERSION

# name = len(input('what is your name?'))
# new_name = str(name) # this is how you convert the type
# a = str(123)
# print(type(a))

# print('your name has ' + new_name + ' characters.')


#MATHEMATICAL OPERATORS

1 + 4
7 - 8
3 * 2
print(6 / 4)
print(2 ** 3) #2 * 2 * 2 = exponent

#OPERATION PRECEDENCE - PEMDAS LR (computer checks from left to right)

# parentheses ()
# exponents **
# multiplication *
# division /
# addition +
# subtraction -

print(3 * 3 + 3 / 3 - 3)

#NUMBER MANIPULATION AND F-STRINGS IN PYTHON

result = 4 / 2
result /= 2
print(result)

score = 1
height = 1.75
isWinning = True

# F-STRING

print(f"your score is {score},your height is {height}, you are winning is {isWinning}")
# formats all the different data types in a string and outputs in consistent format.
# when you to want integrate variables into strings

#CONTROL FLOW WITH IF/ELSE STATEMENTS AND CONDITIONAL OPERATORS

# print("welcome to the rollercoaster")
# height = int(input("what is your height in cm? "))
#
# if height >= 150:
#     print("you can ride")
# else:
#     print("sorry, you can not ride it, grow a little bit!")

# nested if statements and elif statements
# if statement inside another if statements., nested concept is anywhere, e.g. nested loops, nested lists, etc.

# print("welcome to the rollercoaster")
# height = int(input("what is your height in cm? "))
#
# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("what is your age?"))
#     if age < 12:
#         print("please pay USD 5.")
#     elif age <= 18:
#         print("please pay USD 7.")
#     else:
#         print("please pay USD 12.")
# else:
#     print("sorry, you have to grow taller before you can ride")

####### MULTIPLE IF STATEMENTS IN SUCCESSION ############

# print("welcome to the rollercoaster")
# height = int(input("what is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("what is your age?"))
#
#     if age < 12:
#         bill = 5
#         print("please pay USD 5.")
#     elif age <= 18:
#         bill = 7
#         print("please pay USD 7.")
#     else:
#         bill = 12
#         print("please pay USD 12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N?")               # this is the second if statements, hence multiple if statements
#     if wants_photo == "Y":
#         bill += 3 # same as bill = bill + 3, abbreviation
#
#     print(f"your final bill is {bill}")
#
# else:
#     print("sorry, you have to grow taller before you can ride")

#LOGICAL OPERATORS AND, OR AND AND NOT (useful for checking different conditions)


# print("welcome to the rollercoaster")
# height = int(input("what is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("what is your age?"))
#
#     if age < 12:
#         bill = 5
#         print("please pay USD 5.")
#     elif age <= 18:
#         bill = 7
#         print("please pay USD 7.")
#     elif age >= 45 and  age <= 55:            # that is an example of a logical operator
#         print("everything is gonna be ok, have a free ride on us")
#     else:
#         bill = 12
#         print("please pay USD 12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N?")               # this is the second if statements, hence multiple if statements
#     if wants_photo == "Y":
#         bill += 3 # same as bill = bill + 3, abbreviation
#
#     print(f"your final bill is {bill}")
#
# else:
#     print("sorry, you have to grow taller before you can ride")

# RANDOM MODULE

# import random
#
# random_integer = random.randint(1,2000) # to print a random integer between value 1 and 2000
# print(random_integer)
#
# random_float = random.random()
# print(random_float)

################UNDERSTAND OFFSET AND APPENDING ITEMS TO LISTS################

states_of_america = ['Delaware', 'California', 'New York', 'Texas']

print(states_of_america[0:4])
print(states_of_america[-3:])

states_of_america.append("Kokoland") # to add one single value to the list

print(states_of_america)
print(states_of_america[-3:])

states_of_america.extend(["Momoland", "Mimiland", "Lululand"]) # to add a list to the list
print(states_of_america)

# ERRORS AND WORKING WITH NESTED LISTS

# note: most common error is index out of range


fruits = ["strawberry", "apple", "banana"]
vegetables = ["spinach", "tomato", "potatoes"]

pesticide_food = [fruits, vegetables] # this is a nested list
print(pesticide_food)

#USING THE FOR LOOP WITH LISTS, it does something to each item

fruits = ["strawberry", "apple", "banana"]
for fruit in fruits: # to print each single fruit, assigns a variable(fruit) to the fruits in the list
    print(fruit)
    print(fruit + " pie")

# FOR LOOPS AND THE RANGE() function 

for number in range(1, 31): # that's how it prints 30 numbers, by adding one more than 30.
    print(number)


for number in range(1, 31, 3): # making steps of 3 until 30 is reached
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

#DEFINING AND CALLING FUNCTIONS

def my_function(): #colon says that everything after it belongs to the function
    print("hello")
    print("bye")

my_function() # to call the function

# indentation (shifted to the right by four spaces) below an example of indentation

# def my_function():    # note this code does not work, it is just an example
#     if sky =="clear":
#         print("blue")
#     elif sky == "cloudy":
#         print("grey")
#     print("hello")

#WHILE loops, continue running until this condition switches to false. a condition has to become false. attention that
# it wont turn into an infinite loop.

# while not at_goal(): # refers to the robot example
#     jump()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

#FUNCTIONS WITH INPUTS

# SIMPLE FUNCTION 

def greet():
    print("Hello Rebecca")
    print("How are u don?")
    print("isnt the weather nice today?")
greet()

# FUNCTION THAT ALLOWS FOR INPUT

def greet_with_name(name):
    print(f"hello {name}")    # why does this have to be an f string?
    print(f"how do you do {name}?")

greet_with_name("Alexis")

#POSITIONAL VS. KEYWORD ARGUMENTS

def greet_with(name, location):   # that is a positional argument because it will run based on its order.
    print(f"hello {name}")
    print(f"What is it like in {location}")

greet_with(name="john",location="new york") # that is a keyword argument because its specified by name
# you have to specify name and location when calling the function, when u wanna make it a keyword.

#THE PYTHON DICTIONARY # PROGRAM INSTRUCTIONS FOR COMPUTERS

programming_dictionary = {
    "Bug": "an error in a program that prevents the program from runninig as expected.",
    "Function": "a piece of code that you can easily call over and over again.",
    "Loop": "the action of doing something over and over again",
}
# BUG, FUNCTION, LOOP ARE KEYS, AFTER COLON COMES THE VALUE.


#RETRIEVING ITEMS FROM DICTIONARY

print(programming_dictionary["Bug"])

# CREATING AN EMPTY DICTIONARY
empty_dictionary = {}

#WIPE AN EXISTING DICTIONARY
programming_dictionary = {}
print(programming_dictionary)


#NESTING LISTS AND DICTIONARIES

#DIFFERENCE BETWEEN NESTING AND NESTING LIST IN DICTIONARY

#nesting

capitals = {
    "france": "paris, ",
    "germany": "berlin",
}
print(capitals)

travel_log = { # note france is key, paris is value, separated by colon.
    "france": ["paris", "marseille", "dijon"],
    "germany": ["hamburg", "berlin", "stuttgart"],
}

print(travel_log)


#FUNCTIONS WITH OUTPUTS

def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name("DaViDovSkI", "buBuU"))

#MULTIPLE RETURN VALUES

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
      return "you didnt provide valid inputs"
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name(input("what is ur first name?"),
input("what is ur lats name?")))

#DOCSTRINGS

#use three quotation marks to document something.
"""The function will take first and last name and format it"""

#PRINT VS. RETURN

# Use print when you want to show a value to a human. return is a keyword.
# When a return statement is reached, Python will stop the execution of the current function,
# sending a value out to where the function was called.
# Use return when you want to send a value from one point in your code to another.


#FLAGS (BOOLEAN VALUES)


# Initialize a flag, boolean variable that signals whether a condition is met or not.
condition_met = False

# Simulate some code where the condition is met
# In a real program, this might be a more complex condition or event
# if some_condition():
#     condition_met = True
#
# # Check the flag and take action accordingly
# if condition_met:
#     print("The condition is met!")
# else:
#     print("The condition is not met.")

#LOCAL VS. GLOBAL SCOPE

#SCOPE

enemies = 10

def increase_enemies():
    enemies = 100
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)

#global variable

player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()

# global variable is a variable declared outside of any function or block of code,
# making it accessible throughout the entire program. On the other hand,
# a local variable is declared within a specific function or block of code and is only accessible within that scope.

#HOW TO MODIFY A GLOBAL VARIABLE

#you probably dont want to do this coz it makes no sense. bitch.

#PYTHON CONSTANTS AND GLOBAL SCOPE

# global scope very useful when defining constants, e.g.

pi = 3.14159
print(pi)

URL = "https://www.google.com"
def calc():

# DEBUGGING

# analyze the code, reproduce the bug, evaluate each line, fixing red underline errors,
# use a debugger, try the thonny IDE for writing python code. a good debugger is: pythontutor.com
# ask stackoverflow
