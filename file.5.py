#l1=[6, 7, 8, 9, 0]
#print(len(11))
#print(max(11))
#print(min(11))

#l1=[6, 8, 9, "p", "u"]
#print (max(11)) # --> error coz its a combination of list and string
#11 [6, 8, 9, "p", "u"]
#print(max(11)) #> error coz its a combination of int and string
#print(min(11)) #> еггor coz its a combination of int and string
#11 [6, 7, 8, 9, 8, 8.89, 5, 8.78]
#print(min(11)) #5
#11=[6, 7, 8, 9, 8, 8.89, -5, 0.78] #index() --> to get index value of specific element
#print(11.index(9))
#l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
#count()
#print(l1.count(6))

# some functions which is specially used for list

# to add element inside list
'''
#? insert(index_value, element) -> to add element at specific index position
l1=[6,6,6, 7, 8, 9, 0, 8.89, 5, 0.78]
l1.insert(2, "cars")
print(11)





# ? to delete element from list
l1=[6,6,6, 7, 8, 9, 0, 8.89, 5, 0.78]
l1.pop()
print(l1)





# "pop(index_value) --> used to delete element at specific index
#11.pop(4) # 4 is index value
# print(11)
# *remove(element)-> used to delete element directly
#11.remove(8.89)
# print(11)

#clear() -> to complete delete all element in list
#l1.clear()
#print(l1)

#del -> to delete the list
# del 1
#print(l1)


# ? --> join 2 lists

l1=[9,0,8]
l2=["p","o","t",34]
print(l1+l2)


#or
# extend ()---> to combine 2 lists
l1=[9,0,8]
l2=["p","o","t",34]
l1.extend(l2)
print(l1)



#   ?----> copy()

l1=[6,5,8,3,9,5]
l2=l1.copy()
#print(l2)
#print(l1)

#print(id(l1))
#print(id(l2))

# ! diff between shallow copy and deep copy
# shallow copy
import copy
l1=[8,9,0,[5,6],[3,2,1],890]
l2=copy.copy(l1)
l1.append(56)
print(l1)
print(l2)




# deep copy

import copy
l1=[8,9,0,[5,6],[3,2,1]]
#print(l1[-2][1])  ---> to index nexted list
l2=copy.deepcopy(l1)
l1[-1].append('car')
print(l1)
print(l2)



# ? sort --> arrange elements in list in ascending or desending order
l1=[9,7,45,2,-6,5,12]
#l1.sort()  #--- ascending
#print(l1)


l1.sort(reverse=True)   #--- desecding
print(l1)


l1=['z','i','o','p',9]
l1.sort()
print(l1)  #--error


# list constructor
list()
l3=((8,9,0))
print(list(l3))




#  Nested list
l1=[8,9,[0,8,7],['p','o','y'],[8,'t']]
#print(l1[-2][1])

#print(l1[1:4])

#print(l1[1:-1])

l1[-1].remove('t')
print(l1)


# combine these ["p","0","y"],[8,'t'] lists in l1
l1=[8,9,[0,8,7],['p','o','y'],[8,'t']]
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)


#  char of tuple

1).tuple have to be surrounde by ()
2.) The elemnts inside the tuple are not changable
3). the elemnts insided tuple are indexed
4). the elements will execute in order
5). It is hetrogeneous
6). it allow duplicate elements


# eg:1
t1=(8,8,9,6,5,[9,5,],(6,8),'hey',9+6j)
print(t1)
print(type(t1))

# indexing slicking are all same as list



l1=(8)
print(type(l1)) #int


l1=8,
print(type(l1))  # tuple

l1=8,9
print(type(l1))   #tuple




# len(),min(),index(),count() ---> all same as list

#to add element inside tuple ---> cannot add
#cannot delete any element from tuple

t1=(8,9,0)
t2=(6,7,8)
print(t1+t2)


#to add all element inside list and tuole
#sum()
t1=(8,9,0)
print(sum(t1))


# sort tuple

t1=(8,8,9,6,5)
#t1.sort()   # error

#print(tuple(sorted(t1)))  # asending
#print(tuple(sorted(t1,reverse=True))) #descendig


# iterate list aand tuples

t1=(8,8,9,6,5)
for i in t1:
    print(i)


# iterate based on indexed value
t1=[8,8,9,6,5,56,67]
for i in range(0,len(t1)):
    print(t1[i])


#  ! ----> Strings

s1='o'
print(type(s1))


s1="hello world"
# * To access string
#print(s1[5:])
# indexing and slicking --> same as list and tuple


common functions
len(0,min(),max(),index(),count()

#s1="hello world"
#print(len(s1))
#print(min(s1))
#print(max(s1))


# ord() ---> used to find the ascii value of acharacter
s1='u'
print(ord(s1))


# Functions of string
s1="hello world"

# to convert all characters to upper case

print(s1.upper())



#to convert the lower case
s1="FTFFUTF"
print(s1.lower())

'''

#   strip() ---> to eliminate the space in begining and end of string


#s1=" where are you? "
#print(s1.lstrip())
#print(s1.strip())



# split()---> to split the words in strings based on a character
#s1=" hey there dont sleep "
#print(s1.split(" "))

#print(s1.count('e'))
# * replace() ---. to replace a specic char in the strip
#print(s1.replace('r','&&'))


# swapcase()---> to convert capital to smalll and small to capital at a time
#s1="HEY there"
#print(s1.swapcase())


#*title() ---> to write the string in the fromat of title
#s1='i love you'
#print(s1.title())

# capitalize() ---> 1st char of string will be converted to capital
#s1='i love you'
#print(s1.capitalize())


# join the strings
#s1="hello"
#s2="world"
#print(s1+s2)

# splitline()--> used to split the string based on lines


#s1='''how are you
#i am fine
#hey there
#'''
#print(s1.splitline())


# Convert the string to a list of lines
#lines_list = s1.splitlines()

#print(lines_list)

# find() ---> to find the index based on acharacter
#dECfgvs1="hello world"
#print(s1.find('h'))
#print(s1.index('h'))
#print(s1.find('z'))


# join() --->
#l1=["hey","there"]
#print(" ".join(l1))
#print("$".join(l1))

#s1="welcome to all"
#print(s1.endswith('1'))
#print(s1.endswith('l'))

#s1="67"
#print(type(s1))
#print(s1.isdigit())


# print the string in reverse manner
#s1="Welcome to all"
#print(s1[::-1])


'''
#ex;1
s1="HEY there you aRE"
# wap to find the number of lower case letters

# Initialize a variable to store the count of lowercase letters
lowercase_count = 0

# Iterate through each character in the string
for char in s1:
    # Check if the character is a lowercase letter
    if char.islower():
        # If it is, increment the count
        lowercase_count += 1

print("Number of lowercase letters:", lowercase_count)


s1="HEY there you aRE"
count=0
for i in s1:
    if i.islower():
        count+=1
        print(" The total num of loer case letter:",count)



#eg:2 ----> "$"
s1='restarter'
fst=s1[0]
bal=s1[1:]
txt=bal.replace(fst,"$")
print(fst+txt)

'''

#str1="bbbbyybbshwghss"
#str2="%

#Ex:3

s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
s1=s1.strip()

print(len(s1))

words=s1.split(" ")
print(len(words))

sentenses = s1.split('.')
for val in sentenses:
    if val =='':
        index=sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))

space=0
for val in s1:
    if val ==" ":
        space=space+1
print(space)
