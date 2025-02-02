import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '581ec74162708d50936b3fd4d3353496'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}
body_create_pokemon = {
    "name": "lizzz",
    "photo_id": 656
}

body_change_name = {
    "pokemon_id": "198179",
    "name": "Lokolllie",
    "photo_id": 445
}

body_in_pokeball = {
    "pokemon_id": "212999"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_in_pokeball)
print(response.text)