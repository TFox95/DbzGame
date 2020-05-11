from arguments import playerargs,vegeta as vg
def quest(name, shows):
    while playerargs.userAttempt != playerargs.guessLimit:
        validQuestion = False
#so while this boolean is flase it will keep asking a question
        if validQuestion != True:
            print("When was {} introduced? Db/Dbz/Dbs:\n".format(vg.name))
            guess = input("What will be your answer?: ".capitalize())
            playerargs.myAttempts

            if guess == shows:
                validQuestion = True
                playerargs.myScore
                break
#Depending on the points gathered during the game this will the final message
def scoreTotal():
    if playerargs.userScore == 6:
        print("Congratulations, Your a DbGenuis!")
    elif playerargs.userScore == 4:
        print("Almost Had 'em all!")
    elif playerargs.userScore == 2:
        print("ahh you can do better")
    else:
        print("you failed me")
#quest(vg.name,vg.show)
#scoreTotal()
playerargs.myAttempts
print(playerargs.userAttempt)