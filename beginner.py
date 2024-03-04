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

### beginner2


na = 'abc'
print(na)

# i am learning python
# python am i learning

# int
# float
# string
# bool

55.67777

10 ** 2

10 // 2

10 % 3

(10 + 2) * 5

# import math
# math.

'i am learning python'[0:7:2]

for cat in range(4000, 4200, 50):
    print(cat)
    print('---------')

for key, value in {'name': 'david',
                   'learning': 'python'}.items():
    print(key, value)

while 2 > 4 and 5 < 9 or 4 == 9 and 4 > 90:
    print('abc')

while len('khaled') < int(input('Enter a Number: ')):
    print('abc')

string = 'Muhammad'
id(string)

# Memory Allocation in Bytes/ Memory consumption

a = 9000000000

import sys

sys.getsizeof(a)

s = 'Car'
s[::-1][::-1]

name = 'Muhammad khaled'
name[::1]

s = 'Car'

print(s == s[::-1][::-1])
print(s is s[::-1][::-1])

'k' not in 'ok'

# String Functions

s = 'We are learning python aaaa python'
# s.upper()
s.title()
s.capitalize()
s.split('a')
s.partition('a')
s.zfill(50)
s.center(50, '-')
s.replace('python', 'java')
s.count('a', 9)
s.endswith(' aa')
s.startswith('W')
s.index('python')

len(s)

s = 'Myageis30'
s.isdigit()
s.isalnum()

# BUILT-IN FUNCTIONS / UNIVERSAL Functions

# print
# range
# str
# tuple
# set
# dict
# list
# max

'abc' * 70

strOne = str("pynative")
strTwo = "pynative"
print(strOne == strTwo)
print(strOne is strTwo)

s = 'My name is Hamza'
s.replace('Hamza', 'Muhammad')
s

name = 'Muhammad'
age = 30

print('My name is ' + name + ' age is ' + str(age))
print(f'My name is {name:-^40} age is {age}')
print('My name is {0:-^40} age is {1}'.format(name, age))
print('My name is', name, 'age is', age)

# f-string or formatted string
name = 'Allah'
f'{name:-^30}'

num = 128971239.190827380912738901
f'{num:_.3f}'

# excape sequence example
print(f'My name\\t is Pasquale \\nI am learning python')

# r-string or raw string
print(r'My name is John \nI am learning python')

# string literals
# \n and \t are string literals
# \n NEWLINE
# \t TAB SPACE
# \ is an escape sequence

'abcdefghi'[::-3]

'foobar'[::-1][-1]

'foobar'[::5]

# https://realpython.com/quizzes/python-strings/viewer/

# strings
# list, tuple and set
# conditionals
# loops
# functions

# LC lambda map zip NLC Dictionaries

# OOP FH DB

'abcda'.count('a', 2)

"""------------------TOPIC **LIST** STARTS HERE----------------------"""

# string
# dictionary
# list

listA = [1, 2, 3, 4, 5]
listB = ['apple', 'mango', 'orange']
listC = [22, 45, 67, 'abc', 'xyz', True, 78.9999]
listD = [True, False, True, True]
listE = [33, 67, 44, [1, [2, 3]], 'apple', ['🍎🍏', '🥭']]

listB = ['apple', 'mango', 'orange']
listB[1][1: 5]

listE = [33, 67, 44, [1, [2, 3]], 'apple', [['🍎🍏', [56, '90']], '🥭']]
listE[5][0][1][1][0]

listE = [33, 67, '44', 3, [1, [2, 3]], 5, ['apple', [3, 'print me']], 'abc', 8]

listB = ['apple', 'mango', 'orange']
# listB.extend([4000])
# listB.pop(0)
# del listB[1]
# del listB
# listB.clear()
# listB.reverse()
# listB.insert(1,987678987)
listB[1:1] = ['908', 44, 55, 66]
listB

# Datastructures and Algorithms

# Amazon --> 5 Billion.  0.001s

# 1,2,3,4,5,6,7,9,10,11,12,13,14

listE = [33, 67, '44', 3, [1, [2, 3]], 5, ['apple', [3, 'print me']], 'abc', 8]
listE[4][1].append(4)
listE

# copy
# list
a = [1, 2, 3]
b = list(a)

a.append(10)
b

# tuple

tupleA = 3, 4, [5, 6, 67], 7, 9, 0
tupleA[2].append(9000)
tupleA

a, b, c, d = (5, 78, 9, 3)

b

type((1,))

'apple'

1, 2, 3, 4

[1, 2] * 8

'a' * 40

a

name = 'Khaled'
nam

print('Khaled'

10 / 0

a = 10
a + '9'

try:
    10 / 0
except Exception as e:
    print(e)

a = 'abc'
a[:] is a

print(id(a[:]))
print(id(a))

l = [1, 2, 3, 4, 5]
l[2:2] = [100, 200]
l

a = ['a', 'b', 'c']

a.extend(['d', 'e'])
a

# conditionals

if 2 > 10:
    print('Muhammad')
elif 'abc' == 'abc':
    print('Muhammad KhAlEd')
elif 'abc' == 'abc':
    print('Muhammad Khaled')
else:
    print('abc')

# Assignment Operators
# =
# +=
# -=
# *=
# /=

# comparison
# ==
# !=
# >
# <
# >=
# <=

# Logical Operators
# and
# or
# not

3 <= 3

4 == 4

3 != 3

30 >= 2 or 5 > 30

not 3 == 3

# Nested if else

if 300 > 20:
    if 4 < 5:
        if 3 == 3:
            if 5 != 90:
                print('k')
            else:
                print('k')

        else:
            print('k')
    else:
        print('k')

a = 10
b = 20
c = 30

if a == 10:
    if b == 20:
        pass

if 2 > 1 and 5 < 10 or 5 == 5:
    pass

2 > 1 and 5 < 10 or 5 == 5

number = 3 if 4 == 4 else 30

number

# Loop - for loop and while loop

for cat in range(5, 10, 2):
    print(cat)

for cat in 'abc':
    print(cat)

for cat in [22, 33, 44, 55, 66]:
    print(cat)

for cat in '45':
    print(cat)

for x in range(3):
    print('outer loop')
    for y in range(5):
        print('---------inner loop')

a = 4
b = 0
while a < 10 and b < 2:
    print('cool')
    a += 1
    b += 1

# break continue pass
for i in range(10):
    if i == 6:
        continue
    print(i)

for i in range(10):
    pass


def sum(a, b=80):
    c = a + b
    return c


sum(b=7, a=100)

sum(30, 8)

sum(55, 89)

print('Muhammad')


# Function
# 1 Built in
# print
# range
# len
# list
# tuple
# set
# max
# str
# int

# 2 User Defined
# def
# lambda (In-line Function)

# (lambda a,b : a+b) (2,3)

# positional and keyword

def sum(*args, **kwargs):
    print(args)
    print(kwargs)


sum(4, 5, 6, 7, 78, 8, 89, 9, 0, 0, 0, 4, 4, 3, 3, 4, 5, 67, 7, a=90, b=80, c=8)


def a():
    print('i am called from outside')

    def b():
        print('i am called from a')

    b()


a()


def a():
    print('i am called from outside')
    return 'abc', 12, 23, 14


print(a())
