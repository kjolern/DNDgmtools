import random
import csv

def npcgen():
    #variables
    sex = None
    race = None
    charname = None

    #Sex choice
    print("1.Male")
    print("2.Female")

    npcsex = input("Are you Male or Female ? ")

    if npcsex == "1":
        sex = "Male"
    
    elif npcsex == "2":
        sex = "Female"

    else:
        print("Invalid Choice")
        print(25* "*")
        return

    #Race choices listed
    print("1.Dragonborn")
    print("2.Dwarf")
    print("3.Elf")
    print("4.Gnome")
    print("5.Half-Elf")
    print("6.Halfling")
    print("7.Half-Orc")
    print("8.Human")
    print("9.Tiefling")

    npcrace = input("What race do you want to generate? ")

    if npcrace == "1":
        race = "Dragonborn"
    
    elif npcrace == "2":
        race = "Dwarf"
    
    elif npcrace == "3":
        race ="Elf"

    elif npcrace == "4":
        race = "Gnome"
    
    elif npcrace == "5":
        race ="Half-Elf"

    elif npcrace == "6":
        race = "Halfling"
    
    elif npcrace == "7":
        race ="Half-Orc"

    elif npcrace == "8":
        race = "Human"
    
    elif npcrace == "9":
        race ="Tiefling"

    else:
        print("Invalid choice")
        print(25* "*")
        return


    # Name Generator will use name lists based on sex and race.  Traits are random other lists
    namelookup = sex+race+".csv"
    
    with open("./namelists/"+str(namelookup)) as f:
        reader = csv.reader(f)
        charname = random.choice(list(reader))

    with open("./traitslists/appearances.csv") as f:
        reader = csv.reader(f)
        appearance = random.choice(list(reader))

    with open("./traitslists/highabilities.csv") as f:
        reader = csv.reader(f)
        highability = random.choice(list(reader))

    dupcheck = True
    while dupcheck:
        with open("./traitslists/lowabilities.csv") as f:
            reader = csv.reader(f)
            lowability = random.choice(list(reader))
            if str(lowability).split()[0] == str(highability).split()[0]:
                continue
            else:
                dupcheck = False
                
    with open("./traitslists/talents.csv") as f:
        reader = csv.reader(f)
        talent = random.choice(list(reader))

    with open("./traitslists/mannerisms.csv") as f:
        reader = csv.reader(f)
        mannerism = random.choice(list(reader))

    with open("./traitslists/interactions.csv") as f:
        reader = csv.reader(f)
        interaction = random.choice(list(reader))

    with open("./traitslists/bonds.csv") as f:
        reader = csv.reader(f)
        bond = random.choice(list(reader))

    with open("./traitslists/flawssecrets.csv") as f:
        reader = csv.reader(f)
        flawsecret = random.choice(list(reader))
    

    
    # Printing the NPC generated
    print(25* "*")
    print("Sex: {}".format(sex))
    print("Race: {}".format(race))
    print("Name: {}".format(charname[0]))
    print("Appearance: {}".format(appearance[0]))
    print("High ability: {}".format(highability[0]))
    print("Low ability: {}".format(lowability[0]))
    print("Talent: {}".format(talent[0]))
    print("Mannerism: {}".format(mannerism[0]))
    print("Interaction trait: {}".format(interaction[0]))
    print("Bond: {}".format(bond[0]))
    print("Flaw or secret: {}".format(flawsecret[0]))
    print(25* "*")
    return


