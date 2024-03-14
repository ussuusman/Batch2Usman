#while loop
# ----> break using loop
'''
# eg:1
#1).iterate from 20 to 30 and break the loop in 27

i=20
while i<31:
    if i==27:
        break
    print(i)
    i=i+1

#eg:2
i=20
while i<31:
    print(i)
    i=i+1
    if i==27:
        break


#eg:3
i=20
while i<31:
    print(i)
    if i==27:
        break
    i=i+1


#eg:4


i=20
while i<31:
    if i==27:
        print(i)
        break
    i=i+1




# ! ----> continue

Ex:5


i=20
while i<31:
    if i==27:
        continue
    print(i)
    i=i+1



#ex:6


i=20
while i<31:
    i=i+1
    if i==27:
        continue
    print(i)



#ex:7
#while to iterate from 12 to 22
#find the sum of all numbers

i=12
sum=0
while i<23:
    sum=sum+i
    print(sum)
    i=i+1




#eg:8


i=12
sum=0
while i<23:
    sum=sum+i
    i=i+1
print(sum)




#ex:9

# Find the avg of value from 20 t0 25



i=20
sum=0
while i<25:
    sum=sum+i
    i=i+1
print(sum/6)


ex:10

i=20
sum=0
count=0
while i<=25:
    sum=sum+i
    count+=1
    i=i+1
print(sum/count)
print(100/6)



# ! ----> Nested for loop
#ex:1


for i in range(1,5):
    for j in range(1,4):
        print(i,j)


#ex:2

# * * * *
# * * * *
# * * * *
# * * * *


rows=int(input("enter the rows: "))
cols=int(input("enter the cols: "))
for row in range(rows):
    for col in range(cols):
        print("*",end=" ")
    print()



sum=0
for row in range(5):
    for col in range(7):
        sum=sum+1
        print(sum,end=" ")
    print()




# to print stars in right angled triangle
for row in range(0,6):
    for col in range(0,row):
        print("*",end=" ")
    print()




for row in range(0,6): #(6,0,-1)
    for col in range(row,6): #(0,row)
        print("*",end=" ")
    print()



def print_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage:
size = 20
print_hollow_square(size)



for row in range(0,5):
    for col in range(0,6):
        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or (row==2 and (col>=1 and col<5)))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()




doubt
for row in range(0,5):
    for col in range(0,6):
        if ((row==1 and col==0) or (row==2 and (col<=2 and col=1)) or (row==2 and (col>=1 and col<5))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



---> List

Primary
Number--->int,float complex
string
boolen
none

collection
list
tuple
set
dictionary


# List

#1). if the collection of elrments are sorrounded by square brackets, it is considered
#to be list
# eg:
# l1=[4,7,9,9.89,"hello",7+9j,[8,9,0]]

#characteristics of list
1). List have to be surrounded by []
2). it is mutable( the elements in the list are changable)
3). Every element inside list is indexed
4). the element inside list is will be ordered format
5). it can hold duplicatevalue
6). its heterogenous


to access the element of the list

l1=[1,4,1,7,7.5,"p","i"]
print(l1)



l1=["Usman","is","Alone","KING"]
print(l1)

 Indexing

the collection of datatype like list,tuple,string,the elements will be alloted
with prefines unique value called index value

we have 2types of indexing
positive indexing--> starts with 0 from left hand side
negative indexing --> strts with -1 from right hand side





l1=["my","heart","is","Totally","BRoked"]
l2=["thanks","For","Leaving","Me","without","telling"]
print(l1)
print(l2)

# Slicking
lst1=[1,4,2,7.5,"p","i"]
#lst1[start_index:end_index:step]
#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
print(lst1[0:7:2])

lst1=[1,4,1,7,7.5,"p","i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4]) #--->[]
#print(lst1[-7:-1])
#print(lst1[-5:-3])
print(lst1[4:6])

'''

# To insert at add element inside list

# append()
l1=[9,8,0,6,5]
l1.append("Usman")
print(l1)











