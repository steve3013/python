# OBJECT-ORIENTED PROGRAMMING (OOP) & HOW TO USE OOP, CLASSES AND OBJECTS

class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# dog.py

class Dog:
    pass

# dog.py

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#consult this page for practical examples and explanation: https://realpython.com/python3-object-oriented-programming/

# CONSTRUCTING OBJECTS AND ACCESSING THEIR ATTRIBUTES AND METHODS

from turtle import Turtle, Screen

timmy = Turtle()
#capital t on turtle is called pascal case
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
#object.attribute (data that object holds)

my_screen = Screen()
print(my_screen.canvheight)

#object methods = stuff objects can do.
my_screen.exitonclick()

# HOW TO CREATE AN OWN CLASS IN PYTHON
# WORKING WITH ATTRIBUTES, CLASS CONSTRUCTORS AND THE  __init__() function
# ADDING METHODS TO A CLASS, three in one.

class User:
    #creating a constructor

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        #print("new user being created")
        #initialize attributes


        #defining new method
    def follow(self, user):
        user.followers += 1
        self.following += 1

# whenever a new object of this class is initiated, it must provide the above mentioned two pieces of data, i.e. user_id, username
user_1 = User("001", "john")
user_2 = User("002", "Bunny")


#print(user_1.id)
#print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
#attribute is variable associated with an object
#PascalCase, camelCase, snake_case are very important naming concepts in programming

# IMPORTING MODULES, PACKAGES AND WORK WITH ALIASES

from turtle import Turtle
# module name is turtle, thing in the module is Turtle

from turtle import * #to import everything that is in that module
tim = (Turtle)
tom = (Turtle)
terry = (Turtle)

import turtle as t
# alias t stands for turtle
tim = t.Turtle()

# TUPLES

#my_tuple = (1, 3, 8)
# cant change the value in a tuple
#print(my_tuple[1])
#useful when creating lists which u want to stay constant
#colors are defined by tuples, for instance

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# HIGHER ORDER FUNCTIONS AND EVENT LISTENERS

# you have to be able to listen to events the user does
# for that we use event listeners.

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

# OBJECT STATE AND INSTANCES

#state of attributes
# appearance or state might be attributes
# separate versions of the same object
timmy.color = green
tommy.color = purple

# CLASS INHERITANCE

# inheriting same attributes or behaviour from an existing class.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        #super refers to the superclass (animal)

    def breathe(self):
        super().breathe()
        print("doing this under water.")


    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# HOW TO SLICE LISTS AND TUPLES

piano_keys = ["a", "b", "c", "d", "e"]
print(piano_keys[2:3])
print(piano_keys[:3])
print(piano_keys[0:4:2])
print(piano_keys[::2])
print(piano_keys[::-1])

# OPEN, READ AND WRITE TO FILES USING THE "with" keyword

file = open("my_file.txt")
contents = file.read()
print(contents)

with open("my_file.txt", mode="w") as file:
    #with keyword will automatically close the file after code executes.
    file.write(he likes red bull a lot")

with open("my_file.txt", mode="a") as file:
    file.write("\nhe likes ice cream.")

with open("new_file_test", mode="w") as file:
    file.write("it is cold today.")

# UNDERSTANDING RELATIVE AND ABSOLUTE FILE PATHS

# absolute file path: /root/work/main.py
# relative file path: ../work/main.py
# e.g. : with open("Users/steve/Desktop/my_file.txt") as file:
    #contents = file.read()
    #print(contents)

# WORKING WITH CSV DATA AND PANDAS LIBRARY

# already possessing enough experience working with the PANDAS library and Machine Learning, with reference to python_data_science_projects.

# HOW TO CREATE LISTS USING LIST COMPREHENSION

# What you need inside a list comprehension
# new_list = [new_item for item in list]

numbers= [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Steve"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

names = ["nissi", "dani", "magugu", "worry", "umong", "david"]
short_names = [name.lower() for name in names if len(name) < 6]
long_names = [name.upper() for name in names if len(name) > 6]
print(short_names, long_names)

# HOW TO USE DICTIONARY COMPREHENSION

# new_dict ={new_key:new_value for item in list}

names = ["anio", "miou", "magugu", "worry", "laura", "david"]
import random
students_scores = {student:random.randint(1, 100) for student in names}
#print(students_scores)

passed_students = {students:score for (students, score) in students_scores.items() if score >= 60}
print(passed_students)

#unique to the python language

# HOW TO ITERATE OVER A PANDAS DATAFRAME, not so important unless you work with it

# SETTING DEFAULT VALUES FOR OPTIONAL ARGUMENTS INSIDE A FUNCTION HEADER

#arguments with default values

#def my_function (a=1, b=2, c=3):
    #do this with a
    # then this with b
    # finally this with c

import tkinter

window = tkinter.Tk()
window.title("my first gui program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am just a Label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)

import turtle
from turtle import Screen

tim = turtle.Turtle()
tim.write("Hi, I am nothing, but an insignificant text", font=("Times New Roman", 80, "bold"))

my_screen = Screen()
print(my_screen.canvheight)

#object methods = stuff objects can do.
my_screen.exitonclick()

# ARGS: many positional arguments

def add(*args):
    print(args[5])

    sum = 56
    for n in args:
        sum += n
    return sum

print(add(3, 5, 8, 5,8, 9, 120, 4875, 58585))

# KWARGS: many keyword arguments

def calculate(n, **kwargs):
    print(kwargs)
        # for key, value in kwargs.items():
        #     print(key)
        #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

#self-created class using **kwargs

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Ferrari", model="California", color="Red")
print(my_car.make, my_car.model, my_car.color)


# DYNAMIC TYPING: not impportant at the moment

# CATCHING EXCEPTIONS: THE TRY, CATCH, EXCEPT, FINALLY PATTERN

# FileNotFound Error
# with open("a_simple_nigga_file.txt") as file:
#     file.read()
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["bubu"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something cute is happening")
except KeyError as error_message:
    print(f"The key {error_message} does not exist, be more precise")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File has been closed.")

# KeyError
# a_diction ary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Kiwi"]
# fruit = fruit_list[4]

# TypeError
# text = "abc"
# print(text + 5)

#Catching Exceptions explained

# try: #something that might cause an exception
#
# except: #do this if there was an exception
#
# else: #do this if there were no exceptions
#
# finally: #do this no matter what happens
#

# RAISING OWN EXCEPTIONS

height = float(input("Height: "))
weight = int(input("Weight "))

if height > 3:
    raise ValueError("Human Height shall not be over 3 meters. ")

bmi = weight / height ** 2
print(bmi)

#---------------------------------intermediate_advanced2---------------------------------

# DATETIME MODULE

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

print(day_of_week)

date_of_birth = dt.datetime(year=1963, month=3, day=13, hour=2)
print(date_of_birth)

# PYTHON ANYWHERE TO AUTOMATE PYTHON SCRIPTS

''' go to pythonanywhere.com
upload the script, and enter the section tasks, input the time you want the script to run. '''

# API's

# API request = requesting the data from a page, in our example ISS Current Location
# it is going to come back in JSON format.
#requests module is one of the most popular that the webdevelopers even use.

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

'''response codes:404 does not exist.
1XX: hold on. this is not final
2XX: everything is ok
3XX: go away, no permission.
4XX: you screwed up
5XX: server is down or website is down'''

# TYPING HINTS AND ARROWS IN PYTHON

age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(5):
    print("You may pass")
else:
    print("Pay a fine")

# API AUTHENTICATION


import requests
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "c1c5fb72fcb06ergr869ca12e34d346765875sdfge51ec61c9"

weather_params = {
    "lat": 51.05577,
    "lon": -0.15888,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
print(response.json())

# HTTP POST REQUESTS

#HTTP requests

'''
requests.get(), getting data from the internet
requests.post(), sending data to the internet.
requests.put()
requests.delete()
'''

import requests

USERNAME = "cool_guy"
TOKEN = "48343rejgfn3"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "TOKEN",
    "username": "USERNAME",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "codinggraph1",
    "name": "coding graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"

}
# use header key authentication method

headers = {
    "X-USER-TOKEN": TOKEN
}
# to protect my api from being sniffed by third parties, this step is necessary.

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# STRFTIME

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%Y%m%d"))

# HTTP PUT AND DELETE REQUESTS


# They work the same as post requests, with the difference that PUT means to update an existing value in the online application and delete to delete something from the application via API.


# INTRO TO HMTL
# INTERMEDIATE HTML
# INTRODUCTION TO CSS
# INTERMEDIATE CSS
# WEB FOUNDATION BOOTSTRAP AND TINDOG WEBPAGE (OPTIONAL)

''' already possessing enough experience at the above-mentioned topicss'''


# WEBSCRAPING WITH BEAUTIFOUL SOUP

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text


soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


'''
FAQ: Empire's website has changed!

When this lesson was created, I used this URL for the project: 
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
You'll see that the h3 with the class "title" is no longer there. 
To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.

'''

# SELENIUM TO SCRAPE WEBSITE DATA

from selenium import webdriver

# keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")

#stopped it due to time constraints, come back if necessary.



# __name__ and __main__ ATTRIBUTES BUILT INTO PYTHON

from flask import Flask
app = Flask(__name__)
# by providing name, flask will check whether this is the file where code executes and make sure
# that we aren't using an imported module.
if __name__ == "__main__": # meaning: if we are running the script from this current file
    app.run()
# print(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World'

# FUNCTIONS AS FIRST CLASS OBJECTS AND PASSING NESTING FUNCTIONS

## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(add, 2, 3)
print(result)

##Functions can be nested in other functions

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()

outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

inner_function = outer_function()
inner_function

# PYTHON DECORATOR FUNCTIONS AND THE @ syntax

# just wrapping another function and giving it some additional functionality or modifies the functionality. (syntactic sugar)
# call decorator by pasting it above object with an @sign, followed by function, e.g. @delay_decorator, putting an entire function through a machine that addds functionality before or after the function.

## Simple Python Decorator Functions
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        function()
        #Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

#With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")

#Without the @ syntactic sugar
def say_greeting():
    print("How are you?")
decorated_function = delay_decorator(say_greeting)
decorated_function()

# DATABASES WITH SQLite and SQLAlchemy

#notneededatmoment










