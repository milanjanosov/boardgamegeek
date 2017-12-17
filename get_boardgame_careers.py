import os
import sys
import csv
reload(sys)  
sys.setdefaultencoding('utf8')

def parse_list(lista):

    return lista.replace('",', '\',').replace(' \"', ' \'').replace('u\'', '\'').replace('[\'', '').replace('\']', '').replace('[', '').replace(']', '').split('\', \'')


def add_to_dict(dictionary, key, value):

    if key not in dictionary:
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)



artists_career   = {}
designers_career = {}

with open('results/boardgamegeek_api_results.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        try:


            artists   = parse_list(row[1])
            designers = parse_list(row[5]) 
            year      = row[21].replace('\'', '')
            index     = row[10].replace('\'', '')
            
            impact = '0'


            if len(artists) > 1:
                for artist in artists:
                    add_to_dict(artists_career, artist, (index, year, impact) )

            if len(designers) > 1:
                for designer in designers:
                    add_to_dict(designers_career, designer, (index, year, impact) )

        except:
            pass






''' ==========================  '''
''' ----  WRITE  ARTISTS  ----  '''
''' ==========================  '''


folder_a = 'Data/Boardgame/boardgame-artists-simple-careers'
if not os.path.exists(folder_a):
    os.makedirs(folder_a)

leng = 0
for artist, games in artists_career.items():

    if '/' not in artist:
    
 
        f = open(folder_a + '/' + artist + '_artist_simple_career.dat', 'w')
        f.write('game_id\tyear\trating_count\n')
        for game in games:
            f.write(game[0] + '\t' + game[1] + '\t' + game[2] + '\n')
            print game
   



print leng






''' ============================  '''
''' ----  WRITE  DESIGNERS  ----  '''
''' ============================  '''
'''
folder_d = 'Data/Boardgame/boardgame-designers-simple-careers'
if not os.path.exists(folder_d):
    os.makedirs(folder_d)

print len(artists_career)
leng = 0
for designer, career in designers_career.items():
    if len(career) > 10:
        leng += 1

print leng

'''

'''

movie_id	year	rating_value	rating_count	metascore	review_count_user	review_count_critic
tt0121766	2005	7.6	533664	68	3296	353
tt0121765	2002	6.7	474520	54	3524	288
tt0120915	1999	6.5	550248	51	3607	323
tt0076759	1977	8.7	938781	92	1485	287
tt0069704	1973	7.5	64801	None	238	99
tt0066434	1971	6.8	39894	75	211	116
tt0426949	1971	5.9	183	None	3	1
tt0283462	1969	4.8	45	None	None	None
tt0062970	1968	5.5	107	None	2	None
tt0061318	1967	5.2	86	None	2	None
tt0061362	1967	4.9	92	None	3	None
tt0061621	1967	5.9	88	None	3	1
tt0062331	1967	6.4	1908	None	22	3
tt0060046	1966	5.2	239	None	5	1
tt0060432	1966	5.3	540	None	4	1
tt0060504	1966	5.9	453	None	2	None
tt0059397	1965	5.9	241	None	4	None


'''





