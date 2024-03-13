#   DAY 3
# ! Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not.
# Taking input from the user for length and breadth
'''
length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

# Checking if it's a square or not
if length == breadth:
    print("It is a square.")
else:
    print("It is not a square.")



# ! Eg:4
# Python program to check whether the
# given integer is a multiple of both 5 and 7
n = int(input("enter the number: "))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")


# ! eg:5
Write a program to accept the cost price of a bike and display the
road tax to be paid
according to the following criteria:
    cost price (in Rs)
    > 100000                        Tax
    < 100000                         15 % + discount 6%
                           5%


price=int(input("enter the price:"))
total=0
if price>=100000:
    discount=price*(6/100)
    value=price-discount
    tax=value*(15/100)
    total=value+tax
else:
    tax=price*(5/100)
    total=price+tax
print("The onroad cost of bike is: ",total)

 *if elif
 *Eg:1

a=6
b=7
c=9

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")


#A school has following rules for grading system:
#a. Below 25 F
#b. 25 to 45 E
#c. 45 to 50 D
#d. 50 to 60 C
#e. 60 to 80 B
#f. Above 80 A
#Ask user to enter marks and print the corresponding grade.

# Ask the user to enter marks
marks =int(input("Enter the marks: "))

# Determine the grade based on the marks entered
if marks < 25:
    grade = 'F'
elif marks >= 25 and marks < 45:
    grade = 'E'
elif marks >= 45 and marks < 50:
    grade = 'D'
elif marks >= 50 and marks < 60:
    grade = 'C'
elif marks >= 60 and marks < 80:
    grade = 'B'
else:
    grade = 'A'

# Print the corresponding grade
print("Grade:", grade)



# Eg:6
# ? Accept the age of peoples and display the oldest one.

# ! --> short hand if else
# Eg:1

a=9
b=60
if a>b:
    print("A")
else:
    print("B")
    #--> using short hand if else
    # rules
    #1). statement inside the if conditions have to be present at first
    #2). elif cannot be used in short hand if else
    #3). always it have to end with else

    #print("A") if a>b else print ("B")


# ! code to check the given char is vowel or consonent
char=input("enter the chart:")
if char=="a" or char =='i' or char=='o' or char=='u':
    print("is a vowel")
else:
    print("its consonent")



# ? or


str1="aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")


# ! shorthand if else
char=input("enter the char:")
str1="aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")


# ! ---> elif ladder using short hand if else
# eg :1
# ? find greatest among 3 varaibles using short hand if else
a=8
b=5
c=9
print("A is greater") if a>b and a>c else print("B is greater") if b>a and b>c else print("C is greater")



# ! -----------> looping

# looping can be iplemented using
# for loop
# while loop

# ! ---> for loop
# ? for loop is used for itearation, if we know the number of times the loop have to run
# ? It is used to iterate the iteratables eg(string, list, tuple, etc...)

# todo --> Syntax for loop

# ! for syntax in c
# for(i=0;i<10;i++){
#      printf("hello");
#}

# ! for the syntax in python
# for userdefined_varaible in range(start,end,step):default setp value is 1
#      statement
#      statement
#      statemenet
'''

#eg:1


#To print the value from 1 to 10 using for loop

#for i in range(0,10):
    #print(i)
 #   print("hello")
# eg:2
#for val in range(1,15,3):
#   print(val)


# eg:3
# to decrement the value

#for val in range(10,0,-1):
 #   print(val)

#for val in range(10,0,1):
#    print(val)


# EG:4
# PRINT THE OUTPUT OF 7 TH MULTIPLICATION TABLE FROM 21 TO 43
#for val in range(1,10):
#    print(val*7)
#for val in range(1,10000+1):
#    print(" I love you ",val*8)

#eg:4
#print the output of 7th multiplication table from 21 to 43
#for val in range(1,100+1):
#    print(" Jai balayya",val*5)
    #method 2
#    print('7','x',val,'=',val*7)
           #method 3
#   ans="7 x {} = {}"
#   print(ans.format(val,val*7))
#    print(f"7 x {val}={val*7}")



# eg:5
# break ---> which is used to terminate to loop

#for val in range(1,10):
#    if val==6:
#        break
#    print(val)


#    print(val)
#    if val==6:
#        break


#    if val==5:
#        print(val)
#        break


# ! continue
#eg:1
#for val in range(1,10):
#    if val==6:
#        continue
#    print(val)


#    print(val)
#    if val==6:
#        continue



# practice the problems
#print the even number between the 20 to 40
#for val in range(20,40,2):
#    print(val+1)
#for val in range(20,41):
#    if val %2==0:
#        print(val)





# ! ---> while loop
# while is used when do not kmow the number of times the loop haveto run
# to iterate the non iterable elements while loop is used

# todo syntax


#initialisation
# while conditons:
#    statement
#   incre or decre



#eg : 1
# to iterate number from 1 to 10

#i=0
#while i<11:
#    print(i)
#    i=i+1   #or i+=1

#Eg:2

#Eg:2
# to decrement using while loop
#i = 10
#while i > 0
#    print(1)
#    i-=1



#!---> 1-4+9-16+25=15
#n =int(input("enter number: "))
#sum=0
#for val in range(1,n+1):
#    sq=val*val
#    if val %2!=0:
#        sum=sum+sq
#    else:
#        sum=sum-sq
#print(sum)






#For loop practisee
#Write a program to display sum of odd numbers and even
#numbers that fall between
#12 and 37(including both numbers)

# Initialize variables to store the sum of odd and even numbers
#sum_odd = 0
#sum_even = 0

# Iterate through numbers from 12 to 37 (inclusive)
#for num in range(12, 38):
    # Check if the number is odd
#    if num % 2 != 0:
#        sum_odd += num  # Add odd number to the sum_odd
#    else:
#        sum_even += num  # Add even number to the sum_even

# Display the sum of odd and even numbers
#print("Sum of odd numbers:", sum_odd)
#print("Sum of even numbers:", sum_even)


#---> Assesment
# 1.) cats and mouse: Hacker rank
#2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even #numbers that fall between
# 12 and 37(including both numbers) # 4.) Write code to print the sum of number using while loop #n1123 -> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432




