################ q1 ####################
# class BankAccount:
#     def __init__(self, account_number, owner_name, balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance = amount
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. New balance is {self.balance}")
#     def check_balance(self):
#         print(f"current balance is {self.balance}")
# acc1 = BankAccount("123456789", "John Doe", 1000)
# acc1.check_balance()
# acc1.deposit(500)
# acc1.check_balance()
# acc1.withdraw(200)
# acc1.check_balance()
################## q2 #####################
# class book:
#     def __init__(self, title, author, list_of_reviews= None):
#         self.title = title
#         self.author = author
#         if list_of_reviews is None:
#             self.list_of_reviews = []
#         else:
#             self.list_of_reviews = list_of_reviews
#     def new_review(self, new):
#         self.list_of_reviews.append(new)
#     def count_reviews(self):
#         return len(self.list_of_reviews)
#     def  display_all_reviews(self):
#         return(self.list_of_reviews)
# book1 = book("Wonder is love", "Seyam")
# book1.new_review("It's great")
# book1.new_review("wow i like this")
# print(book1.count_reviews())
# print(book1.display_all_reviews())
################## q3 #####################
# class student:
#     def __init__(self, name= None,roll_no=None, marks=None):
#         self.__name = name #private variable
#         self.__roll_no = roll_no
#         self.__marks = marks
#     def set_name(self, name):
#         if name == "":
#             print("Name cannot be empty")
#         else:
#             self.__name = name
#     def get_name(self):
#         return self.__name
#     def set_roll_no(self, roll_no):
#         if roll_no>100 or roll_no <= 0:
#             print("Roll number must be positive")
#         else:
#             self.__roll_no = roll_no
#     def get_roll_no(self):
#         return self.__roll_no
#     def set_marks(self, marks):
#         if marks < 0 or marks > 100:
#             print("Marks must be between 0 and 100")
#         else:
#             self.__marks = marks
#     def get_marks(self):
#         return self.__marks
# s1 = student()
# s1.set_name("Seyam")
# s1.set_roll_no(10)
# s1.set_marks(85)
# print(s1.get_name())
# print(s1.get_roll_no())
# print(s1.get_marks())
################## q4 #####################
# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.1416 * self.radius ** 2
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height
# cir = Circle(5)
# rect = Rectangle(4, 6)
# tri = Triangle(4, 8)
# print(f"Area of Circle: {cir.area()}")
# print(f"Area of Rectangle: {rect.area()}")
# print(f"Area of Triangle: {tri.area()}")

################ q5 ###################
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         Vehicle.__init__(self , brand, model)
#         self.seats = seats
# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_cc):
#         Vehicle.__init__(self , brand, model)
#         self.engine_cc = engine_cc
# ca1 = Car("Toyota", "RTx-323", 5)
# ba1 = Bike("hero", "ct-323", 100)
# print(ca1.brand)
# print(ba1.model)
# print(f"In the car seats number is: {ca1.seats}")

#################### q6 ######################
# from abc import ABC, abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         None
# class Intern(Employee):
#     def calculate_salary(self):
#         print("the salary is 29k")
# class FullTimeEmployee(Employee):
#     def calculate_salary(self):
#         return("the salary is 53k")
# class ContractEmployee(Employee):
#     def calculate_salary(self):
#         return("the salary is 40k")
# a1 = Intern()
# a2 = FullTimeEmployee()
# a3 = ContractEmployee()
# a1.calculate_salary()
# print(a2.calculate_salary())
# print(a3.calculate_salary())

################### q7 ##################
# class Person:
#     def __init__(self, name = None, age = None, address = None):
#         self.name = name
#         self.age = age
#         self.address = address
# a1 = Person("Seyam")
# a2 = Person("rohim", 98)
# a3 = Person("Lemon", 34, "Dhaka")
# print(a1.name)
# print(a2.name)
# print(a3.name)
# print(a3.address)
# print(a1.age)
# print(a2.age)   
####################### q8 ########################
# class Player:
#     player_count= 0
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         Player.player_count +=1
# p1 = Player("Seyam", 100)
# p2 = Player("Rohan", 150)
# print(f"Total players created: {Player.player_count}")
#################### q9 ##########################
# class Herbivore:
#     def Herb(self):
#         print("I lobe Herbivore")
# class Carnivore:
#     def Carn(self):
#         print("I lobe Carnivore")
# class Omnivore:
#     def Omn(self):
#         print("I lobe Omnivore")
# class Bear(Herbivore, Carnivore, Omnivore):
#     def Bear(self):
#         print("I lobe Bear")
# a2 = Bear()
# a2.Herb()
# a2.Carn()
# a2.Omn()
# a2.Bear()
################## q10 ######################
# class Message:
#     message_counter = 1

#     def __init__(self, sender, content):
#         self.sender = sender
#         self.content = content
#         self.id = Message.message_counter
#         Message.message_counter += 1

#     def __str__(self):
#         return f"[{self.id}] {self.sender.username}: {self.content}"

# class User:
#     def __init__(self, username):
#         self.username = username
#         self.chatroom = None

#     def join_chatroom(self, chatroom):
#         if self.chatroom:
#             print(f"{self.username} is already in {self.chatroom.name}.")
#         else:
#             chatroom.add_user(self)
#             self.chatroom = chatroom
#             print(f"{self.username} joined {chatroom.name}")

#     def leave_chatroom(self):
#         if not self.chatroom:
#             print(f"{self.username} is not in any chatroom.")
#         else:
#             room_name = self.chatroom.name
#             self.chatroom.remove_user(self)
#             self.chatroom = None
#             print(f"{self.username} left {room_name}")

#     def send_message(self, content):
#         if not self.chatroom:
#             print(f"{self.username} cannot send a message (not in a chatroom).")
#         else:
#             self.chatroom.broadcast(self, content)

# class ChatRoom:
#     def __init__(self, name):
#         self.name = name
#         self.users = []
#         self.messages = []

#     def add_user(self, user):
#         if user not in self.users:
#             self.users.append(user)

#     def remove_user(self, user):
#         if user in self.users:
#             self.users.remove(user)

#     def broadcast(self, sender, content):
#         new_msg = Message(sender, content)
#         self.messages.append(new_msg)
#         print(new_msg)

#     def show_active_users(self):
#         """New feature: Lists all users currently in the room."""
#         print(f"\n--- Users currently in {self.name} ---")
#         if not self.users:
#             print("The room is empty.")
#         for user in self.users:
#             print(f"• {user.username}")
#         print("----------------------------------\n")

#     def show_chat_history(self):
#         print(f"\n--- Chat History of {self.name} ---")
#         for msg in self.messages:
#             print(msg)
#         print("-------------------------------\n")

# # Testing the new feature
# if __name__ == "__main__":
#     room = ChatRoom("Python Lounge")
    
#     u1, u2, u3 = User("Alice"), User("Bob"), User("Charlie")

#     u1.join_chatroom(room)
#     u2.join_chatroom(room)
    
#     # Check who is online
#     room.show_active_users()

#     u1.send_message("Is anyone else here?")
#     u3.join_chatroom(room)
    
#     # Check updated list
#     room.show_active_users()