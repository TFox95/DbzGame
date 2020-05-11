class zFighter():
    
    def __init__(self, name, show, isAFighter):
        self.name = name
        self.show = show
        self.isAFighter = isAFighter


class parameter():
# This line is to set the constant variables
  def __init__(self, attempt, score, guessLimit):
    self.attempt = attempt
    self.score = score
    self.guessLimit = guessLimit
#This func is to add to the score
  def myScore(self):
    self.score += 2
#This func is to add to the userAtempts    
  def myAttempt(self):
    self.attempt += 1
