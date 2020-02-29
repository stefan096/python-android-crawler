import requests
import json

# resp = requests.get('http://localhost:8081/api/pokemon/proba')
# if resp.status_code != 200:
#     # This means something went wrong.
#     print('los')
# else:
#     print("uspeo")
#
from pokemon import Pokemon

pokemon = {
    "name": "najnoviji",
    "hp": 200,
    "atk": 300,
    "defense": 400
}

pokemonList = []
pokemonObj1 = Pokemon()
pokemonObj1.name = "prvi"
pokemonObj1.atk = 100
pokemonObj1.hp = 200
pokemonObj1.defense = 300

pokemonObj2 = Pokemon()
pokemonObj2.name = "drugi"
pokemonObj2.atk = 101
pokemonObj2.hp = 201
pokemonObj2.defense = 301

pokemonList.append(pokemonObj1)
pokemonList.append(pokemonObj2)

# jsonStr = json.dumps(pokemonObj1.__dict__)

# dataStr = {
#     "name": pokemonObj1.name,
#     "hp": pokemonObj1.hp,
#     "atk": pokemonObj1.atk,
#     "defense": pokemonObj1.defense
# }

# dataStrList = {
#     "pokemons": json.dumps([ob.__dict__ for ob in pokemonList])
# }

json_string = json.dumps([ob.__dict__ for ob in pokemonList])

resp = requests.post('http://localhost:8081/api/pokemon/all/string', json=json_string)
if resp.status_code != 200:
    # This means something went wrong.
    print('los')
else:
    print("uspeo")
