from Hikisu import playerargs, pydb, pydbz, pydbs
from Kurasu import zFighter
import random

lst = [pydb, pydbz, pydbs]

#This is the guessing game
def quest(names):
    while playerargs.attempt != playerargs.guessLimit:
        validQuestion = False

#so while this boolean is flase it will keep asking a question
        if validQuestion != True:
            print("When was {} introduced? Db/Dbz/Dbs:\n".format(names.name))
            guess = input("What will be your answer?: ").capitalize()
            playerargs.raiseGuess()

# After the user answer the following code will run and check if it's right.
            if guess == names.show:
                validQuestion = True
                playerargs.raiseScore()
                break

#If it isn't right this code will run instead
            if guess != names.show:
                validQuestion = False
                print("incorrect buddy")

#Depending on the points gathered during the game this will the final message
def scoreTotal():
    if playerargs.score == 6:
        print("Congratulations, Your a DbGenuis!")
    elif playerargs.score == 4:
        print("Almost Had 'em all!")
    elif playerargs.score == 2:
        print("ahh you can do better")
    else:
        print("you failed me")

# This is the Function to shufle the game.
def Game(first, second, third):
    questions = [quest(random.choice([first,second,third])),
    quest(random.choice([first,second,third])),
    quest(random.choice([first,second,third]))]

    random.shuffle(questions)

#This code is supposed to stop the game from producing duplicate questions
    if first == pydb or pydbz or pydbs:
        lst.remove(first)

        if second == pydb or pydbz or pydbs:
            lst.remove(second)

            if third == pydb or pydbz or pydbs:
                lst.remove(third)