def read_data():
    james = get_coach_data('./data/james2.txt')
    julie = get_coach_data('./data/julie2.txt')
    mikey = get_coach_data('./data/mikey2.txt')
    sarah = get_coach_data('./data/sarah2.txt')

    print(james['name'] + "'s fastest times are: "+str(james['times']))

    print(julie['name'] + "'s fastest times are: "+str(julie['times']))
    
    print(mikey['name'] + "'s fastest times are: "+str(mikey['times']))

    print(sarah['name'] + "'s fastest times are: "+str(sarah['times']))

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return ({
            'name': templ.pop(0),
            'DOB': templ.pop(0),
            'times': str(sorted(set([sanitize(t) for t in templ]))[0:3])
        })
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)
    

if __name__ == '__main__':
    read_data()