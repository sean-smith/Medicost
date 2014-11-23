import json

procedures = []
def make_list():
    f = open('uniques.txt', 'r+')
    global procedures
    procedures = f.read().split("\n")
    f.close()
    thing = json.dumps([dict(line=pn) for pn in procedures])
    json_file = open('uniques.json', 'w')
    json_file.write(thing)

make_list()
