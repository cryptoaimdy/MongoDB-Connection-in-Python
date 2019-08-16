# MongoDB With Python
The Task is to connect mongoDB using python and store data and perform CRUD Operations into it.

# What is MongoDB
MongoDB is a NoSQL database used for storing large amount of data. Instead of using tables and rows, MongoDB uses Collections and documents.

# What is Python
Python is an Object Oriented Programming Language and is considered very convenient to take in if working on Objects. Python is easy to understand beacuase it has english like syntax and does the work in few lines of code.

As we know MongoDB is used for historic and large amount of data(data related to time). here we ll know about how to connect MongoDB in Python using a library called "Pymongo". Python has another libraries also to connect MongoDB but pymongo is most preferred library.

### Technologies Used
+ Used Python and Related libraries(pymongo used to connect MongoDB database).
+ Used MongoDB database 

# Tutorial

**Download and Install MongoDB, Set Path**

Read my MEDIUM Story on "How to Install MongoDB and CRUD Operations"

https://medium.com/@mohammadali1ali/mongodb-installation-and-crud-commands-dd0972a9be6c


**Library Used**
+ Pymongo
+ MongoEngine is also a library to connect mongoDB  with python but we ll prefer pymongo here.
+ MongoKit is a Python-module, a PyMongo wrapper, that brings structured schemes and screening layer.

**IDE Used and version**
+ PyCharm ( PyCharm is recommed IDE for Python, you can use any IDE that supports Python)
+ JetBrains PyCharm Community Edition 2019.1.3

**Download and install Pycharm IDE**

+ Create a work directory any where on the localmachine(desktop) and open that directory into Pycharm-->Open project.
+ Install Pymongo(a mongodb library for python) using "pip install pymongo" command in the terminal(you can use pycharm terminal also)
+ create a userdata.py file into that directory and import all the required libraries first(pyMongo) then create a connect to MongoDB and then create Objects to store in database.

# Running the Code!

+Give the Configuration of your MongoDB server into userdata.py file('mongodb://localhost:27017') and cd to location where
you saved "userdata.py" file and run this command "python userdata.py"
