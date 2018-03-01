import urllib.request
import urllib.parse
import json


file = open('film_db.json', 'r')
str = file.read()
db = json.loads(str)
name = input('Введите фразу присуствующую в названии фильма: ')
for film in db:
    if name.lower() in film['title'].lower():
        print(film['title'])
