# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:14:34 2018

@author: SBOHORA
"""

a = 0
b = 1

for i in range(0,10):
    print(a)
    a, b = b, a + b
    #a = b
    #a,b = b, a + bR
    
my_dict = {'name': 'Bronx', 'age':2,'Occupation':'Statistician'}

for key, val in my_dict.items():
    print("My " + key + " is " + str(val))
    print("My {} is {}".format(key, val))
    
    
class Restaurant(object):
    bankrupt = False
    def open_branch(self): # this is same as this in C# and Java, self is not a reserved word
        if not self.bankrupt:
            print("branch opened")
            
            
x = Restaurant()
x.bankrupt = True
x.open_branch()


def build_profile(first, last, **user_info):
    profile = {'first': first, 'last': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_0 = build_profile('albert', 'einstein',location='princeton')
user_1 = build_profile('marie', 'curie',location='paris', field='chemistry')
print(user_0)
print(user_1)


def make_pizza(size, *toppings):
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers','onions', 'extra cheese')

import snake_case

snake_case.snake_case("Hi______   _____ There hrllo")


lst=[10, 20, 30, 40, 50]

lst[-2:]

lst[1:4] = [15,45,46]

lst
x=4
y =6
print("v=",3,"cm :",x,",",y+4)

lst = [11,18,9,12,23,4,17]
lost = []
for idx in range(len(lst)):
    val = lst[idx]
    if val > 15:
        lost.append(val)
        lst[idx] = 15
print("modif:",lst,"-lost:",lost)

for idx,val in enumerate(lst):
    print(idx,val)
'c'*5

my_dict.items()

'so2m'.isalpha()

def swap_case(x):
    m = []
    for i in x:
        if i.islower():
            m.append(i.upper())
            mm = ''.join(m)
        else:
            m.append(i.lower())
            mm = ''.join(m)
    return mm

swap_case('HackerRank.com presents "Pythonist 2".')

s = 'GNCHCDCDC'
s.startswith('CDC')

def count_substring(string, sub_string):
    sum_count = 0
    for i in range(len(string)):
        if string.startswith(sub_string, i):
            add = 1
            sum_count += add
    return sum_count

count_substring(s, 'CDC')  


n = 24
if n % 2 is not 0:
    print("Weird")
elif n <=5 and n >= 2:
    print("Not Weird")
elif n <=20 and 6 >= 2:
    print("Weird")
else:
    print("Not Weird")
    
n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}


n = 5
print("Not Werid" if not n%2 and (n in range(2,6) or n >20) else "Weird")

print("%s", "sdf")


print(''.join(map(str,list(range(1,n)))) + str(n))


for i in range(1, n + 1):
    print(i, end = '')


'rotor'[::-1] == 'rotor'


['r','r','y'][::3] = [i.upper() for i in ['r','r','y'][::-3]]

#String -- immutable
name = 'Sam'
name[0] = 'P'
'P' + name[1:]


print("This is a string {}".format('Inserted'))
print("the {2} {1} {0}".format('fox','brown','quick'))

print("This is a string {r:1.3f}".format(r = 0.235647)) #value:width.precision f
print(f"This is a string {name}")


1 is not 1

[2,3,4].insert

import re
string = "Important text,      !Comment that could be removed"
re.sub("!", "", string)


def alternate_letter_swap_case(args):
    return(''.join([args[i].lower() if i % 2 == 0 else args[i].upper() for i in range(len(args))]))

args = "Anthropomorphism"
alternate_letter_swap_case(args)

args.swapcase()

"som som".capitalize()

' '.join("I am home".split()[::-1])

x = "Mississippi"
''.join([char*3 for char in x])


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('e')

#Map
def square(num):
    return(num**2)
    
my_nums = [2,3,4,5]
for item in map(square, my_nums): print(item)
list(map(square, my_nums))

#filter
def slicer(x):
    return(x % 2 == 0)
list(filter(slicer, my_nums))

#Lambda expression/anonymous function
square = lambda num: num ** 2
square(2)

list(map(lambda num: num **2, my_nums))
list(filter(lambda num: num % 2 == 0, my_nums))

names = ['sam','hari','lyam']
list(map(lambda x: x[0], names))



#functions
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())

ispangram("The quick brown fox jumps over the lazy dog")


{1,2,3} <= {2,3,1}

set(string.ascii_lowercase) <= set("The quick brown fox jumps over the lazy dog".lower())
