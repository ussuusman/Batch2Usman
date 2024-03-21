# Task 1
'''
def min_max_price(products):
    min_price = min(products.values())
    max_price = max(products.values())
    min_product = [key for key, value in products.items() if value == min_price]
    max_product = [key for key, value in products.items() if value == max_price]
    return min_product, max_product

def find_products_startswith_s(products):
    startswith_s = [key for key in products.keys() if key.lower().startswith('s')]
    return startswith_s

d1 = {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
min_product, max_product = min_max_price(d1)
print("Min priced product(s):", min_product)
print("Max priced product(s):", max_product)

startswith_s = find_products_startswith_s(d1)
print("Products starting with 's' or 'S':", startswith_s)

# Task 2
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_strong_number(num):
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))
    return sum_of_factorials == num

n = 67
if is_strong_number(n):
    print(f"{n} is a strong number.")
else:
    print(f"{n} is not a strong number.")

# Task 3
def rotate_list(l, n):
    n = n % len(l)
    return l[-n:] + l[:-n]

l1 = [1, 2, 3, 4, 5, 6]
n = 2
print(f"n={n} --> {rotate_list(l1, n)}")

n = 3
print(f"n={n} --> {rotate_list(l1, n)}")
'''
'''
# Method Over-riding
#Ploymorphism in classes
class bank:
    def ratio(self):
        print("All banks has repo rate")
class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")
class IOB(bank):
    def ratio(self):
        print("IDB rate is 7.5%")
i= IOB()
i.ratio()
s = SBI()
s.ratio()
'''
'''
#Eg:2
class USA:
    def langauge(self):
        print("English")
        def capital(self):
            print("Washington DC")
class India(USA):
    def langauge(self):
        print("None")
    def capital(self):
        print("New delhi")
I = India()
I.langauge()
I.capital()
'''

#Eg:3
#Polymorphism using objects
#C!1, C2 ---->C1= print(c1), print(c2)
#f1, f2
'''
class c1:
    def f1(self):
        print("class1")
class c2(c1):
    def f2(self):
        super().f()
        print("class2")
obj1=c2()
obj1.f1()

#obj2=c1()
#obj2.f1()
'''
'''
# Eg:4
class c1:
    def f1(self):
        print("class 1")
class c2(c1):
    def f1(self):
        print("class 2")
obj1=c2()
obj2=c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)

'''
'''
#changing the functionality of builtin functions
class shooping:
    def __init__(self, l1):
        self.items =l1
    def __len__(self):
        length=len(self.items)
        return length

s=shooping([1,2,3,4,5])
print(len(s))
'''

# ! ___> Method overloading
'''
#! Eg:1
class suming:
    def add(self, a, b):
        print(a+b)
    def add(self, a, b, c):
        print(a+b+c)
s = suming()
#s.add(4, 5) # ---> error
s.add(4,5,1)
'''

# EX:5
'''
#| Eg:2
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj=summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)
'''
# ! --->  Abstraction
# The process of hiding the  implementation details is abstraction
#Eg:1
'''
class shapes(ABC):
    def sides(self):
        print('All shapes have sides except circle')
class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")
    def name(self):
        pass
class square(shapes):
    def square(self):
        print("4 sides")
    def sides(self):
        pass
tr=triangle()
tr.triangle_sides()
tr.name()
'''

# Rules to define abstract class1
#1.) Abstract class cannot be instantiated
#2.) from abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) convert the normal method inside the abstract class to abstract method
#5.) All the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the # child classes
'''
 #! Eg:2
#super() ---> used to access the parent class method from child class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")
class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")
    def m1(self):
        pass
class2=c2()
class2.m2()

# * Eg:3
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd="ussu1438"
        return pswd
class login(password):
    def validate(self,name,password):
        if super().pwd()==password:
            print("Welcome", name,'!!')
            print("Login Successfull")
        else:
            print("Please check the password")
    def pwd(self):
        pass
Login=login()
name=input("Enter the nume: ")
pwd=input("Enter the password: ")
Login.validate(name,pwd)
            
'''
'''
# ! Encapsulation
# EX:1
class car:
    __name="BMW" # Private variable
    print(__name)
c1=car()
print(c1.name) # error
c1.name="Audi"
print(c1.name)# error
   '''
'''
# * ---> Ex;2
class c1:
    __phone='1234567890'
    def display(self):
        print(self.__phone)
c=c1()
c.display()
'''
'''
# * ---> Eg:3
# ? declare private method
class class1:
    def __m1(self): # Private method
        print("Iam private method")
    def __init__(self):
        self.__m1()
c=class1()
'''
'''
#? nested class
class class1:
    class class2:
        name= "Usman"
        def display(self):
            print(self.name)
    obj1 =class2()
obj = class1()
obj.obj1.display()
'''
#!----> Tasks
#Write the code for the below tasks using function
#1.) d1 {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30)

d1 ={"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
for val in d1:
    if d1 [val] == min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)








# * changing the functionality of builtin functions
#a = 3
#b = 6
# print(a+b)

#print(a.__add__(b)) #? dunder metthod or mafic method
#int()
#print(a.__sub__(b))
#len()








































