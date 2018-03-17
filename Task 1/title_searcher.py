import json

from utility_functions import title_search


if __name__ == '__main__':
	name = input()
	print(title_search(name)['title'])