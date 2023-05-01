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

    for each_t in james:
        clean_james.append(sanitize(each_t))
    for each_t in julie:
        clean_julie.append(sanitize(each_t))
    for each_t in mikey:
        clean_mikey.append(sanitize(each_t))
    for each_t in sarah:
        clean_sarah.append(sanitize(each_t))

    print(sorted(clean_james))
    print(sorted(clean_julie))
    print(sorted(clean_julie))
    print(sorted(clean_sarah))

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