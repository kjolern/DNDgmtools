import random
import csv

def villgen():

    with open("./villainlists/schemes.csv") as f:
        reader = csv.reader(f)
        scheme = random.choice(list(reader))

    with open("./villainlists/methods.csv") as f:
        reader = csv.reader(f)
        method = random.choice(list(reader))

    with open("./villainlists/weakness.csv") as f:
        reader = csv.reader(f)
        weakness = random.choice(list(reader))

    print(25* "*")
    print("Villain info:")
    print("Scheme: {}".format(scheme[0]))
    print("Method: {}".format(method[0]))
    print("Weakness: {}".format(weakness[0]))
    print(25* "*")
    return