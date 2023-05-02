import pickle


def read_data():
    james = get_coach_data('./data/james2.txt')
    julie = get_coach_data('./data/julie2.txt')
    mikey = get_coach_data('./data/mikey2.txt')
    sarah = get_coach_data('./data/sarah2.txt')

    print(james.name + "'s fastest times are: "+str(james.top3()))

    print(julie.name + "'s fastest times are: "+str(julie.top3()))
    
    print(mikey.name + "'s fastest times are: "+str(mikey.top3()))

    print(sarah.name + "'s fastest times are: "+str(sarah.top3()))

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
        return AthleteList(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return(None)
    
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]) -> None:
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    
    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put and store):' + str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athlete = {}
    try:
        with open('athlete.pickle', 'rb') as athf:
            all_athlete = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get from store):' + str(ioerr))
    return(all_athlete)

if __name__ == '__main__':
    read_data()