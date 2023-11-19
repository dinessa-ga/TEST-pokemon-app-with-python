# from django.shortcuts import render
# import requests

# def ListaView(request):
#     pokemon_list = []

#     # Fetch a list of Pokémon
#     url_pokeapi = 'https://pokeapi.co/api/v2/pokemon?limit=10'
#     response = requests.get(url_pokeapi)

#     if response.status_code == 200:
#         data = response.json()

#         for result in data.get('results', []):
#             pokemon_name = result.get('name', '')
#             pokemon_url = result.get('url', '')

#             # Fetch details for each Pokémon
#             response_pokemon = requests.get(pokemon_url)

#             if response_pokemon.status_code == 200:
#                 pokemon_data = response_pokemon.json()

#                 # Extract relevant information
#                 pokemon_info = {
                    
#                     'sprite': pokemon_data.get('sprites', {}).get('front_default', ''),
#                     'name': pokemon_name.capitalize(),
#                     'abilities_count': len(pokemon_data.get('abilities', [])),
#                     'url': pokemon_url,
#                 }

#                 pokemon_list.append(pokemon_info)

#     context = {
#         'pokemon_list': pokemon_list,
#     }

#     return render(request, 'main/index.html', context)


# consumo_api/views.py
from django.shortcuts import render
from django.views import View
from .api import PokemonAPI

class ListView(View):
    def get(self, request):
        pokemon_list = []

        # Obtener la lista de Pokémon
        pokemon_api = PokemonAPI()
        results = pokemon_api.get_pokemon_list(limit=20)

        for result in results:
            pokemon_name = result.get('name', '')
            pokemon_url = result.get('url', '')
            pokemon_id = result.get('url', '').split('/')[-2]

            # Obtener detalles para cada Pokémon
            pokemon_data = pokemon_api.get_pokemon_details(pokemon_url)

            if pokemon_data:
                # Extraer información relevante
                pokemon_info = {
                    'id': pokemon_id,
                    'sprite': pokemon_data.get('sprites', {}).get('front_default', ''),
                    'name': pokemon_name.capitalize(),
                    'abilities_count': len(pokemon_data.get('abilities', [])),
                    'url': pokemon_url,
                }

                pokemon_list.append(pokemon_info)

        context = {
            'pokemon_list': pokemon_list,
        }

        return render(request, 'main/index.html', context)


    
class DetailsView(View):
    def get(self, request, item_id):
        # Obtener detalles para el Pokémon específico
        pokemon_api = PokemonAPI()
        pokemon_data = pokemon_api.get_pokemon_details_by_id(item_id)

        if pokemon_data:
            # Obtener más detalles del Pokémon

            weight = pokemon_data.get('weight', '')
            height = pokemon_data.get('height', '')
                    
            context = {
                'pokemon_data': pokemon_data,
                'sprite': pokemon_data.get('sprites', {}).get('front_default', ''),
                'weight': weight,
                'height': height,
           }

            return render(request, 'main/details.html', context)
        # else:
        #     # Manejar errores si no se puede obtener detalles
        #     return render(request, 'main/error.html', {'error_message': 'Error al obtener detalles del Pokémon'})