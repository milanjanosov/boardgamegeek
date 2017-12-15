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
    #ll_titles =  [line.strip() for line in open('MISSING_GAMES_2st_run.dat') if ',name' not in line]

  
    num_of_chunks = 8 
    chunks = chunk(all_titles, num_of_chunks)   

    for i in range(num_of_chunks):   
        f = open(folder + '/names_and_links_all_games_' + str(i) + '.dat', 'w')
        for game in chunks[i]:     
            f.write(game+'\n')
        f.close()
        


def get_game_data(g, title):



  

    alternative_names = 'na'
    try:  
        alternative_names = g.alternative_names
    except:
        pass


    artists = 'na'
    try:  
        artists = g.artists
    except:
        pass



    boardgame_rank = 'na'
    try:  
        boardgame_rank = g.boardgame_rank
    except:
        pass



    categories = 'na'
    try:  
        categories = g.categories
    except:
        pass



    description = 'na'
    try:  
        description = g.description
    except:
        pass



    designers = 'na'
    try:  
        designers = g.designers
    except:
        pass


    expands = 'na'
    try:  
        expands = g.expands
    except:
        pass

 

    expansion = 'na'
    try:  
        expansion = g.expansion
    except:
        pass
  
    families= 'na'
    try:  
        families = g.families
    except:
        pass


    iid = 'na'
    try:  
        iid = g.id
    except:
        pass

  
    implementations = 'na'
    try:  
        implementations = g.implementations
    except:
        pass
  
    max_players = 'na'
    try:  
        max_players = g.max_players
    except:
        pass
  
    
    mechanics = 'na'
    try:  
        mechanics = g.mechanics
    except:
        pass
  
    

    min_age = 'na'
    try:  
        min_age = g.min_age
    except:
        pass
  
    

    min_players = 'na'
    try:  
        min_players = g.min_players
    except:
        pass
  
       
    
    playing_time = 'na'
    try:  
        playing_time = g.playing_time
    except:
        pass  
  
    
    expansions = 'na'
    try:  
        expansions = g.expansions
    except:
        pass  




    
    publishers = 'na'
    try:  
        publishers = g.publishers
    except:
        pass  
      
    
    ranks = 'na'
    try:  
        ranks = g.ranks
    except:
        pass 


  
 

    rating_average = 'na'
    try:  
       rating_average  = g.rating_average
    except:
        pass  




    rating_num_weights = 'na'
    try:  
       rating_num_weights  = g.rating_num_weights
    except:
        pass  

   

    year = 'na'
    try:  
       year  = g.year
    except:
        pass     
    
    
                            




    game_data = OrderedDict([   ('name'              , title),
                                ('alternative_names' , alternative_names),
                                ('artists'           , artists),
                                ('boardgame_rank'    , boardgame_rank),
                                ('categories'        , categories),
                                ('description'       , description),
                                ('designers'         , designers),
                                ('expands'           , expands),
                                ('expansion'         , expansion),
                                ('expansions'        , expansions),
                                ('families'          , families),
                                ('id'                , iid),
                                ('implementations'   , implementations),
                                ('max_players'       , max_players),
                                ('mechanics'         , mechanics),
                                ('min_age'           , min_age),
                                ('min_players'       , min_players),
                                ('playing_time'      , playing_time),
                                ('publishers'        , publishers),
                                ('ranks'             , ranks),
                                ('rating_average'    , rating_average),
                                ('rating_num_weights', rating_num_weights),
                                ('year'              , year)
                             ])


    return game_data


def download_data(thread):


    titles = [line.strip() for line in open('game_titles/names_and_links_all_games_' + str(thread) + '.dat')]
    bgg    = boardgamegeek.BoardGameGeek()
    i      = 1
    n      = len(titles)


    with open('board_game_api_data_9_' + str(thread) + '.csv', 'wb') as fou:

        for title in titles:
            try:
            
                print title
                g = bgg.game(title.replace('"',''))
                 
                print g

                dw = csv.DictWriter(fou, delimiter=',', fieldnames=get_game_data(g, title))
                if i == 1:  dw.writeheader()
                dw.writerow(get_game_data(g, title))

                print title, '\t', i, '/', n, '\t', thread+1, '/5'
                i += 1
                time.sleep(1)
                
            except:
                print 'error'
                i += 1
                time.sleep(1)
                pass


if __name__ == '__main__': 

    if sys.argv[1] == 'chunk':
        chunk_input_file()
    elif sys.argv[1] == 'download':
        thread = int(sys.argv[2])
        download_data(thread)










