import os

from utility_functions import load_json_data_from_url, make_tmdb_api_request


if __name__ == '__main__':
    api = os.environ.get('my_api')
    print(make_tmdb_api_request(method='/movie/215', api_key=api)['budget'])
