#aTuple = (10,20,30,40,50)
#bTuple = reversed(aTuple)
#print(tuple(bTuple))

#2

#aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
#print(aTuple[1][1])

#3

#aTuple=(50,)
#print(aTuple)

#4

#tuple1 = (11, 22)
#tuple2 = (99, 88)
#tuple1, tuple2 = tuple2, tuple1
#print("tuple1 = ", tuple1)
#print("tuple2 = ", tuple2)

#5

#tuple1 = (11, 22, 33, 44, 55, 66)
#tuple2 = tuple1[3:-1]
#print(tuple2)

#6

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Dictonary = dict(keys[0]+ values[0], keys[1]+ values[1], keys[2]+ values[2] )
print(Dictonary)

#7

#dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#dict3 = {**dict1, **dict2}
#print(dict3)

#8

#sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
#keysToextract = ["age", "city"]
#sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keysToextract}
#print(sampleDict)

#9


#sampleDict = {'a': 100, 'b': 200, 'c': 300}
#print(200 in sampleDict.values())

#10

#sampleDict = {
#'emp1': {'name': 'Jhon', 'salary': 7500},
#'emp2': {'name': 'Emma', 'salary': 8000},
#'emp3': {'name': 'Brad', 'salary': 6500}}
#sampleDict['emp3']['salary'] = 8500
#print(sampleDict)


























