'''
def calculate_fuel_consumption():    liters = float(input("Enter the no of liters to fill the tank:\n"))
    if liters <= 0:
        print(f"{liters} is an Invalid Input")
        return
    
    distance = float(input("Enter the distance covered:\n"))
    if distance <= 0:
        print(f"{distance} is an Invalid Input")
        return

    fuel_consumption_per_100km = (liters / distance) * 100
    miles = distance * 0.6214
    gallons = liters * 0.2642
    miles_per_gallon = miles / gallons

    print("\nLiters/100KM")
    print("{:.2f}".format(fuel_consumption_per_100km))

    print("\nMiles/gallons")
    print("{:.2f}".format(miles_per_gallon))

calculate_fuel_consumption()
'''
'''
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

print("8th Fibonacci number:", fibonacci(8))


s1= "Hello how are you"
s2="Hello how is"
s1=s1.split(" ")
s2=s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

'''

# 3). Write a code print the 8th fibanochi number
# 0,1,1,2,3,5,8

#n1=0
#n1=1
#ans=0+1==> 1

#n1=1
#n2=1
#ans=1+1==> 2
'''
# find the 8th fibanochi number
num=8
n1=0
n2=1

for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
print(ans)
    


# ! contructors

# ex:2

#unparametarised constructor
class profile:
    def __init__ (self):
        print("hello world")
obj =profile()
obj.__init__()

'''
'''
# Ex:3

class profile:
    def __init__ (self, id, name, age):
        print(id, name, age)
obj=profile(318, "usman", 21)
'''
'''
# ? Eg:4
class c1:
    name= "Usman"
    place="Dhone"
    def m1(self):
        print(self.name,self.place)
#        pass
object=c1()
object.m1()

or

class c1:
    email="ussu@gmail.com"
    def m1(self):
        name= "Usman"
        place="Dhone"
        print(name,place)
        print(self.email)
#        pass
object=c1()
object.m1()

# Ex:5

class c1:
    def m1(self):
        name= "Usman"
        age=21
        return name, age

    def display(self):
        print(self.m1())
object=c1()
object.display()

'''
'''
# ? Eg:6
# ? To use the variables inside the constructor in another method
class class1:
   # email ="ussu@gmail.com"    --" static variable"
    def __init__(self):
        self.name="Usman"
        self.email="Ussu@gmail.com"
        # return name, email ----> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1=class1()
c1.display()

'''

# !  ------> Inheritance

 # the process of utilising the methods and attributes of parent class
 # through the object of child class it is called as inheritance

 # 5 types of Inheritance
 # single Inheritance
 # multilevel Inheritance
 # Multiple Inheritance
 # hybrid Inheritance
 # heirarichal Inheritance

 # single Inheritance
 # It has only one parent and only one child class
'''
 # EX:1

class parent:
    def m1(self):
        print("Iam parent class")

class child(parent):
    def m2(self):
        print("Iam child class")

obj=child()
obj.m1()

# ! Ex:2

class c1:
    def __init__(self):
        print(" I am constructor from parent class")

class child1(c1):
    pass

obj= child1()


# ! ex:3
class parent:
    name= "Usman"
class child(parent):
     name= "Ussu"

     def display(self):
         print(self.name)

d=child()
d.display()

'''

#  ! MUltilevel inheritance

# ! Ex:1
'''
class voice:
    def sound(self):
        print("All the animals have their own voice")

class dog(voice):
    def dog_voice(self):
        print("Bark")

class cat(dog):
    def cat_voice(self):
        print("Meow")

class parrot(cat):
    def parrot_voice(self):
        print("Speak")

all=parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
'''

# EX:2
'''
class honda_city:
    def engine_specs(self,cc,hp,torque,fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel_type, num_of_piston)
    def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class amaze(honda_city):
    def amaze engine_s (parameter_torque: Any 2, fuel type, num_of_piston):
        print(cc, Hp, torque, fuel type, num_of_piston)
    def amaze_body_specs(self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class civic(amaze):
    def civic_engine_specs(self, cc, Hp, torque, fuel_type, num_of_piston):
        print(cc, Hp, torque, fuel type, num of piston)
    def civic_body_specs (self, color, weight, height, length, vehicle_type):
        print(color, weight, height, length, vehicle_type)
class Honda(civic):
    pass

honda =Honda()
honda.honda_city_engine_specs (1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")

'''
'''
 # Multiple Inheritance
 #? It has multiple parent and 1 child
class while_pertol:
    def function_w(self):
        print("used to Airplans")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol(while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
        print("Petrols types")
p=petrol()
p.defanition()
p.function_o()

'''
'''
# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(4,2)
'''
'''
 # heirarichal Inheritance
 #! Heirarical inheritance
class catagory:
    def weight(self,weight):
        print("weight")
    def display(self,color,taste):
        print(color,taste)
class tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste= "neutral taste"
        self.display(color,taste)
class carrot(catagory):
    def carrot_specs (self):
        color="green"
        taste= "sweet"
        self.display(color,taste)

c=carrot()
c.carrot_specs()
c.weight("30gms")

t=Tomato()
t.tomato_spec()
t.weight("20gms")

'''
'''
 # hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
class c2(c1):
    def m2(self):
        print("class2")
class c3(c2):
    def m3(self):
        print("Class 3")
class c4(c2):
    def m4(self):
        print("Class 4")
class c5(c3):
    def m5(self):
        print("Class 5")
class c6(c5,c4,c2,c1):
    def m6(self):
        print("Class 6")
obj=c6()
obj.m3()

'''

# ! -------> polymorphism
#poly - many -, morph ---> form
# a function has the ability to perform more than 1 functionality
# then it is considered to be as polymorphism

# polymorphism in builtin functions
# len() --> Which is used to find the length of list, tuple, dict etc...
# index
#max()
#count()
#pop()
# and more...

# polymorphism in operation

#+
#print(8+8)

#print("k"+'1')
#print ([1, 2, 3] + [5, 6])

# *
print(6*7)
l1= (12,3,4,5,6)
print(*l1)
#def f1(*args)
l1 =[1,2,3,4]
print(l1*10)















