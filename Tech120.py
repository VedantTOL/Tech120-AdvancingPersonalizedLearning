from random import randint as rd



questiondict = {} #question bank initialized as dictionary

#temporary dict with answers (for randomization; remove when actual question bank is created)
ans ={1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
topic ={1:'integral', 2:"derivative", 3:"limit", 4:"optimization"}

#tracking progress of topics stores correct attempts and total attempts
progress ={'integral':[0,0], "derivative":[0,0], "limit":[0,0], "optimization":[0,0]}

#question mastery => if questions reach level 0 difficulty
mastered = {}

#creating question bank with random values
for i in range(1,20):
    questiondict[i] = [str(i),rd(1,6),ans[rd(1,5)],topic[rd(1,4)]]

print (questiondict)

#dictionary info
#key => question number (easy to track)
#values are a in list 
#list legend ["question",level,"correct answer","topic"]

#asks a random question
def ask():
    question = rd(1,20)
    print(question)
    print("Question difficulty is " + str(questiondict[question][1]))
    return question

#checks if answer is correct
def checkans(question):
    temp = questiondict[question] #stores list in temporary variable for easy access
    print("Question is: " + temp[0]) #prints question
    correctans = temp[2] #index of correct ans from temp storage variable
    user = input("Select correct answer:") #user inputs chosen answer
    current_difficulty = temp[1] #stores difficulty of variable
    current_topic = temp[3]
    if user == correctans:
        print("Correct Answer!")
        if current_difficulty != 0: #if correct reduces level
            temp[1] -= 1 
        else: #if the level is already 0, it adds the question to mastery dictionary
            print("Question mastery achieved!")
            mastered[question] = questiondict.pop(question)
        progress[current_topic][1] +=1 #adds one to number of attempts and correct answers
        progress[current_topic][0] +=1 #adds one to number of attempts and correct answers
    else:
        print("Incorrect!") #increases difficulty by one
        temp[1] +=1
        progress[current_topic][1] +=1 #adds one to the number of attempts in that topic

checkans(ask())

#print (questiondict)
#print (mastered)


print(progress)