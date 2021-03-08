import json
import random

for i in range(3):
    with open("./items/magicitems.json") as f:
        reader = json.load(f)
        item = random.choice(list(reader['items']))

        print(item)
