import requests

poke_api = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    #pinfo = get_pokemon_info("Pikachu")
   # pinfo = get_pokemon_info(123)
   # names = get_pokemon_names()
    
    download_pokemon_artwork('ditto', '')
    
    return

def get_pokemon_info(pname):
    pname = str(pname).strip().lower()

    url = poke_api + pname

    print(f'getting information for {pname}...', end='')
    resp_msg = requests.get(url)

    if resp_msg.status_code == requests.codes.ok:
        print('success')
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return
    
def get_pokemon_names(offset=0, limit=100000):
    
    query_str_params = {
        'offset' : offset,
        'limit' : limit,


    }
    print(f'Getting list of Pokemon names...', end='')
    resp_msg = requests.get(poke_api, params=query_str_params)

    if resp_msg.status_code == requests.codes.ok:
        print('success')
        pokemon_dict = resp_msg.json()
        pokemon_names_list = [p['name']for p in pokemon_dict['results']]
        return pokemon_names_list
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return
    

def download_pokemon_artwork(pokemon_name):
    
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info is None:
        return

    artwork_url = pokemon_info['sprites']['other']['official-artwork']['front_default']



    return








if __name__ == '__main__':
        main()

        