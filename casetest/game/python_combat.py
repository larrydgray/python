import random
random.seed()

class Unit:
    def __init__(self,unit_type,attack_value,defend_value):
        self.type=unit_type
        self.attack=attack_value
        self.defend=defend_value

tank = Unit('tank',9,4)
plane = Unit('plane',4,1)
troop = Unit('troop',1,2)

units = [tank,plane,troop]

#build attackers
num_attackers=random.randint(2,6)
attackers=[]
for i in range(num_attackers):
    print('Attacker ',i)
    #unit = random.randint(0,2) # random int 1 to 3
    attackers.append(random.choice(units))

#build defenders
num_defenders=random.randint(1,5)
defenders=[]
for i in range(num_defenders):
    print('Defender ',i)
    #unit = random.randint(0,2) # random int 1 to 3
    defenders.append(random.choice(units))

print('Attackers')
print([a.type for a in attackers])
print('Defenders')
print([a.type for a in defenders])

attack_values=[a.attack for a in attackers]
attack_hits=0
for attack_value in attack_values:
    attack_role=random.randint(1,10)
    if attack_role>=attack_value:
        attack_hits+=1
print('Attack hits ',attack_hits)

defend_values=[a.defend for a in defenders]
defend_hits=0
for defend_value in defend_values:
    defend_role=random.randint(1,10)
    if defend_role>=defend_value:
        defend_hits+=1
print('Defend hits ',defend_hits)

print()
print('Attacker casualties')
if len(attackers)<defend_hits:
    defend_hits=len(attackers)
for i in range(defend_hits):
    remove=random.randint(0,len(attackers)-1)
    print('Attacker '+attackers[remove].type+' is destroyed.')
    attackers.pop(remove)

print()
print('Defender casualties')
if len(defenders)<attack_hits:
    attack_hits=len(defenders)
for i in range(attack_hits):
    remove=random.randint(0,len(defenders)-1)
    print('Defender '+defenders[remove].type+' is destroyed.')
    defenders.pop(remove)

    

