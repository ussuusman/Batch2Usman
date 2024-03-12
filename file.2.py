'''
   VARIABLES

# a, b, c = 9 , 8, 7, 8
# print(a, b, c)
#a, b = c = 7, 8
# print(a)
# print(b)
# print(c)


a=b, c = 4, 2
print(a, b, c) 
a = 7
b = 5
# a=b, c = 4 2
# print(a, b, c) I
# ----> swapping of variables a = 7
b = 5


# Eg:1
# temp=a  #temp=7
# a=b     #a = 5
# b=temp  #b = 7
## a = 5, b = 7
# print(a, b)

 #Eg:2
a=a+b #a=12
b=a-b #b=12-7=5
a=a-b #a=12-5=7
print(a, b)
a, b=b, a # only in python
print(a, b)

a=35
b=7
a=a*b #a=35
b=a/b #b=35/7=5.0
a=a/b #a=35/5=7.0
print(int(a),int(b))

#id() --> used to find the memory address of the variable
a = 7
b = 8
# print(a)
print(id(a))
print(id(b))

#-----> Keywords
# Keywords are reserved words which provides special meaning to
# compiler or interpretor

import keyword
print(keyword.kwlist)
print(type(keyword.kwlist))

# To check if the string is keyword or not
print(keyword.iskeyword("sid")) # False


if=8
print(if) # error coz if is a keyword


#!----> literals
# Literal is the constant value asssigned to a variable
# A variable is considers to be constant when it is defines
# in caps

a= 78 # a is variable
A=78 # A is constant



#hash() --> it creates a hash value for constant datatypes and
# provides error for non constant datatypes
n1=89.78
print(hash(n1))

f1=[7,8,9]
print(hash(f1)) #error --> list is not-constant or mutable datatype

a=9
b=9
b=90
print(id(a))
print(id(b))


# ! ----> Operators
# ? Operators are symbols which is used to perform various opearions
# ? between 2 or more operands

#ARTHIMATIC
#ASSIGNMENT
#LOGICAL
#RELATIONAL OR COMPARISION
#BITWISE
#IDENTITY
#MEMBERSHIP

# todo ---> +,-,*,/,%,//,**
a=8
b=6
c=9
print(a+b+c)



#input() --> used to get the runtime input
#eval() --> used to get the runtime values of all datatype
n1= eval(input("Enter the value:"))
print(n1)


a=4
b=2
print(a/b) # is used to get the quotient value
print(a%b) # is used to get the remainder value


#! //--> floor devision
a = 765433
b = 19
#print(a//b) #--> the output will be in integer & the output will
#based on floor value

#! **--> used for power of a number
#print(2**4) #--> 16


# ! Assignment  --> +=, -=, /=, *=, //=, **=, &=, |=

a=8
a+=2
print(a)


a=30
a-=5
print(a)


# ! comparision --> ==, >, <, !=< >=


a=8
b=7
print(a>b) # true


a=9
b=4
print(a==b)


# ! Bitwise opeartor --> &, |, ^, ~, <<, >>
a=7
b=4
print(a&b)



#2^4 2^3 2^2 2^1 2^0
#8    4    2    1

#0    1    1    1       #---> 7
#0    1    1    0       #---> 6
# ---------------------------
#0    1    1    1    #---->7


# 256 128 64 32 16 8 4 2 1
# 0 0 0 0 0 0 0 0 1 0 0


# AND
# A B A&B
# 0 0 0
# 0 1 0
# 1 0 0
# 1 1 1

                 
# XOR
# A  B  A^B
# 0  0  0
# 0  1  1
# 1  0  1
# 1  1  0

# 32
# --> 10
#100110^ #
#
# 2^4 2^3 2^2 2^1 2^0
# 8 4 2


#~--->
a = 9
print(~a+1)

# a = 9
# 128 64 32 16 8 4 2 1
# 0    0  0  0 1 0 0 1 # -->   9

#  1   1  1  1 0 1 1 0 # -->  -10

# 0  0  0  0  1  0 1 0 --> 10

# 1 1 1 1 0 1 0 1  -> 1s compliment of 10
              # 1  -->2s compliment
#------------------------------
# 1  1  1  1  0  1  1 0 --> -10

# 256 128 64 32 16 8 4 2 1
#  0   0   0  0  0 0 1 0 1   3<
#  0   0   0  1  0 1 0 0 0 --> 40
# 107

# <<,>>
print(5>>1)
'''


# ! Logical  --> used to compare the expressiona
# and< or , not
#a=6
#print(a>3 and a<10)
#print(a>7 or a<30)
#print(not(a>8 and a<10))

#! Identity operator
#a=8
#b=8
#print(a is b)
#print(a==b)

#a=(1,2,3)
#b=(1,2,3)
#print(a is b)


#a=[1,2,3]
#b=[1,2,3]
#print(a is not b)


# ! Membership operator
# in, not in
#l1=[7,8,9,0,6,5]
#num=55
#print(num in l1)
#print(num not in l1)


#num=678
#print(8 not in num) # error

# ! conditional statement
# if, elif, else

# Eg:1
#--> C syntax)
#if (condition){
#    statement
#    statement
#    statement
#    statement
    
#}
# Python syntax
#if condiotion
#    statement
#    statement
#    statement
# statement


#eg:1
#a=6
#if a:
#    print("hello")

# eg:2
#a=6
#if a>3:
      #print("hey")
#else:
    #print("No")


# eg:3
#if 7>8:
     #print("hello")
#print("Usman")

# eg:4
#a=0
#a=False
#a=""
#if a:
#    print("Usman")
#else:
 #   print("No")


# a number is even or odd
#n=int(input("enter the number"))
#if n %2==0:
 #     print(n, "is even")
#else:
#    print(n, "is odd")


#name, age ,nationality
# 18 above, Indian
Name=input("What is your Name?:")
Age=input("how old are you:")
nationality=input("enter the nation:")

if age>=18 and nationality=="Indian":
    print("eligible for vote")
else:
    print("not eligible")
