import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return "A Saxon has died in combat"

# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if self.saxonArmy and self.vikingArmy:  # Check if armies are not empty
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            ret = saxon.receiveDamage(viking.attack())
            if ret == "A Saxon has died in combat":
                self.saxonArmy.remove(saxon)
            return ret
        return "No more soldiers to attack"

    def saxonAttack(self):
        if self.saxonArmy and self.vikingArmy:  # Check if armies are not empty
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            ret = viking.receiveDamage(saxon.attack())
            if ret.endswith("has died in act of combat"):
                self.vikingArmy.remove(viking)
            return ret
        return "No more soldiers to attack"

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
