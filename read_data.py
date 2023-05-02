def read_data():
    with open('./data/james.txt') as jaf:
        data = jaf.readline()
    james = data.strip().split(',')
    james = sorted([sanitize(t) for t in james])
    with open('./data/julie.txt') as juf:
        data = juf.readline()
    julie = data.strip().split(',')
    julie = sorted([sanitize(t) for t in julie])
    with open('./data/mikey.txt') as mif:
        data = mif.readline()
    mikey = data.strip().split(',')
    mikey = sorted([sanitize(t) for t in mikey])
    with open('./data/sarah.txt') as saf:
        data = saf.readline()
    sarah = data.strip().split(',')
    sarah = sorted([sanitize(t) for t in sarah])

    unique_james = []
    for each_t in james:
        if each_t not in unique_james:
            unique_james.append(each_t)
    print(unique_james[0:3])

    unique_julie = []
    for each_t in julie:
        if each_t not in unique_julie:
            unique_julie.append(each_t)
    print(unique_julie[0:3])

    unique_mikey = []
    for each_t in mikey:
        if each_t not in unique_mikey:
            unique_mikey.append(each_t)
    print(unique_mikey[0:3])

    unique_sarah = []
    for each_t in sarah:
        if each_t not in unique_sarah:
            unique_sarah.append(each_t)
    print(unique_sarah[0:3])

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

if __name__ == '__main__':
    read_data()