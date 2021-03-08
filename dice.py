import random 

#simple diceroller that takes in the number of sides on the dice and number of dice
def diceroller():
    sides = int(input("How many sides do you want on your dice? "))
    dicenumber = int(input("How many dice do you want to roll? "))
    bonus = int(input("Add bonus modifier! "))
    dicetotal = 0

    for dice in range(0,dicenumber):
        eyes = random.randint(1, sides)
        print("rolling dice {}".format(dice+1))
        print(eyes)
        dicetotal += eyes

    print("Adding bonus {}".format(bonus))
    dicetotal += bonus
    print("The total roll is {}".format(dicetotal))
    
    return