import os
import boardgamegeek
import time
import csv
import sys
from collections import OrderedDict
reload(sys)  
sys.setdefaultencoding('utf8')


def chunk(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out
 
  

def chunk_input_file():

    folder = 'game_titles'
    if not os.path.exists(folder): os.makedirs(folder)

    all_titles =  [line.strip().split(',', 2)[-1] for line in open('names_and_links_all_games.csv') if ',name' not in line]

    num_of_chunks = 5
    chunks = chunk(all_titles, num_of_chunks)   

    for i in range(num_of_chunks):   
        f = open(folder + '/names_and_links_all_games_' + str(i) + '.dat', 'w')
        for game in chunks[i]:     
            f.write(game+'\n')
        f.close()
        


def get_game_data(g):

    game_data = OrderedDict([   ('alternative_names' , g.alternative_names),
                                ('artists'           , g.artists),
                                ('boardgame_rank'    , g.boardgame_rank),
                                ('categories'        , g.categories),
                                ('description'       , g.description),
                                ('designers'         , g.designers),
                                ('expands'           , g.expands),
                                ('expansion'         , g.expansion),
                                ('expansions'        , g.expansions),
                                ('families'          , g.families),
                                ('id'                , g.id),
                                ('implementations'   , g.implementations),
                                ('max_players'       , g.max_players),
                                ('mechanics'         , g.mechanics),
                                ('min_age'           , g.min_age),
                                ('min_players'       , g.min_players),
                                ('playing_time'      , g.playing_time),
                                ('publishers'        , g.publishers),
                                ('ranks'             , g.ranks),
                                ('rating_average'    , g.rating_average),
                                ('rating_num_weights', g.rating_num_weights),
                                ('year'              , g.year)
                             ])


    return game_data


def download_data(thread):


    titles = [line.strip() for line in open('game_titles/names_and_links_all_games_' + str(thread) + '.dat')]
    bgg    = boardgamegeek.BoardGameGeek()
    i      = 1
    n      = len(titles)


    with open('board_game_api_data_' + str(thread) + '.csv', 'wb') as fou:

        for title in titles[0:10]:
            
            g = bgg.game(title)
             
            dw = csv.DictWriter(fou, delimiter=',', fieldnames=get_game_data(g))
            if i == 1:  dw.writeheader()
            dw.writerow(get_game_data(g))

            print title, '\t', i, '/', n, '\t', thread+1, '/5'
            i += 1
            time.sleep(1)
    


if __name__ == '__main__': 

    if sys.argv[1] == 'chunk':
        chunk_input_file()
    elif sys.argv[1] == 'download':
        thread = int(sys.argv[2])
        download_data(thread)










