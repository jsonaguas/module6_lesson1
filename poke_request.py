import requests
import json

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text
pikachu_data = json.loads(json_data)
poke_name = (str(pikachu_data['name'])).capitalize()

def poke_abilities(data):
    print('Abilities:')
    for ability in data['abilities']:
        print('-' + ability['ability']['name'])

print (f"Name: {poke_name}")
poke_abilities(pikachu_data)


#Task 2
def fetch_pokemon_data(pokemon_list):
    for pokemon in pokemon_list:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        json_data = response.text
        data = json.loads(json_data)
        poke_name = (str(data['name'])).capitalize()
        print(f"Name: {poke_name}")
        print('Abilities:')
        for ability in data['abilities']:
            print('-' + ability['ability']['name'])

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
def average_weight(pokemon_list):
    weight = 0
    for pokemon in pokemon_list:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
        json_data = response.text
        data = json.loads(json_data)
        weight += data['weight']
    return weight / len(pokemon_list)
    




pokemon_names = ["pikachu", "bulbasaur", "charmander"]
fetch_pokemon_data(pokemon_names)
print(f"The average weight is: {average_weight(pokemon_names)}")

