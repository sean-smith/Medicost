#MediCost Data Query Code
import csv
import sys

lol = list(csv.reader(open('Medicare-Physician-and-Other-Supplier-PUF-yz-CY2012.csv', "rt", encoding='utf8'), delimiter=','))

def queryDatabase(state, zip, service):
    for x in range(10):
        print("")
        for y in range(27):
          sys.stdout.write(lol[x][y])
    return

def getvalues(value, valuetype):
    if(valuetype == "State"):
        for x in range(len(lol)):
            for y in range(len(lol[x])):
                print(lol[x][11])
                #
                #
                #
    if(valuetype == "Zip"):
        print()
    if(valuetype == "Service"):
        print()
    return





#queryDatabase(0,0,0)
getvalues(5, "State")