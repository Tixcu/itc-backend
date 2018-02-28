import urllib.request
import urllib.parse
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    print(url)
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)

def get_film_data(film_id):
    film = dict()
    f_id = '/movie/%s' % film_id
    film = make_tmdb_api_request(method=f_id, api_key='f83997ed5774e7f3a8dbd1bcbbc0b384',extra_params={'append_to_response' : 'lists,keywords,credits'})
    print('shiet')
    return film


def create_film_db(db_size):
    print('say smth man')
    db = []
    i = 1
    while(i <= db_size):
        try:
            print(i)
            db.append(get_film_data(i))
            i+=1
        except:
            db_size += 1
            i+=1
    print('fin')
    return db


x = create_film_db(1000)
f = open('film_db.json', 'w')
f.write(json.dumps(x))
f.close()


