import json

from utility_functions import title_search


def make_same_genre_list(film):# makes list of films with same genre
    with open('film_db.json', 'r') as file:
        film_db = json.loads(file.read())
    rec_list = list()
    for film_num in range(len(film_db)):
        if film_db[film_num]['genres'] == film['genres'] and film_db[film_num]['adult'] == film['adult'] and fiml_db[film_num] != film:
            film_db[film_num]['rec_rate'] = 0.0
            rec_list.append(film_db[film_num])
    return rec_list


def check_credits(rec_list, sfilm): # comparing credits and adding rating
    rec_list = compare_cast(rec_list, sfilm)
    rec_list = compare_crew(rec_list, sfilm)
    return rec_list


def compare_cast(rec_list, sfilm):
    cast_list = set()
    for man in film['credits']['cast']:
            for sman in sfilm['credits']['cast']:
                if sman['name'] == man['name']:
                    cast_list.add(sman['name'])
        film['rec_rate'] += len(cast_list)/2 #cast has less value
        cast_list = set()
    return rec_list


def compare_crew(rec_list, sfilm):
    crew_list = set()
    for film in rec_list:
        for man in film['credits']['crew']:
            for sman in sfilm['credits']['crew']:
                if man['name'] == sman['name']:
                    crew_list.add(sman['name'])
        film['rec_rate'] += len(crew_list)
        crew_list = set()
    return rec_list


def rating_dif(rec_list, sfilm): #comparing rating and adding recomendation rating
    for film in rec_list:
        film['rec_rate'] += (10 - abs(film['vote_average'] - sfilm['vote_average']))/2
    return rec_list


def budget_dif(rec_list, sfilm): #comparing budget and adding recomendation rating
    for film in rec_list:
        dif = abs(i['budget'] - sfilm['budget']) + 0.1
        if dif/(sfilm['budget']+0.1) < sfilm['budget']/dif:
            film['rec_rate'] += dif/sfilm['budget']
        else:
            film['rec_rate'] += sfilm['budget']/dif
    return rec_list


def check_keywords(rec_list, sfilm): #comparing keywords and adding recomendation rating
    for film in rec_list:
        for key in film['keywords']['keywords']:
            for skey in sfilm['keywords']['keywords']:
                if key==skey:
                    film['rec_rate'] += 1
    return rec_list
       

def create_recomendation_list(sfilm) 
    rec_list = make_same_genre_list(sfilm)
    rec_list = check_credits(rec_list, sfilm)
    rec_list = rating_dif(rec_list, sfilm)
    rec_list = check_keywords(rec_list, sfilm)
    rec_list = sorted(rec_list, key = lambda x: x['rec_rate'], reverse = True) #Sorting list by recomendation rating
    return rec_list


def main():
    sfilm = title_search(input().lower())
    rec_list = create_recomendation_list(sfilm)
    film_count = 3
    if len(rec_list) < film_count:
        for film in rec_list:
            print(film['title'])
    else:
        for film_num in range(3):
            print(rec_list[film_num]['title'])


if __name__ == '__main__':       
	main()
