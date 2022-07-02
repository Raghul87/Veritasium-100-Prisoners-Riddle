from random import randint, shuffle 

totalPrisoners = 100
attemptsCount = totalPrisoners/2
trialsCount = 10000
# ================================================================ #
# Go for the Random Pick #
# ================================================================ # 

percentagesRates = {True: 0, False: 0}
prisoners = []

for i in range(1,totalPrisoners+1):
    prisoners.append(i)
boxes = prisoners.copy()

for i in range(trialsCount):
    shuffle(boxes)
    shuffle(boxes)
    shuffle(boxes)
    totalSuccess = [] 

    for i in range(1,totalPrisoners+1):
        choices = []
        success = False  

        while(len(choices) != attemptsCount):
            randomNo = randint(1,totalPrisoners)
            if randomNo not in choices:
                choices.append(randomNo) 
                if boxes[randomNo-1] == i:
                    success = True
                    break
        totalSuccess.append(success)       

    if False in totalSuccess:
        percentagesRates[False] = percentagesRates.get(False) + 1
    else:
        percentagesRates[True] = percentagesRates.get(True) + 1 

print("Success " + str((percentagesRates.get(True) / trialsCount) * 100))
print("Failure " + str((percentagesRates.get(False) / trialsCount) * 100)) 

# ================================================================ #
# Go for the Loop Pattern #
# ================================================================ # 

percentagesRates = {True: 0, False: 0}
for i in range(trialsCount):
    shuffle(boxes)
    shuffle(boxes)
    shuffle(boxes) 

    totalSuccess = []
    for i in range(1,totalPrisoners+1):
        loopChoices = []
        success = False
        nextInt = i  

        while(len(loopChoices) != attemptsCount):
            loopChoices.append(nextInt)
            if boxes[nextInt-1] == i:
                success = True
                break
            else:
                nextInt = boxes[nextInt-1]
        totalSuccess.append(success)       

    if False in totalSuccess:
        percentagesRates[False] = percentagesRates.get(False) + 1
    else:
        percentagesRates[True] = percentagesRates.get(True) + 1 

print(" ")
print("Success " + str((percentagesRates.get(True) / trialsCount) * 100))
print("Failure " + str((percentagesRates.get(False) / trialsCount) * 100))