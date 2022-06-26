import json
import requests
from bs4 import BeautifulSoup

from utils import get_percentage

characters = [
    "Abigail",
    "Akira",
    "Akuma",
    "Alex",
    "Balrog",
    "Birdie",
    "Blanka",
    "Cammy",
    "Chun-Li",
    "Cody",
    "Dan",
    "Dhalsim",
    "Ed",
    "EHonda",
    "Falke",
    "FANG",
    "G",
    "Gill",
    "Guile",
    "Ibuki",
    "Juri",
    "Kage",
    "Karin",
    "Ken",
    "Kolin",
    "Laura",
    "Lucia",
    "Luke",
    "MBison",
    "Menat",
    "Nash",
    "Necalli",
    "Oro",
    "Poison",
    "Rashid",
    "RMika",
    "Rose",
    "Ryu",
    "Sagat",
    "Sakura",
    "Seth",
    "Urien",
    "Vega",
    "Zangief",
    "Zeku",
]

done_characters = 0

url = 'https://game.capcom.com/cfn/sfv/character/{}/movelist?lang=en'
data = {
    'moves': [],
}

def print_characters_percentage():
    print(f'{get_percentage(done_characters, characters.__len__())}% done')


for character in characters:

    furl = url.format(character.lower())
    res = requests.get(furl)
    soup = BeautifulSoup(res.text, 'html.parser')
    all_rows = soup.find_all(class_='styleRecord')
    all_character_moves = []

    for row in all_rows:
        text = row.find_all('td')[0].text
        if text != '':
            all_character_moves.append(text.strip())

    moves_done = 0

    for move in all_character_moves:
        move_metadata = {
            'name': move,
            'franchise': 'Street Fighter',
            'iteration': 'Street Fighter V',
            'character': character 
        }
        data['moves'].append(move_metadata)
    
    done_characters = done_characters + 1
    print_characters_percentage()

db = json.load(open('db.json'))


with open('db.json', 'w') as f:
    for m in data['moves']:
        db['moves'].append(m)
    f.write(json.dumps(db, indent=4))
    f.close()

