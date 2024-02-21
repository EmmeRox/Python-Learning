#name = input("What is your name? ")
#print("Hello, " + name)
#fundamental data types
int
float
bool
str
list
tuple
set
dict
#classes -> custom types
#specialized data types
None

#int and float
print(type(2 + 4))
print(type(2 / 4)) #is 0.5 which is a floating point number
print(5 // 4) #returns an integer rounded down

# math functions
print(round(3.1))
print(abs(-20)) #returns the absolute value of the argument

#operator precedence
print(20 - 3 * 4) #think pemdas

#variables
iq = 190
print(iq)

#no more camelcase here. use an underscore for multiword variables
user_iq = 190
#case sensitivity
#you can assign variables like this also
a,b,c = 1,2,3
print(a)
print(b)
print(c)
#statemnts and expressions
#iq = 9 vs 3/4
#augmented assignment operator which is a shorthand += or -=
some_value = 5
some_value += 2

#in python 3, strings can span mulitple lines
long_string = '''
WOW
0 0
---
'''
print(long_string)

#escaped sequences (similar to JS)
weather = "It\'s \"kind of\" sunny"

#formatted strings (the f at the beginning tells python to format the string)
name = 'Johnny'
age = 55
print(f'hi {name}. You are {age} years old')

#string indexes
selfish = '01234567'
# [start:stop:stepover]
print(selfish[0:8:2])
#a negative index means start at the end of the string
print(selfish[-1])
print(selfish[::-1])

#in python, variables are immutable. once assigned, a string cannot be changed unless you reassign the entire string in which case it'll be an entirely different data
#make a function that combines two names
def combine_names(first, last):
    return ' '.join([first, last])

#make a function that checks if a cube using only the volume and one side as information (some test cases contain negative numbers and 0's)
def cube_checker(volume, side):
    if side >= 0:
        total = side * side * side
        if total == volume and total !=0:
            return True
        else:
            return False
    else:
        return False # if cuboid is a cube or not
#below is a better writted function
def cube_checker(volume, side):
    if side>0 and volume>0:
        return True if side*side*side==volume else False
    else:
        return False
#and below is even better practice
def cube_checker(volume, side):
    return side > 0 and side ** 3 == volume

#tuple
my_tuple = (1,2,3,4,5)
#tuples are immutable lists
#you can use tuples as keys in dictionaries
print(5 in my_tuple)
print(my_tuple.index(5))
print(len(my_tuple))

#set
#unordered collections of unique objects
my_set = {1,2,3,4,5,5}
print(my_set)
#above only returns the unique values aka no duplicates like in above example
#the second 5 is not returned
#sets do not support indexing
print(1 in my_set)

is_magician = False
is_expert = True

if is_magician and is_expert:
  print('you are a master magician')
elif is_magician and not is_expert:
  print('at least you are getting there')
elif not is_magician:
  print('you need magic powers')

#new keyword: is
#is checks if the location in memory where the value is stored is the same
#data structures are created in different locations in memory

#for loops
for item in [1, 2, 3, 4, 5]:
    print(item)

#nesting is also allowed
for item in (1, 2, 3, 4):
    for x in ['a', 'b', 'c']:
        print(item, x)

#iterable means a collection (a list, a dictionary, a tuple) that can be iterated over
#iterate means go through one by one check each item
        
user = {
    name: 'Golem',
    age: 5000,
    'can_swim': False
}

for item in user.items(): #this dot notation gives the key value pairs from a dictionary
    print(item)

for key, value, in user.items():
    print(key, value)

#below an exercise
my_list = [1,2,3,4,5,6,7,8,9,10]

sum = 0

for item in my_list:
  sum = sum + item

print(sum)

#range is a special type of object that produces a sequence of intergers from start to stop
for number in range(0, 100):
    print(number)
#with this we looped 100 times
#also comes with a third parameter, how many to step by
for item in range(0, 10, 2): #a negative number in the third spot will run the list backwards
    print(item)