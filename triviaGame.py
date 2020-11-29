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
for i in allOptions:
    print(i)

