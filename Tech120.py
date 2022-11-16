from random import randint as rd

questiondict = {}
ans ={1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
topic ={1:'integral', 2:"derivative", 3:"limit", 4:"optimization"}
progress ={'integral':0, "derivative":0, "limit":0, "optimization":0}
mastered = {}
for i in range(1,80):
    questiondict[i] = [str(i),rd(1,6),ans[rd(1,5)],topic[rd(1,4)]]

print (questiondict)

def ask():
    question = rd(1,79)
    print(question)
    print("Question difficulty is " + str(questiondict[question][1]))
    return question

def checkans(question):
    temp = questiondict[question]
    print("Question is: " + temp[0])
    correctans = temp[2]
    user = input("Select correct answer:")
    current_difficulty = temp[1]
    if user == correctans:
        print("Correct Answer!")
        if current_difficulty != 0:
            temp[1] -= 1
        else:
            print("Question mastery achieved!")
            mastered[question] = questiondict.pop(question)
    else:
        print("Incorrect!")
        temp[1] +=1

#checkans(ask())

#print (questiondict)
#print (mastered)



def progression():

    for i in questiondict:
        progress[questiondict[i[3]]]+=questiondict[i[2]]
    print(progress)
        


progression()