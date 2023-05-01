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

    clean_james = []
    clean_julie = []
    clean_mikey = []
    clean_sarah = []

    print(sorted([sanitize(t) for t in james]))
    print(sorted([sanitize(t) for t in julie]))
    print(sorted([sanitize(t) for t in mikey]))
    print(sorted([sanitize(t) for t in sarah]))

def sanitize(time_string):
    if '-' in time_string:
        splitter = ''
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '-.' + secs)

if __name__ == '__main__':
    read_data()