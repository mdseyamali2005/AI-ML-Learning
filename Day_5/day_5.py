# class student:
#     def __init__(self, name, age):
#         print("Wow you are very interesting..........")
#         self.name = name
#         self.age = age
# s1 = student("harun", 34)
# s2 = student("bokachoda", 3.344)
# s3 = student("harun", 21.34)
# print(s1.name,s1.age)
# print(s2.name,s2.age)
# print(s3.name,s3.age)
# class balu:
#     school = "Baust"
#     batch = 19
#     def __init__ (self,name,cgpa=4):
#         self.name= name
#         self.cgpa = cgpa
# s1 = balu("Rohan", 3.37)
# s2 = balu("chandu", 2.45)
# s3 = balu("mandu", 3.64)
# s4 = balu("tharki", 3.99)
# s5 = balu("harnia")
# print(s1.name,s1.cgpa)
# print(s5.name, s5.cgpa)
# print(s5.school, s5.cgpa,s5.batch)
# class seyam:
#     pi = 3.1416
#     name = "Seya987m"
#     def __init__(self, rahul, nulmber):
#         self.name = rahul
#         self.number = nulmber
# ob1 = seyam("Bablu", 3243)
# print(ob1.name, ob1.number, seyam.name)
# class laptop:
#     st_type = "NVME"
#     def __init__(self, ram, storage):
#         self.ram = ram
#         self.storage = storage
#     def get_info(self):
#         print(f"Ram is {self.ram} and storage is {self.storage} and the type of the storage is {self.st_type}")
# l1 = laptop("16GB", "1TB")
# l12 = laptop("8GB", "512GB")
# l1.get_info()
# l12.get_info()
# class laptop:
#     st_type = "NVME"
#     def __init__ (self, ram, storage):
#         self.ram = ram
#         self.storage = storage
#     @classmethod
#     def get_class(cls):
#         print(f"the fucking storage is {cls.st_type}")
#     @staticmethod
#     def get_discount(price, amount):
#         print(f"The price is after teh discount is {price - amount}")
# l1 = laptop("16GB", "1TB")
# l1.get_class()
# l1.get_discount(1000, 200)
# class product:
#     count = 0
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         product.count +=1
#     def get_info(self):
#         print(f"The name of the product is {self.name} and the price is {self.price}")
#     @classmethod
#     def get_count(cls):
#         print(f"The total number of products is {cls.count}")
#     @staticmethod
#     def get_discount(price, percentage):
#         discount_amount = price * (percentage / 100)
#         discounted_price = price - discount_amount
#         print(f"The price after {percentage}% discount is {discounted_price}")
# l1 = product("Laptop", 1000)
# l2 = product("Phone", 500)
# l3 = product("Tablet", 300)
# l1.get_info()
# l2.get_info()
# l3.get_info()
# product.get_count()
# product.get_discount(1000, 20)
# class bandaccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#     def sel_balance(self, ammount):
#         self.__balance += ammount
#     def get_balance(self):
#         return self.__balance
# acc1= bandaccount("Janu", 1000_99)
# acc1.sel_balance(2000_22)
# print(acc1.name, acc1._bandaccount__balance)
# class employ:
#     start_time = "10am"
#     end_time = "6pm"
# class teacher(employ):
#     def __init__(self, sub):
#         self.sub = sub
# class worker(employ):
#     def __init__(self, role):
#         self.role = role
# t1 = teacher("Math")
# w1 = worker("wosh")
# print(t1.sub, t1.start_time, w1.role, w1.end_time)
# class teacher:
#     def __init__(self, sub):
#         self.sub = sub
# class student:
#     def __init__(self, dep):
#         self.dep = dep
# class ta(teacher, student):
#     def __init__(self, sub, dep, name):
#         # teacher.__init__(self, sub)
#         # student.__init__(self, dep)
#         super().__init__(sub)
#         student.__init__(self, dep)
#         self.name = name
# a1 = ta("Math", "cse", "Md seyam ali")
# print(a1.name, a1.dep, a1.sub)
###################################
# from abc import ABC, abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def sound(self):
#         None
# class lion(animal):
#     def sound(self):
#         print("ror!")
# class cow(animal):
#     def sound(self):
#         print("Mooo!")
# a1 = lion()
# a2 = cow()
# a1.sound()
# a2.sound()
