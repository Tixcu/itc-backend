import json

import os

from utility_functions import load_json_data_from_url, make_tmdb_api_request


def get_film_data(film_id):
    film = dict()
    f_id = '/movie/%s' % film_id
    film = make_tmdb_api_request(method=f_id, api_key=api,extra_params={'append_to_response' : 'lists,keywords,credits'})
    return film


def create_film_db(db_size):
    db = list()
    film_num = 1
    while(film_num <= db_size):
        try:
            print(film_num)
            db.append(get_film_data(i))
            film_num += 1
        except urllib.error.HTTPError:
            db_size += 1
            film_num += 1
    

def main():
    api = os.environ.get('my_api')
    data_base = create_film_db(1000)
    with open('film_db.json', 'w') as file:
        file.write(json.dumps(data_base))

        
if __name__ == '__main__':
    main()