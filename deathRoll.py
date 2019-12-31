import random

def deathRoll():
    count = 0
    roll = 1000
    while roll != 1:
        roll = random.randint(1, roll)
        count +=1
    return (count % 2)

first = 0
second = 0

for x in range(0, 100000):
    if (deathRoll() == 1):
        first += 1
    else:
        second +=1

print(first)
print(second)