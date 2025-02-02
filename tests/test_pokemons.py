import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '581ec74162708d50936b3fd4d3353496'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}
TRAINER_ID = 18903

def test_status_code():
    response = requests.get(url = f'{URL}/trainers',params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers',params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == "18903"