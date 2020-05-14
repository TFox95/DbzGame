from classes import parameter, zFighter
import random

#These are the character breakdowns
vegeta = zFighter("Vegeta", "Dbz", True)
goku = zFighter("Goku", "Db", True)
krillin = zFighter("Krillin", "Db", True)

#These are newly imported Db Characters
bulma = zFighter("Bulma", "Db", False)
korrin = zFighter("Korin", "Db", True)
chichi = zFighter("Chi-Chi", "Db", True)
oolong = zFighter("Oolong", "Db", False)
A8 = zFighter("Android 8", "Db", False)
piccolo = zFighter("piccolo", "Db", True)
roshi = zFighter("Master Roshi", "Db", True)

#Newly imoported Dbz Characters
nappa = zFighter("Nappa", "Dbz", True)
futureTrunks = zFighter("Future Trunks","Dbz", True)
raddiz = zFighter("Raddiz", "Dbz", True)
cell = zFighter("Cell","Dbz", True)
vegito = zFighter("Vegito","Dbz", True)
frieza = zFighter("Frieza","Dbz", True)
broly = zFighter("Broly", "Dbz", True) 

#Newly imported Dbs Characters
bulla = zFighter("Bulla", "Dbs", False)
beerus = zFighter("Beerus", "Dbs", True)
frost = zFighter("Frost", "Dbs", True)
hit = zFighter("Hit","Dbs",True)
jiren = zFighter("Jiren","Dbs",True)
zamatsu = zFighter("Zamatsu","Dbs",True)
zeno = zFighter("Lord Zeno","Dbs",False)
vados = zFighter("Vados","Dbs",True)
chompa = zFighter("Chompa","Dbs",True)

#These are the player's basic arguments; user attempts, score, guess limit
playerargs = parameter(0,0,4)

#This is a list of the created charcter breakdowns of Dragonball
pydb = random.choice([goku, krillin, bulma, 
korrin, chichi, oolong, 
A8, piccolo, roshi,])

#This is a list of the created charcter breakdowns of Dragonball z
pydbz = random.choice([vegeta, nappa, futureTrunks, 
raddiz, cell, vegito, 
frieza, broly,])

#This is a list of the created charcter breakdowns of Dragonball Super
pydbs = random.choice([bulla, beerus, frost, 
hit, jiren, zamatsu, 
zeno, vados, chompa,])

#This is the random module selecting characters from the above lists
