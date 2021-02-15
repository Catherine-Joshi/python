'''
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print("Numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 : ")
print (','.join(nl))

s = input("Input a string : ")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters : ", l)
print("Digits : ", d)


def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print("The length of the string is ",string_length('Python Programming'))

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print("The number of characters are \n",char_frequency('Classmate'))
'''
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)
