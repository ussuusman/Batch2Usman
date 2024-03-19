'''
def generate_dict(n):
    return {x: x*x for x in range(1, n+1)}

n = 5
print("Sample Dictionary (n =", n, "):")
print("Expected Output:", generate_dict(n))

or

n=int(input("Enter the number:"))
d1={}
for val in range(1,n+1):
    d1[val]=val**2
print(d1)
'''           

#def dict1(n):
#    d1={}
#    for val in range(1,n+1):
#        d1[val]=val**2
#    print(d1)
#dict1(5)


# ! ---> object oriented programming

# The panadigms of objects oriented progarmming are


# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation

# ! Class is a blue print of an object

#l1=[1,2,3,4,5,6]

#eg:1
#class c1:
#    nmae1="Usman"
#    print(Ussu)

# ! Ex:2
#class person:
#     name="siddu"
#c=person() # c or object
##The process of creation of an object is called as Instantiation

#print(c.name)
# ex:3
# create of a method
#When the function is created with a class is called as method

# MEthod without parameter#class person:
#    def display(person):
#        print("Hello welcome to classes")
#p=person()
#p.display()

# Ex ; 4
# MEthod with parameter
'''
class person:
    def display(person,name,age):
        print(name,age)
p=person()
p.display("Usman",age)

# ! Eg:5
class person1:
    fname="Usman" # attribute or static variable

    lname = "T"

    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(self.fname+" "+self.lname)
p = person1()
p.first_name()
p.full_name()
'''
# Ex:6
# contructer ---> _init ___()

class profile:
    def __init__(self):
        print("hey")

p=profile()

'''
s1 = "Hello how are you"
s2 = "Hello how is"

def uncommon_words(s1, s2):
    set1 = set(s1.split())
    set2 = set(s2.split())
    uncommon = set1.symmetric_difference(set2)
    return uncommon

print("Uncommon words:", uncommon_words(s1, s2))

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

print("8th Fibonacci number:", fibonacci(8))


# ! Ex: 1
def profile(name,age,place):
    txt="My name is{}. Iam{} years old. Iam from{}."
    print(txt.format(name,age,place))
print("usman",21,"Dhone")

# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement



Ex:4
function with return statement

def f1():
    z=8
f1()
print(z) # --> error ---cannot use outside the function




def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)


def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)


# 123
def palindrome():
    print(n)

a=int(input("Enter the value: "))
palindrome(a)




#? Problem:1
def palindrome(n):
    string=str(n)
    rev=str(n) [::-1]
    if string==rev:
        print(n, "Palindrome")
    else:
        print("Not palindrome")
a= int(input("Enter the value: "))
palindrome(a)



#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args


# * Positional args
# ? The position of parameter have to be same as position as arguments
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(9666868631,"Usman",100) #unexpected



# * Keyword args
# ! Eg:1
#? To overcome the disadvantage of position args, we use keyword args
# ? it is process of initiating the parameter with args while calling the
# funtions
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))
profile(name="Usman",mark=100,phone=96668686)

# todo  ---> Exception of keyword args functions
def profile(name,phone,mark):
    txt="My name is{}. My phone number{}. I got{} marks."
    print(txt.format(name,phone,mark))#
#profile(name="Usman",mark=100,9666868631) # error --> positional arsg follow keys
#profile(9666868631,name="Usman",mark=100) # error __-> name has multiple values
profile("Usman",mark=100,phone=9666868631)

'''

#default args

# ! Ex: 1

#def profile(name,phone,place="Kadap"):
#    txt="My name is{}. My phone number{}. I am from{}."
#    print(txt.format(name,phone,place))
#profile("Usman",9666868631,"Guntur")
'''
def profile(name,phone,place="Kadapa"):
    if place="kadapa" or place=="KADAPA" or place=="kadapa":
        txt="My name is{}. My phone number{}. I am from{}."    
        print(txt.format(name,phone,place))
        
    else:
        print("You are not eligible to signup")
    
profile("Usman",9666868631)
'''
'''
Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal
'''
'''
Exception
profile(name, place="KADAPA", phone): # error coz default args should not follow #positional param
if place == "Kadapa" or place="KADAPA" or place=="kadapa":
    txt = "My name is {}. My phone number is (). I am from {})."
    print(txt.format(name, phone, place))
else:
    print("You are not eligible to Signup")
file("Usman", 9666868631)


# ! Variable length parameter
# ! EX: 1

def profile(*name):
    print("My name is ", name)
profile("Usman", 'Charan', 'Naresh')


# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="Usman", " Charan ", " NAresh "
#print(name)


def profile(*name):
    for val in name:
        print(" My name is",val)
profile("USman", 'Ussu', 'Alone')

'''

# Ex:2
#def profile(*name,age):
#    for val in name:
#        print(" My name is",val,"may age is",age)
#        
#profile("USman", 'Ussu', 'Alone',35) # ---> error ---> age has no args

'''
def profile(age, *name):
    for val in name:
        print(" My name is",val,"my age is",age)
profile(21,"USman", 'Ussu', 'Alone')
'''
'''
# * Keyword variable length args
# Ex: 1
#kwargs ---> Which is used to provide the args in the form of key value pair.
def price(**price_list):
    print(price_list)
price(a=200,b=80000)

#d1=dict{}
'''







