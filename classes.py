#This is the created datatype of a Dragonball Character
class zFighter():
    
    def __init__(self, name, show, isAFighter):
        self.name = name
        self.show = show
        self.isAFighter = isAFighter

#This is the parameter inprint that the program will run by 
class parameter():
# This line is to set the constant variables
  def __init__(self, attempt, score, guessLimit):
    self.attempt = attempt
    self.score = score
    self.guessLimit = guessLimit

#This func is to raise the score by 2
  def raiseScore(self):
    self.score += 2

#This func is to add to the userAtempts    
  def raiseGuess(self):
    self.attempt += 1
