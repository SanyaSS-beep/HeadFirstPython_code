def read_data():
    james = get_coach_data('./data/james2.txt')
    julie = get_coach_data('./data/julie2.txt')
    mikey = get_coach_data('./data/mikey2.txt')
    sarah = get_coach_data('./data/sarah2.txt')

    james_data = {}
    james_data['name'] = james.pop(0)
    james_data['DOB'] = james.pop(0)
    james_data['times'] = james
    print(james_data['name'] + "'s fastest times are: "+str(sorted(set([sanitize(t) for t in james_data['times']]))[0:3]))

    julie_data = {}
    julie_data['name'] = julie.pop(0)
    julie_data['DOB'] = julie.pop(0)
    julie_data['times'] = julie    
    print(julie_data['name'] + "'s fastest times are: "+str(sorted(set([sanitize(t) for t in julie_data['times']]))[0:3]))
    
    mikey_data = {}
    mikey_data['name'] = mikey.pop(0)
    mikey_data['DOB'] = mikey.pop(0)
    mikey_data['times'] = mikey
    print(mikey_data['name'] + "'s fastest times are: "+str(sorted(set([sanitize(t) for t in mikey_data['times']]))[0:3]))

    sarah_data = {}
    sarah_data['name'] = sarah.pop(0)
    sarah_data['DOB'] = sarah.pop(0)
    sarah_data['times'] = sarah
    print(sarah_data['name'] + "'s fastest times are: "+str(sorted(set([sanitize(t) for t in sarah_data['times']]))[0:3]))

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
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)
    

if __name__ == '__main__':
    read_data()