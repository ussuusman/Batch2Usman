# !). Python program to capitalize the first and last charcater of each
#s1='hello world'
#fst=s1[0].upper()
#l1=s1[-1].upper()
#print(fst+s1[1:10]+l1)
#print(s1.capitalize())
#print(s1.swapcase())


#  2). ex

#Input:128
#output: yes
#128%1==0, 128 % 2==0, and 128 % 8==0
'''

n=128
if n % 1==0 and n % 2==0 and n % 8==0:
    print("yes")
else:
    print("No")

n=128
temp = n
f1 = 0
while n!=0:
    rem = n%10
    check = temp % rem
    if check!=0:
        f1=1
    n = n//10

if f1==0:
    print("yes")
else:
    print("no")


# 3).
l1=[1,2,3,4]
l2=[5,6,7,8]

#print(l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2],l1[3]+l2[3])
l3=[]
for val in range(len(l1)):
    ans1=l1[val]+l2[val]
    l3.append(ans1)
print(l3)



# ! -----> set
# characteristics of set
1.) set can be created using{}
2.) The element inside set are not indexed
3.) Does not allow duplicate values
4.) it unordered
5.) heterogenous ----> accept only unutable datatype
6.) mutable or changable

'''

# EX;1
#S1={9,9,89,7.76,8+7j,(8,7,5),"truck","e"}
#print(S1)


# ex:2
#s2={5,8,98,[9,0]}
#print(s2) #--->error

#Ex:3
# min(),max(),len()

# Ex;4
# to add elemrnt inside set
#s3={8,78,67,'u'}
#s3.add(43)
#print(s3)


#update()

#s3.update([9,7])
#print(s3)



#EX;5
# to delete element inside set
#pop() ---> #to delete one element randomly
#s3.pop()
#print(s3)

#remove()
#s3.remove(8)
#print(s3)

#discard()
#s3.discard(67)
#print(s3)


#clear()
#s3.clear()
#print(s3)

#s1={}
#print(type(s1))  #----> dist


#s1=set()
#print(type(s1))

#s1={8,9,5}
#s1.clear()
#del s1
#s1.del()

# join the sets
#s1={8,9,5}
#s2={8,78,67,789}
#union()  ---> to combine 2 sets
#s3=s1.union(s2)

#print(s3)


# intersection()--> to get common elements  insides set
#s1={8,9,5}
#s2={8,78,67,789}
#print(s1.intersection(s2))
'''
s1={8,9,5}
s2={8,78,67,789}
#print(s1.difference(s2))
#print(s2.difference(s1))
#print(s1.symmetric_difference(s2))

# isdisjoint() , issubset(), issupreset()
#print(s1.isdisjoint(s2))
#print(s1.issubset(s2))
#print(s1.issuperset(s2))
'''
'''
# ---> problem:1

s1={1,2,3,4,5}
s2={3,2,7,8,9}

#print(s1.isdisjoint(s2))
for val in s1:
    if val in s2:
        str1="Its joint set"
print(str1)




# ! ---> dictionary

# Ex:1
d1={1:100,'a':200,4.5:"hello"}
print(d1)
print(len(d1))



mech_name=["name1","name2","name3"]
mech_age=[23,22,24]
mech_mark=[89,78,60]
mech_email=["name2@gmail.com","name3@gmail.com"]

mech={
    "student1":"name1",
    "age":22,
    "mark":76,
    },
    "student2":{
        "name2",
        "age":21,
        "mark":45,
    },
    "student3":{
        "name3",
        "age":27,
        "mark":143,
    },
print(mech)


#d1={1:100,'a':200,4.5:"hello"}
#marks_stud1={"English":79,"Maths":20,"Physics":60}
#print(d1)

# ? Char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key, value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed, duplicate value are allowed
# 5.) It is unindexed
# 6.) It is ordered
# 7). key does allow mutable datable , value allow mutable datatype

d1={1:100,2:200,3:300,4:400}
# to acess elements in dictionary
#print(d1)
#or
# To acess the values, have to use key
print(d1[2]) #--> o/p is 200


d1={1:100,2:200,3:300,4:400}
# sum common functions
#len(),max(),min()
print(min(d1))
print(max(d1))




# ? To find min, max based on value
d1={1:100,2:200,3:300,4:400}
print(min(d1.values()))
print(max(d1.values()))




#  dictionary based functions

# to add element (key any value pair) in disc

d1={1:100,2:200,3:300,4:400}
d1[5]=500
print(d1)

'''
# To replace a value in dict
#d1={1:100,2:200,3:300,4:400}
#d1[2]="mango"
#print(d1)


# ? delete element from dict
# popitem()  --->  to dele the last ley value pair in dict
#d1.popitem()
#print(d1)

#pop()
#d1.pop(2) ---> 2 is the key value in dict
#print(d1)

# clear() , in dict

# join 2 dictionary
#d2={"a":"apple","b":"boy","c":"CAt"}
#d1.update(d2)
#print(d1)

# get() ---> used to get the value from a ley
#print(d1[3])
#print(d1.get(90))


#to print the all the keys()
#print(d1.keys())
#print(type(d1.keys()))

# to print all the values
#print(d1.values)

# Iterating dictionary
#for val in d1: # to iterate values alone
#    print(val)
    


#for val in d1.values():  # to iteratealues alone
#    print(val)

# to get both key and values
# Iterating dictionary
#for key, val in d1.items():
#    print(key,val)

# ! problrm:1

#n=input()

#1). Swap elemnts in String list
#2)> The original list is : ['gift','is', ;for','geeks']
# list after performing characteristics swaps:['gift','is','bGst']
'''
n=int(input("Enter of times:"))
integer=[]
float_value=[]
string=[]

for val in range(n):
    value=eval(input("Enter of times:"))
    if type(value)==int:
        integer.append(value)
    elif type(value) == float:
        float_value.append(value)
    elif type(value) ==str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)
'''
'''
# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}
set1 = {10, 20, 30, 40, 50,90}
set2 = {30, 40, 50, 60, 70}
set3=set()

#l1=set1 ^ set2
#print(l1)

for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)
'''

# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
'''
set1=[1,2,3]
set2=[1,2,3,4,5,6,7,8,9]
set3=set1 and set2
print(set3)


#!------> problem 3
l1=[1,2,3,4] # key
l2=["a", "b", "c", "d"] # value

#{1:'a'}
d1 = {}
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)
'''


# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}

# 3.)li
Siddharth T
4:12 PM
# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']


















