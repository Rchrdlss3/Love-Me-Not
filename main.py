import random
from random import randint

##### Name of person
x = " "
### Positive and Negative questions

results = 0
qAnswered = 0
posQ = ['make an effort to spark a conversation ?', 'Lean towards you when you are together ?','remember small details?', 'seem nervous around you ?','make time for you ?','make eye contact ?','always makes jokes around you ?']
negQ = ['close themselves with their body language ?','give a smile that is not sincere ?','mirror you ?','look you in the eyes ?','close conversations ?','make plans with you ?','listen to you ?','only respond with emjois when texting ?']



def start():
    global x
    ques = input ("Who do you think has a crush on you ?: ")
    x = ques     
    main()

def main():
    global ranPosQ
    global results
    global x
    global qAnswered

    while qAnswered <10:
        ranPosQ = posQ[random.randint(0,len(posQ)-1)]
        ranNegQ = negQ[random.randint(0,len(negQ)-1)]
        randomQ = [ranPosQ,ranNegQ]
        randInt =  random.randint(0,1)
        print('Does ' + x + ' ' + str(randomQ[randInt]))
        answer = input().lower()
        qAnswered += 1
        if answer == ('yes') and randInt == 0:
            results += 10
        elif answer ==('no') and randInt == 1:
            results += 10
        elif answer ==('no') and randInt == 0:
            results -= 10
        elif answer == ('yes') and randInt ==1:
            results -=10
        else:
            print("Invalid response. Only 'yes' or 'no'. Please try again.")
            qAnswered -= 1
    if results <50:
        print("There's a " + str(results) + "% chance that " + x + " likes you. It's not worth it")
    elif results >=80: 
        print("There's a " + str(results) + "% chance that " + x + " REALLY likes you.")
    else:
        print("There's a " + str(results) + "% chance that " + x + " likes you. ")

start()

