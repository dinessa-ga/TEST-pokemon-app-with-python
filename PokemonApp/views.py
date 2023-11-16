from django.shortcuts import render
import requests

def index(request):
    pokemon_list = []

    # Fetch a list of Pokémon
    url_pokeapi = 'https://pokeapi.co/api/v2/pokemon?limit=10'
    response = requests.get(url_pokeapi)

    if response.status_code == 200:
        data = response.json()

        for result in data.get('results', []):
            pokemon_name = result.get('name', '')
            pokemon_url = result.get('url', '')

            # Fetch details for each Pokémon
            response_pokemon = requests.get(pokemon_url)

            if response_pokemon.status_code == 200:
                pokemon_data = response_pokemon.json()

                # Extract relevant information
                pokemon_info = {
                    'name': pokemon_name.capitalize(),
                    'sprite': pokemon_data.get('sprites', {}).get('front_default', ''),
                    'abilities_count': len(pokemon_data.get('abilities', [])),
                    'url': pokemon_url,
                }

                pokemon_list.append(pokemon_info)

    context = {
        'pokemon_list': pokemon_list,
    }

    return render(request, 'main/index.html', context)
