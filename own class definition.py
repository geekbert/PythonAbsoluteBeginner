class Critter(object):
    total = 0 
    def __init__(self, name):
        print("a new critter has been born")
        self.name = name
        Critter.total += 1
    @staticmethod
    def status():
        print("Total number of critters: ", Critter.total) 
    def __str__(self):
        rep = "Critter Object\n"
        rep+= "Name: " + self.name + "\n"
        return rep 

#main
print(Critter.total) 
crit1 = Critter("Frank")
crit2 = Critter("Dirk") 
print(crit1)
print(crit1.name)
Critter.status()

