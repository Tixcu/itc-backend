import json


def find_film(film_db, film_name):# film search via title
    for film_num in range(len(film_db)):
        if film_db[film_num]['title'].lower() == film_name:
            del db[film_num]
            return film_db[film_num]
    print('Film not found, using first film in the base')
    return db[0]


def make_same_genre_list(film_db, film):# makes lst of films with same genre
    rec_list = list()
    for film_num in range(len(film_db)):
        if film_db[film_num]['genres'] == film['genres'] and film_db[film_num]['adult'] == film['adult']:
            film_db[film_num]['rec_rate'] = 0.0
            rec_list.append(film_db[film_num])
    return rec_list


def check_credits(rec_list, sfilm): # comparing credits and adding rating
    crew_list = set()
    cast_list = set()
    for film in rec_list:
        for man in film['credits']['crew']:
            for sman in sfilm['credits']['crew']:
                if man['name'] == sman['name']:
                    crew_list.add(sman['name'])
        film['rec_rate'] += len(crew_list)
        for man in film['credits']['cast']:
            for sman in sfilm['credits']['cast']:
                if sman['name'] == man['name']:
                    cast_list.add(sman['name'])
        film['rec_rate'] += len(cast_list)/2
        cast_list = set()
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
       

if __name__ == '__main__':       
	with open('film_db.json', 'r') as f:
		db = json.loads(f.read())
		sname = input().lower()
		sfilm = find_film(db,sname)
		rec_list = make_same_genre_list(db, sfilm)
		rec_list = check_credits(rec_list, sfilm)
		rec_list = rating_dif(rec_list, sfilm)
		rec_list = check_keywords(rec_list, sfilm)
		rec_list = sorted(rec_list, key = lambda x: x['rec_rate'], reverse = True) #Sorting list by recomendation rating
		film_count = 0
		while film_count < 3 and film_count < len(rec_list):
			print(rec_list[film_count]['title'])
			film_count += 1

