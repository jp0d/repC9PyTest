import random

def funRandomWords(num):
	setNum = set({})
	for i in range(0,5):
		setNum.add(random.randint(0, num))
	return setNum


fo = open("./rc1", "r")
para = fo.read()
lstPara = para.split()
lstPara = para.split()
lstWords = ['Words: -> ']
setIndex = funRandomWords(len(lstPara))
for number in setIndex:
	lstWords.append(lstPara[number])
	lstPara[number] = '_____'

print(" ".join(lstPara))
print(lstWords)


