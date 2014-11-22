
procedures = []
def make_list():
    f = open('uniques.txt', 'r+')
    global procedures
    procedures = f.read().split("\n")
    for x 
    #f.write(procedures)
    print(procedures)
    f.close()

make_list()
