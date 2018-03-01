import json


def find_film(film_db, film_name):# film search via title
    for i in range(len(film_db)):
        if film_db[i]['title'].lower() == film_name:
            del db[i]
            return film_db[i]
    print('Film not found, using first in the base')
    return db[0]


def make_same_genre_list(film_db, film):# makes lst of films with same genre
    rec_list = list()
    for i in range(len(film_db)):
        if film_db[i]['genres'] == film['genres'] and film_db[i]['adult'] == film['adult']:
            film_db[i]['rec_rate'] = 0.0
            rec_list.append(film_db[i])
    return rec_list


def check_credits(rec_list, film): # comparing credits and adding rating
    crew_list = set()
    cast_list = set()
    for i in rec_list:
        for j in i['credits']['crew']:
            for l in film['credits']['crew']:
                if l['name'] == j['name']:
                    crew_list.add(l['name'])
        i['rec_rate'] += len(crew_list)
        for j in i['credits']['cast']:
            for l in film['credits']['cast']:
                if l['name'] == j['name']:
                    cast_list.add(l['name'])
        i['rec_rate'] += len(cast_list)/2
        cast_list = set()
        crew_list = set()
    return rec_list


def rating_dif(rec_list, film): #comparing rating and ading recomendation rating
    for i in rec_list:
        i['rec_rate'] += (10 - abs(i['vote_average'] - film['vote_average']))/2
    return rec_list


def budget_dif(rec_list, film): #comparing budget and adding recomendation rating
    for i in rec_list:
        f = abs(i['budget'] - film['budget']) + 0.1
        if f/(film['budget']+0.1) < film['budget']/f:
            i['rec_rate'] += f/film['budget']
        else:
            i['rec_rate'] += film['budget']/f
    return rec_list


def check_keywords(rec_list, film): #comparing keywords and adding recomendation rating
    for i in rec_list:
        for j in i['keywords']['keywords']:
            for l in film['keywords']['keywords']:
                if j==l:
                    i['rec_rate'] += 1
    return rec_list
       
                              
f = open('film_db.json', 'r')
db = json.loads(f.read())
sname = input().lower()
sfilm = find_film(db,sname)
rec_list = make_same_genre_list(db, sfilm)
rec_list = check_credits(rec_list, sfilm)
rec_list = rating_dif(rec_list, sfilm)
rec_list = check_keywords(rec_list, sfilm)
rec_list = sorted(rec_list, key = lambda x: x['rec_rate'], reverse = True)
i = 0
while i < 3 and i < len(rec_list):
    print(rec_list[i]['title'])
    i += 1

