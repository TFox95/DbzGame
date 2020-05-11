from arguments import playerargs, vegeta , goku, dict

#This is the guessing game
def quest(name, shows):
    while playerargs.attempt != playerargs.guessLimit:
        validQuestion = False
#so while this boolean is flase it will keep asking a question
        if validQuestion != True:
            print("When was {} introduced? Db/Dbz/Dbs:\n".format(name))
            guess = input("What will be your answer?: ").capitalize()
            playerargs.myAttempt()
# After the user answer the following code will run and check if it's right.
            if guess == shows:
                validQuestion = True
                playerargs.myScore()
                break
#If it isn't right this code will run instead
            if guess != shows:
                validQuestion = True
                print("incorrect buddy")
                break

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
