#prgm1

'''
def count_4(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 

lst = [4, 6, 4, 10, 4, 20, 10, 4, 4] 
x = 4
print('{} has occurred {} times'.format(x, count_4(lst, x))) 
'''

#prgm2
'''
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

'''
#prgm3 a
'''
list1 = [11, -21, 0, 45, 66, -93]   
for num in list1: 
    if num >= 0: 
       print(num, end = " ")
'''

#prgm3 b
'''
n = int(input("Enter the value of N :"))
for j in range(0, n):
    num = int(input("Enter number: "))
    square = num*num
    print(square)
'''

#prgm3 c
'''
elem = input("Enter any statement : ")
vowels =['a','e','i','o','u']
list1=[]
for x in elem:
    if (x in vowels and x not in list1):
        list1.append(x)
print("Vowels present in given statement : ",list1)

'''
#prgm4
'''
def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('python'))
'''

#prgm5

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)


















