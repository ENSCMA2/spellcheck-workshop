myFirstVariable = 5 #int
print(myFirstVariable)
myFirstVariable = 6.7 #float
print(myFirstVariable)
myFirstString = 'this is a string'
print(myFirstString)
myBoolean = (4<5)
print(myBoolean)

x = 5; y = 7
y = y+1; y -= 1
z = x+y; print('z = ' + str(z))
w = x-y; print('w = '+ str(w))
a = w*z; print('a = ' + str(a))
b = w/z; print('b = ' + str(b))

myFirstBool = (4 == 5)
mySecondBool = (56*4 < 65*5)
print(myFirstBool)
print(mySecondBool)
print(myFirstBool and mySecondBool)
print(myFirstBool or mySecondBool)
print(not myFirstBool)
myFirstBool = (4 <= 5 and (5 >= 4 or not 6 == 7))
print(myFirstBool)

myFirstList = [1,2,3,4]; print(myFirstList[0])
print(myFirstList[-1])
myFirstList[3] = 5; print(repr(myFirstList))
myFirstList.append(5); print(repr(myFirstList))

print('last two: ' + repr(myFirstList[3:5]))
print('skipping by twos: ' + repr(myFirstList[0:5:2]))
print('first two: ' + repr(myFirstList[:2]))
print('3rd item onwards: ' + repr(myFirstList[2:]))

listInList = [[1, 2, 3], [4,5,6],[7,8,9]]
print(listInList[0][1])
print(len(listInList))
print(set(myFirstList))

sentence = 'I love natural language processing.'
splitSentence = sentence.split()
print(repr(splitSentence))
sentenceJoinedBackTogether = ' '.join(splitSentence)
print(sentenceJoinedBackTogether)
print(sentenceJoinedBackTogether[1:5])

myMultilineSentence = ''' I really
really love
NLP.'''
print(myMultilineSentence)
mySpecialSentence = 'I\'m so \nspecial \ttoday.'
print(mySpecialSentence)
print(len(mySpecialSentence))

myFirstDict = {'chocolate': 'yes', 'cheese': 'meh', 'vegetable': 'nope'}
print(myFirstDict); print(myFirstDict['chocolate'])
myFirstDict['apples'] = 'keep the doctor away'
print(myFirstDict)
del myFirstDict['cheese']
print(myFirstDict)

from collections import Counter

myCountingList = ['dog', 'dog', 'cat', 'cat', 'cat', 'fry', 'leopard', 'bread', 'bread']
myFirstCounter = Counter(myCountingList)
print(myFirstCounter)

for i in range(10):
 print(i)
for number in myFirstList:
 print(number+1)
for i in myFirstDict:
 print(i, myFirstDict[i])
for i in listInList:
 for j in i:
   print(j)
myFirstTuple = (1, 2)
listOfTuples = [(1, 2), (3, 4), (5, 6)]
for x, y in listOfTuples:
    print(x + y)

n = 6
while n > 1:
    print(n)
    n -= 1

def average(numbers):
 total = 0
 for i in numbers:
   total += i
 return total/len(numbers)

print(average([1,2,3,4,5,6]))

slightlyFancyList = [i for i in range(12)]
print(repr(slightlyFancyList))
slightlyFancierList = [i for i in range(12) if i % 2 == 0 and i != 4]
print(repr(slightlyFancierList))
reallyFancyList = [average(i) for i in listInList if average(i) > 3]
print(repr(reallyFancyList))

