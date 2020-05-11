class zFighter():
    
    def __init__(self, name, show, isAFighter):
        self.name = name
        self.show = show
        self.isAFighter = isAFighter


class parameter():
# This line is to set the constant variables
  def __init__(self, userAttempt, userScore, guessLimit):
    self.userAttempt = userAttempt
    self.userScore = userScore
    self.guessLimit = guessLimit
#This func is to add to the score
  def myScore(self):
    self.userScore += 2
#This func is to add to the guesslimit    
  def myAttempts(self):
    self.userAttempt += 1
