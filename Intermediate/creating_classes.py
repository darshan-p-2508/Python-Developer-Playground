# def function():
#     pass

# creating class - should be "PascalCase" (1st letter capitalized)
# other cases we have seen is like "camelCase", "snake_case"
class User:
    pass    # does nothing, just passes the control over

user_1 = User()
user_1.id = "001"
user_1.username = "Alex"

print(user_1.id + ": " + user_1.username)

# if we want 2nd user
user_2 = User()
user_2.id = "002"
user_2.username = "Bob"

print(user_2.id + ": " + user_2.username)

# this is not feasible, because, in future we may have to change the attribute name
# and update everything manually, shouldn't make typo, time consuming for updating the code
# difficult to manage

# for the id number we can automate it so that when we create an object id is constructed
# this concept is called "constructors" : a part of the blueprint(class) where we specify what
# should happen when object is created - "initializing the object"

# how do we do it?
# class Car:
#   def __init__(self):
#       # initialize attributes

# the init function is going to be called everytime the new object is created

class User1:
    def __init__(self):
        print("Constructors are executed first.\nNew object created...")

u1 = User1()
u1.id = "001"
u1.username = "John"

print(u1.id + ": " + u1.username)

# how to set attributes in a constructors?
# class Car:
#   def __init__(self, seats):  # just add the variable as parameter here
#       self.seats = seats
# my_car = Car(5)    # this creates the object "my_car" and assigns its variable "seats" with the value of "5"

class User2:
    def __init__(self, user_id, user_name, account_status = "Public"):  # here we have provided default argument which is editable
        print("Constructors with arguments")
        self.id = user_id
        self.username = user_name
        self.accountstatus = account_status    # here we have an attribute with default value, for every object created

u2 = User2("001", "Dan")
print(u2.id + ": " + u2.username + ": " + u2.accountstatus)
u2a = User2("002", "Tim", "Private")
print(u2a.id + ": " + u2a.username + ": " + u2a.accountstatus)

# Adding methods to class
# class Car:
#   def enter_race_mode():
#       self.seats = 2

class User3:
    def __init__(self, user_id, user_name): 
        print("Constructors with arguments")
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1

u3 = User3("001", "Sam")
u3a = User3("002", "Jack")

u3a.follow(u3)
print(u3a.followers)
print(u3a.following)
print(u3.followers)
print(u3.following)
