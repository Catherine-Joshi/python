#prgm1
'''
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b
'''
#prgm 2

list = [1,2,3,4,5]
print("The sum of the list is ",sum(list))

#prgm3
'''
rows = int(input("Enter the number of rows: "))

for i in range(1, rows):

    for j in range(1, i + 1):

        print(i * j, end=' ')

    print()
'''
#prgm4
'''
test = "I love my country"
 
frequency = {} 
  
for i in test: 
    if i in frequency: 
        frequency[i] += 1
    else: 
        frequency[i] = 1

print ("Count of all characters:\n "+  str(frequency)) 
'''
#prgm5
'''
def long_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = long_word(["Ammu", "Book", "Google"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
'''
#prgm6
'''
n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
'''
#prgm7
'''
def factor(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 20
factor(num)
'''
