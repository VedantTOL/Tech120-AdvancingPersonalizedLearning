from random import randint as rd
import random



#question bank initialized as dictionary
#temporary dict with answers (for randomization; remove when actual question bank is created)
ans ={1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
topic ={'Limits and Continuity': [0, 0], 'Derivatives: Definition and Basic Rules': [0, 0], 'Derivatives: Chain Rule and Other Advanced Topics': [0, 0], 'Applications of Derivatives': [0, 0], 'Analyzing Functions': [0, 0], 'Integrals': [0, 0], 'Differential Equations': [0, 0], 'Applications of Integrals': [0, 0]}

questiondict = {1: ['Limits and Continuity', ('Question', 'Limit as x -> -9 of (x^2-81)/(x+9)'), ('Correct Answer', '-18'), ('Wrong Answer 2', '-24'), ('Wrong Answer 3', '28'), ('Wrong Answer 4', '18'), ['Difficulty', 2]], 2: ['Limits and Continuity', ('Question', 'Limit as x -> 2 of (-5x)/sqrt(5x-6)'), ('Correct Answer', '-5'), ('Wrong Answer 2', '-4'), ('Wrong Answer 3', '5'), ('Wrong Answer 4', '10'), ['Difficulty', 4]], 3: ['Limits and Continuity', ('Question', 'Limit as x -> -3 of (3(2x+1)^2 -75)/(x+3)'), ('Correct Answer', '-60'), ('Wrong Answer 2', '60'), ('Wrong Answer 3', '50'), ('Wrong Answer 4', '-50'), ['Difficulty', 3]], 4: ['Limits and Continuity', ('Question', 'Limit as x -> 0 of (sqrt(16+h)-4)/h'), ('Correct Answer', '1/8'), ('Wrong Answer 2', '1/7'), ('Wrong Answer 3', '1/6'), ('Wrong Answer 4', '1/5'), ['Difficulty', 2]], 5: ['Limits and Continuity', ('Question', 'Limit as x -> 2 of (x-2)/(sqrt(3x+10)-4)'), ('Correct Answer', '8/3'), ('Wrong Answer 2', '4/3'), ('Wrong Answer 3', '3/4'), ('Wrong Answer 4', '1/2'), ['Difficulty', 4]], 6: ['Derivatives: Definition and Basic Rules', ('Question', 'Find the derivative of (15x^5 -27x +e^2)\\'), ('Correct Answer', '75x^4-27'), ('Wrong Answer 2', '75x^4'), ('Wrong Answer 3', '15x^4-27'), ('Wrong Answer 4', '75x^4-27+2e'), ['Difficulty', 2]], 7: ['Derivatives: Definition and Basic Rules', ('Question', 'Find the derivative of => 14sqrt(x)'), ('Correct Answer', '7/sqrt(t)'), ('Wrong Answer 2', '28/sqrt(t)'), ('Wrong Answer 3', '7/t'), ('Wrong Answer 4', '14/t'), ['Difficulty', 2]], 8: ['Derivatives: Definition and Basic Rules', ('Question', 'Find the derivative of (sqrt(3x+7))'), ('Correct Answer', '3/(2sqrt(3x+7))'), ('Wrong Answer 2', '1/2sqrt(3x+7)'), ('Wrong Answer 3', '1/3sqrt(3x+7)'), ('Wrong Answer 4', '2/3sqrt(3x+7)'), ['Difficulty', 3]], 9: ['Derivatives: Definition and Basic Rules', ('Question', 'Find the derivative of (6x^4+9x^3+7x)'), ('Correct Answer', '24x^3 + 27x^2 + 7'), ('Wrong Answer 2', '6x^3+9x^2 +7'), ('Wrong Answer 3', '24x^2 + 9x'), ('Wrong Answer 4', '24x^3+9x^2+7'), ['Difficulty', 2]], 10: ['Derivatives: Definition and Basic Rules', ('Question', 'Find the derivative of ((3x+4)(2x^2+1))'), ('Correct Answer', '18x^2+16x+3'), ('Wrong Answer 2', '17x^2+8x+3'), ('Wrong Answer 3', '12x^2+8x+3'), ('Wrong Answer 4', '12x^2+10x+3'), ['Difficulty', 3]], 11: ['Derivatives: Chain Rule and Other Advanced Topics'], 12: ['Derivatives: Chain Rule and Other Advanced Topics'], 13: ['Derivatives: Chain Rule and Other Advanced Topics'], 14: ['Derivatives: Chain Rule and Other Advanced Topics'], 15: ['Derivatives: Chain Rule and Other Advanced Topics'], 16: ['Applications of Derivatives'], 17: ['Applications of Derivatives'], 18: ['Applications of Derivatives'], 19: ['Applications of Derivatives'], 20: ['Applications of Derivatives'], 21: ['Analyzing Functions'], 22: ['Analyzing Functions'], 23: ['Analyzing Functions'], 24: ['Analyzing Functions'], 25: ['Analyzing Functions'], 26: ['Integrals'], 27: ['Integrals'], 28: ['Integrals'], 29: ['Integrals'], 30: ['Integrals'], 31: ['Differential Equations'], 32: ['Differential Equations'], 33: ['Differential Equations'], 34: ['Differential Equations'], 35: ['Differential Equations'], 36: ['Applications of Integrals'], 37: ['Applications of Integrals'], 38: ['Applications of Integrals'], 39: ['Applications of Integrals'], 40: ['Applications of Integrals']}
#tracking progress of topics stores correct attempts and total attempts
{'Limits and Continuity': [0, 0], 'Derivatives: Definition and Basic Rules': [0, 0], 'Derivatives: Chain Rule and Other Advanced Topics': [0, 0], 'Applications of Derivatives': [0, 0], 'Analyzing Functions': [0, 0], 'Integrals': [0, 0], 'Differential Equations': [0, 0], 'Applications of Integrals': [0, 0]}

#question mastery => if questions reach level 0 difficulty
mastered = {}

def populate_topic():
    x=6
    for i in range(x,x+5):
        for k in range(1,7):
            print(str((questiondict[i])))
            if k ==1: 
                questiondict[i].insert(1,("Question",input("Question: ")))
            elif k ==2:
                questiondict[i].insert(2,("Correct Answer",input("Correct: ")))
            elif k>=3 and k <=5:
                questiondict[i].insert(k,("Wrong Answer " + str(k-1),input("Ans: ")))
            elif k ==6:
                questiondict[i].insert(6,["Difficulty",input("Difficulty: ")])
            else:
                pass
#creating question bank with random values

def topic_pop():
    for i in range(1,41):
        questiondict[i] = ['topic',]
        if i<=5:
            questiondict[i][0] = "Limits and Continuity"
        elif i<=10:
            questiondict[i][0] = "Derivatives: Definition and Basic Rules"
        elif i<=15:
            questiondict[i][0] = "Derivatives: Chain Rule and Other Advanced Topics"
        elif i<=20:
            questiondict[i][0] = "Applications of Derivatives"
        elif i<=25:
            questiondict[i][0] = "Analyzing Functions"
        elif i<=30:
            questiondict[i][0] = "Integrals"
        elif i<=35:
            questiondict[i][0] = "Differential Equations"
        elif i<=40:
            questiondict[i][0] = "Applications of Integrals"
#populate_topic()
    
#print (questiondict)

#dictionary info
#key => question number (easy to track)
#values are a in list 
#list legend ["question",level,"correct answer","topic"]



#asks the question
def checkans(index):
    print("")
    complete = questiondict[index] #stores list in temporary variable for easy access
    current_topic = complete[0]
    print(current_topic)
    question = complete[1]
    question = question[1]
    print(question)
    correct = complete[2][1]
    current_difficulty = complete[6][1]
    print("The difficulty of this question is: " + str(current_difficulty))
    print("")
    #print(correct)
    options = [complete[x][1] for x in range (2,6)]
    random.shuffle(options)
    print("The options are: (Pick a number between 1 and 4)")
    print(options)
    print("")
    user = int(input("Select correct answer:")) #user inputs chosen answer
    if str(options[user-1]) == str(correct):
        print("Correct Answer!")
        if current_difficulty != 0: #if correct reduces level
            (complete[6][1]) -= 1 
        else: #if the level is already 0, it adds the question to mastery dictionary
            print("Question mastery achieved!")
            mastered[question] = questiondict.pop(question)
        topic[current_topic][1] +=1 #adds one to number of attempts and correct answers
        topic[current_topic][0] +=1 #adds one to number of attempts and correct answers
    else:
        print("Incorrect!") #increases difficulty by one
        complete[6][1] +=1
        topic[current_topic][1] +=1 #adds one to the number of attempts in that topic

def questioncount():
    return int(input("How many questions would you like to answer?"))



while True:
    print("Menu Options:")
    print("1. Ask random questions")
    print("2. Ask questions from a specific topic")
    print("3. Ask questions of particular difficulty")
    print("4. Track progress")
    print("5. Exit")
    menu = int(input("Select Option (1-5): "))
    if menu ==1:
        for i in range(questioncount()):
            checkans(rd(1,11))
    elif menu ==2:
        topicChoice = input("Which topic would you like questions from: ")
        for i in range(1,11):
            if topicChoice == questiondict[i][0]:
                checkans(i)
    elif menu ==3:
        difficultyChoice = int(input("Which level of questions would you like to solve: "))
        for i in range(1,11):
            if difficultyChoice == questiondict[i][6][1]:
                checkans(i)
    elif menu ==4:
        print(topic)
        print(mastered)
    elif menu ==5:
        print("Thank you! Goodbye!")
        break
    else:
        print("invalid input! try again.")

