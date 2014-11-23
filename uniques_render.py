import json


def make_list():
	f = open('uniques.txt', 'r')
	procedures = f.read().split("\n")
	f.close()
	print(procedures)


def make_json():
    f = open('uniques.txt', 'r')
    procedures = []
    dct = {}
    procedures = f.read().split("\n")
    f.close()
    thing = json.dumps([dict(line=pn) for pn in procedures])
    json_file = open('uniques.json', 'w')
    json_file.write(thing)


make_list()
