import json

def make_list():
    f = open('uniques.txt', 'r')
    procedures = []
    dct = {}
    procedures = f.read().split("\n")
    for each in procedures:
        dct.append({"line": each})
    print( dct)



make_list()
