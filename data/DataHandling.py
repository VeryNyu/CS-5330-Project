from os import path
import json, csv

DIR = path.dirname(path.abspath(__file__))
RAW_PATH = path.join(DIR, "raw")


def load_json(filename):
    with open(path.join(RAW_PATH, filename), "r") as f:
        return json.load(f)

def sample(perm, epi):
    effects = []
    for i, bit in enumerate(perm):
        if bit == "1":
            effects.append((i+1, epi[i]['effect']))
    return effects

def record(combatant, card, response):
    FILE_PATH = path.join("processed", f"{combatant}.csv")
    header = ['card', '1', '2', '3', '4', '5']
    data = []
    try:
        with open(FILE_PATH, 'r') as f:
            Reader = csv.DictReader(f)
            for row in Reader:
                data.append(row)
    except FileNotFoundError:
        with open(FILE_PATH, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    finally:
        update(data, card, response[0])
        with open(FILE_PATH, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)

def update(data, target_card, target_epiphany):
    for row in data:
        if row['card'] == target_card:
            if row[target_epiphany] == '':
                row[target_epiphany] = '1'
                return
            else:
                get = row[target_epiphany]
                num = int(get)
                add = num + 1
                new = str(add)
                row[target_epiphany] = new
            return
    data.append({'card': target_card, target_epiphany: '1'})