# consumo_api/api.py
import requests

class PokemonAPI:
    BASE_URL = 'https://pokeapi.co/api/v2/'

    @classmethod
    def get_pokemon_list(cls, limit=10):
        url = f'{cls.BASE_URL}pokemon?limit={limit}'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json().get('results', [])
        else:
            return []

    @classmethod
    def get_pokemon_details(cls, pokemon_url):
        response = requests.get(pokemon_url)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    @classmethod
    def get_pokemon_details_by_id(cls, pokemon_id):
        url = f'{cls.BASE_URL}pokemon/{pokemon_id}/'
        return cls.get_pokemon_details(url)
