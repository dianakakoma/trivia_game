import json

with open("trivia_data.json") as read_file:
    data=json.load(read_file)
    #print(data)

score = 0
print()
print(data[0]['question'])
#print("Answer Options:", data[0]['incorrect'], "or ", data[0]['correct'])

wrongAnswers = data[0]['incorrect']
rightAnswers = data[0]['correct']
#print("Right answers: ",rightAnswers)
#print("Wrong answers: ",wrongAnswers)

allOptions = (*wrongAnswers, rightAnswers)
print()
print("Answers: ")

#listing out each of the answer options
#for item in allOptions:
    #print(item)

#assigning a number to each possible response
optionNum = 0

while optionNum <= len(allOptions)-1:

    #print(optionNum,'-',allOptions[optionNum])
    print(allOptions[optionNum])
    optionNum += 1

   
answer = input("What is your guess? (copy and paste your final answer)")
if answer == "Devmynd":
    print("One point for you!")
    score += 1
    print("Your score is: ", score)
else:
    print("Better luck next time!")

