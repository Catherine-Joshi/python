#prgm1

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
max = max_of_three(3, 6, 10)
print("The maximum of three numbers are ", max)


#prgm2
'''
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 5, 7)))
'''
#prgm3
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print("The factorial is ",factorial(n))
'''
#prgm4
'''
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('India is my Country')
'''
#prgm5
'''
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('onion'))
'''
#prgm6
'''
color_list = []   
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input("Enter color : ")
    color_list.append(ele)
print("List of colors : ",color_list)
print( "The first color is %s and last color is %s"%(color_list[0],color_list[-1]))
'''
#prgm7
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("List 1 : ",color_list_1)
print("List 2 : ",color_list_2)
print("colors from list1 not contained in list2 : ",color_list_1.difference(color_list_2))
'''
#prgm8
'''
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print("Dictionary 1 : ", d1)
print("Dictionary 1 : ", d2)
print("After merging : ",d)
'''
