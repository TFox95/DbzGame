from classes import parameter, zFighter
#These are the character breakdowns
vegeta = zFighter("Vegeta", "Dbz", True)
goku = zFighter("Goku", "Db", True)
krillin = zFighter("Krillin", "Db", True)
bulma = zFighter("Bulma", "Db", False)
piccolo = zFighter("piccolo", "Db", True)
nappa = zFighter("nappa", "Dbz", True)
bulla = zFighter("bulla", "Dbs", False)
beerus = zFighter("Beerus", "Dbs", True)
roshi = zFighter("Master Roshi", "Db", True)
korrin = zFighter("Korin", "Db", True)
chichi = zFighter("Chi-Chi", "Db", True)
oolong = zFighter("Oolong", "Db", False)
A8 = zFighter("Android 8", "Db", False)

#These are the player's basic arguments; user attempts, score, guess limit
playerargs = parameter(0,0,4)

dict = {"vegeta": (vegeta.name, vegeta.show)}

print(dict["vegeta"])