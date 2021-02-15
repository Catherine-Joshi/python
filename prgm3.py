#prgm1
'''
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY'))

'''

#prgm2
'''
names = ["Manu","Vishnu","Samuel","Keerthana","Sivan"]
count = 0
letter = "a"
for x in range(0,len(names)):
    for y in range(0,len(names[x])):
        if letter == names[x][y]:
            count = count + 1
print("Number of occurence of a : ",count)
'''

#prgm3
'''
list1 = [1,3,5,7,9,11]
list2 = [2,3,6,8,9]
if len(list1) == len(list2):
    print("Both list have same length.")
else :
    print("Lists are of different length")
if sum(list1) == sum(list2):
    print("Sum of both list are same")
else :
    print("List not sums to have same value")
if any(check in list1 for check in list2):
    print("List have same values")
else :
    print("List does not have same value")

'''
#prgm4
'''
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
'''
#prgm5

'''
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
'''

#prgm6
'''
n = int(input("Enter a number n: "))
n1 = str(n)
t1 = n1+n1
t2 = n1+n1+n1
value = n+int(t1)+int(t2)
print("The value is:",value)
'''

#prgm7
'''
import operator
d = {1: "anu", 3: "bibin", 4: "vinu", 2: "manu", 0: "sree"}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
'''

#prgm8

list = [11, 22, 33, 44, 55]
print("Original list:")
print(list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print("list after removing EVEN numbers:")
print(list)





























