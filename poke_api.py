import requests
import image_lib
import os

poke_api = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    pinfo = get_pokemon_info("Pikachu")
    pinfo = get_pokemon_info(123)
    names = get_pokemon_names()
    
    download_pokemon_artwork('ditto', r'C:\Users\Danie\OneDrive\Desktop\Random')
    
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
        print('Success')
        pokemon_dict = resp_msg.json()
        pokemon_names_list = [p['name']for p in pokemon_dict['results']]
        return pokemon_names_list
    else:
        print('Failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return
    

def download_pokemon_artwork(pokemon_name, save_dir):
    
    # Get all info for the specified pokemon
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info is None:
        return

    # Extract the artwork URL from the info dictionary
    artwork_url = pokemon_info['sprites']['other']['official-artwork']['front_default']

    
    image_bytes = image_lib.download_image(artwork_url)
    if image_bytes is None: 
        return
    

    file_ext = artwork_url.split('.')[-1]
    image_path = os.path.join(save_dir, f'{pokemon_name}.{file_ext}')
    
    # Saves the image
    if image_lib.save_image_file(image_bytes, image_path):
        return image_path

if __name__ == '__main__':
        main()

        