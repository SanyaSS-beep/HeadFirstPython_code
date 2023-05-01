def read_data():
    with open('./data/james.txt') as jaf:
        data = jaf.readline()
    james = data.strip().split(',')
    with open('./data/julie.txt') as juf:
        data = juf.readline()
    julie = data.strip().split(',')
    with open('./data/mikey.txt') as mif:
        data = mif.readline()
    mikey = data.strip().split(',')
    with open('./data/sarah.txt') as saf:
        data = saf.readline()
    sarah = data.strip().split(',')

    print(james)
    print(julie)
    print(mikey)
    print(sarah)

if __name__ == '__main__':
    read_data()