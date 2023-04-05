import requests

poke_api = 'https://pokeapi.co/api/v2/pokemon/'



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
    
    
        