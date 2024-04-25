from ast import Try
import psycopg2 

try:
    conn = psycopg2.connect(database = 'Project431', user = 'postgres', host = 'localhost', password = '1Spieler12345', port = 5432)
    cur = conn.cursor() 
except:
    print('error connecting to database')
        

TITLE, DATE, ACHIEVEMENTS, IMAGE, DLC, AGE, PRICE, WEBSITE, DISCLAIMERS, DESCRIPTION, PLAT = range(11)
attributes = ['GameID: ', 'Game Title: ', 'Release Date: ', 'Required Age: ', 'Price: ', 'Positive Reviews: ', 'Negative Reviews: ']
    
ID, POSITIVE, NEGATIVE = range(3)




def main():
    conn = psycopg2.connect(database = 'Project431', user = 'postgres', host = 'localhost', password = '1Spieler12345', port = 5432)
    cur = conn.cursor() 
    active = True
    while active:
        print('\nWelcome to the Steam Store Page CLI\n')
        print('Update Game (1)')
        print('Add Game (2)')
        print('Delete Game (3)')
        print('View games (4)')
        print('Exit (0)')
       # print('Get Trailer links (5)')
        #print('Get Screenshot links (6)\n')

        user_choice = str(input('Please select an option (0-4): '))
        selecting = True
    
        while selecting:
                try:
                    user_choice = int(user_choice)
                    assert user_choice in range(0,5)
                    selecting = False
                
                    
                except:
                    user_choice = str(input('Please enter a valid selection: '))
        
        if user_choice == 0:
            active = False
        elif user_choice == 1:
            selecting = True
            while selecting:
                user_choice = str(input('Please enter a GameID or enter 0 to return to the menu: '))
                try:
                    user_choice = int(user_choice)
                    if user_choice == 0:
                        selecting = False
                    else:
                        try:
                            cur.execute('select appid from store_pages where appid = (%s)', (user_choice,))
                   
                            temp_list = cur.fetchall() 
                            assert temp_list[0][0] != None
                            selecting = False
                    
                    
                        except:
                            print('Error fetching from database, ensure GameID is accurate')
                    
                except:
                    print('Please enter a number')
               
            updateGame(user_choice)
        elif user_choice == 2:
            user_choice = str(input('\nPlease enter a Game Title, (you may update additional values once the game is added via the update functions from the main menu): '))
            insert_choice = str(input('\nAre you sure you wish to add %s to the database?(1 for yes, anything else for no): ' % (user_choice,)))
            if insert_choice == '1':
                   insertGame(user_choice)
            
        elif user_choice == 3:
            selecting = True
            while selecting:
                user_choice = str(input('Please enter a GameID you wish to delete or press 0 to cancel: '))
                try:
                    user_choice = int(user_choice)
                    if user_choice == 0:
                        selecting = False
                    else:
                        try:
                            cur.execute('select appid, game_name from store_pages where appid = (%s)', (user_choice,))
                   
                            temp_list = cur.fetchall() 
                            assert temp_list[0][0] != None
                            selecting = False
                            delete_choice = str(input('Are you sure you wish to delete %s, gameID: %d (1 for yes, anything else for no): ' % (temp_list[0][1],user_choice)))
                            if delete_choice == '1':
                                deleteGame(user_choice)
                        
                    
                    
                        except:
                            print('Error fetching from database, ensure GameID is accurate')
                    
                except:
                    print('Please enter a number')
                    
        elif user_choice == 4:
            viewGames()
               
    conn.commit()
    conn.close()
        
          
def viewGames():
    while True:
        print('\nView games: \n')
        print('Sort by gameID (1)')
        print('Sort by positive reviews (2)')
        print('Sort by negative reviews (3)')
        print('Exit (0)')
        user_choice = str(input('\n please select an option (0-3): '))
        selecting = True
        while selecting:
            try:
                user_choice = int(user_choice)
                assert user_choice in range(0,4)
                selecting = False                                   
            except:
                user_choice = str(input('Please enter a valid selection: '))
        
        if user_choice == 0: 
            return
        elif user_choice == 1:
            displayGames(retrieveGames(ID))
                            
        elif user_choice == 2:
            displayGames(retrieveGames(POSITIVE))
        elif user_choice == 3:
            displayGames(retrieveGames(NEGATIVE))
            
       
            
         
def retrieveGames(orders):
    user_choice = str(input('\n Would you like to apply additional constraints? (0 for no, 1 for mac supported games, 2 for Indie Games, 3 for multi-dev games): '))                       
    selecting = True    
    while selecting:
            try:
                user_choice = int(user_choice)
                assert user_choice in range(0,4)
                selecting = False                                   
            except:
                user_choice = str(input('Please enter a valid selection: '))
    if user_choice == 0:
        if orders == ID:
            try:
                cur.execute('select appid, game_name, release_date, required_age, price, positive, negative from store_pages order by appid ')
                temp = cur.fetchall()
                return temp
                
            except:
                print('Error retrieving from database')
        elif orders == POSITIVE:
            try:
                cur.execute('select appid, game_name, release_date, required_age, price, positive, negative from store_pages where positive is not null order by positive desc')
                temp = cur.fetchall()
                return temp
                
            except:
                print('Error retrieving from database')
        elif orders == NEGATIVE:
            try:
                cur.execute('select appid, game_name, release_date, required_age, price, positive, negative from store_pages where negative is not null order by negative desc')
                temp = cur.fetchall()
                return temp
                
                
            except:
                print('Error retrieving from database')
      
    elif user_choice == 1:
        if orders == ID:
            try:
                cur.execute('select appid, game_name, release_date, required_age, price, positive, negative from store_pages where mac = %s order by appid ', (True,))
                temp = cur.fetchall()
                return temp
                
            except:
                print('Error retrieving from database')
        elif orders == POSITIVE:
            try:
                cur.execute('select appid, game_name, release_date, required_age, price, positive, negative from store_pages where mac = %s and positive is not null order by positive desc', (True,))
                temp = cur.fetchall()
                return temp
                
            except:
                print('Error retrieving from database')
        elif orders == NEGATIVE:
            try:
                cur.execute('select appid, game_name, release_date, required_age, price, positive, negative from store_pages where mac = %s and negative is not null order by negative desc', (True,))
                temp = cur.fetchall()
                return temp
                
                
            except:
                print('Error retrieving from database')
      
      
    elif user_choice == 2:
        if orders == ID:
            try:
                cur.execute('select store_pages.appid, store_pages.game_name, store_pages.release_date, store_pages.required_age, store_pages.price, store_pages.positive, store_pages.negative from store_pages inner join game_tags on store_pages.appid = game_tags.appid where game_tags.tag_name = %s order by store_pages.appid ', ('Indie',))
                temp = cur.fetchall()
                return temp
                
            except:
                print('Error retrieving from database')
        elif orders == POSITIVE:
            try:
                cur.execute('select store_pages.appid, store_pages.game_name, store_pages.release_date, store_pages.required_age, store_pages.price, store_pages.positive, store_pages.negative from store_pages inner join game_tags on store_pages.appid = game_tags.appid where game_tags.tag_name = %s and store_pages.positive is not null order by store_pages.positive desc', ('Indie',))
                temp = cur.fetchall()
                return temp
                
            except:
                print('Error retrieving from database')
        elif orders == NEGATIVE:
            try:
                cur.execute('select store_pages.appid, store_pages.game_name, store_pages.release_date, store_pages.required_age, store_pages.price, store_pages.positive, store_pages.negative from store_pages inner join game_tags on store_pages.appid = game_tags.appid where game_tags.tag_name = %s and store_pages.negative is not null order by store_pages.negative desc', ('Indie',))
                temp = cur.fetchall()
                return temp
                
                
            except:
                print('Error retrieving from database')
                
        
    elif user_choice == 3:
        if orders == ID:
            try:
                cur.execute('select appid, game_name, release_date, required_age, price, positive, negative from store_pages where appid in (select appid from developers group by appid having count(company_name) > 1) order by appid ')
                temp = cur.fetchall()
                return temp
                
            except:
                print('Error retrieving from database')
        elif orders == POSITIVE:
            try:
                cur.execute('select appid, game_name, release_date, required_age, price, positive, negative from store_pages where positive is not null and appid in (select appid from developers group by appid having count(company_name) > 1) order by positive desc')
                temp = cur.fetchall()
                return temp
                
            except:
                print('Error retrieving from database')
        elif orders == NEGATIVE:
            try:
                cur.execute('select appid, game_name, release_date, required_age, price, positive, negative from store_pages where negative is not null and appid in (select appid from developers group by appid having count(company_name) > 1) order by negative desc')
                temp = cur.fetchall()
                return temp
                
                
            except:
                print('Error retrieving from database')
      
def displayGames(game_array):
    showing = True
    game_to_print = []
    all_games = []
    curr_index = 0
    while showing:
      if game_array != None:
        for entry in game_array:
            game_to_print = []
            for index in range(len(entry)):
                if index < len(attributes):
                    if entry[index] != None:
                        game_to_print.append(attributes[index] + str(entry[index]))
                    else:
                        game_to_print.append(attributes[index] + 'N/A')
                        
            all_games.append(game_to_print)
        
        print('')
        for game_index in range(curr_index,min(curr_index+10, len(all_games))):
            print(all_games[game_index])
            print('')
            
        print('\n')
        selecting = True
        user_choice = str(input('Enter 0 to exit, 1 to go back, 2 to go forward: '))
        while selecting:
            try:
                user_choice = int(user_choice)
                assert user_choice in range(3)
                selecting = False
            except:
                user_choice = str(input('Please enter a valid selection: '))
            
            
            
        if user_choice == 0:
            showing = False
        elif user_choice == 1:
            if curr_index >= 10:
                curr_index -= 10
        elif user_choice ==2:
            if curr_index < len(all_games)-10:
                curr_index += 10
      else:
          print('No games satisfying constraints, returning to menu')
          showing = False

def deleteGame(id):
    try:
        
        cur.execute('delete from text_support where appid = (%s)', (id,))
        cur.execute('delete from audio_support where appid = (%s)', (id,))
        cur.execute('delete from developers where appid = (%s)', (id,))
        cur.execute('delete from publishers where appid = (%s)', (id,))
        cur.execute('delete from screenshots where appid = (%s)', (id,))
        cur.execute('delete from trailer where appid = (%s)', (id,))
        cur.execute('delete from game_tags where appid = (%s)', (id,))
        cur.execute('delete from game_genres where appid = (%s)', (id,))
        cur.execute('delete from game_categories where appid = (%s)', (id,))
        cur.execute('delete from store_pages where appid = (%s)', (id,))

        conn.commit()
        print('Succesfully deleted gameID: %d from database' % (id))
    except:
        print('Error while deleting from databse')
        conn.rollback()
            

    
  

def insertGame(name):
    new_key = 0
    try:
        cur.execute('select max(appid) from store_pages')
        
        max_key= cur.fetchall()
        new_key = int(nullInt(max_key[0][0]))+1
        
        cur.execute('insert into store_pages values(%s, %s)', (new_key,name))
        conn.commit()
        cur.execute('update store_pages set achievements = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set dlc_count = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set required_age = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set price = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set windows = %s where appid = %s', (False,new_key))
        cur.execute('update store_pages set mac = %s where appid = %s', (False,new_key))
        cur.execute('update store_pages set linux = %s where appid = %s', (False,new_key))
        cur.execute('update store_pages set estimated_owners = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set peak_ccu = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set average_playtime_forever = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set average_playtime_two_weeks = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set median_playtime_forever = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set median_playtime_two_weeks = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set user_score = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set positive = 0 where appid = %s', (new_key,))
        cur.execute('update store_pages set recommendations = 0 where appid = %s', (new_key,))
        conn.commit()

        print('\nNew game: %s, added to database with unique appid: %d' % (name,new_key))
        
        
    except:
        print('Error inserting into database')
        conn.rollback()

def nullInt(s):
    if s is None:
        return '0'
    else:
        return str(s)
    
def nullFloat(s):
    if s is None:
        return '0.0'
    else:
        return str(s)
    

def nullStr(s):
    if s is None:
        return ''
    else:
        return str(s)

def updateGame(id):
    updating = True
   
    while updating:
        selecting = True
        
        print('Edit Store Page of: {0} \n'.format(id))
        
        print('Update game title (1)')
        print('Update release date (2)')
        print('Update achievements (3)')
        print('Update header_image (4) ')
        print('Update dlc count (5) ')
        print('Update required age (6) ')
        print('Update price (7)')
        print('Update game website (8)')
        print('Update available platforms (9) ')
        print('Update metacritic page (10)')
        print('Update disclaimers (11) ')
        print('Update game description (12) ')
        print('Update support info (13) ')
        print('Return to main menu (0)\n')
        user_choice = str(input('Select an option (0-13):'))
        
        while selecting:
            try:
                user_choice = int(user_choice)
                assert user_choice in range(14)
                selecting = False
            except:
                user_choice = str(input('Please enter a valid selection'))
            
     
        if user_choice== 0:
            updating = False
        elif user_choice == 1:
            updateValue(id,TITLE)
            updating = True  
        elif user_choice == 2:
            updateValue(id,DATE)
            updating = True     
        elif user_choice == 3:
            updateValue(id,ACHIEVEMENTS)
            updating = True      
        elif user_choice == 4:
            updateValue(id,IMAGE)
            updating = True      
        elif user_choice == 5:
            updateValue(id,DLC)
            updating = True      
        elif user_choice == 6:
            updateValue(id,AGE)
            updating = True      
        elif user_choice == 7:
            updateValue(id,PRICE)
            updating = True      
        elif user_choice == 8:
            updateValue(id,WEBSITE)
            updating = True      
        elif user_choice == 9:
            updateValue(PLAT)
            updating = True      
        elif user_choice == 10:
            updateMCPage(id)
            updating = True      
        elif user_choice == 11:  
            updateValue(id,DISCLAIMERS)
            updating = True  
        elif user_choice == 12:
            updateValue(id,DESCRIPTION)
            updating = True                  
        elif user_choice == 13:
            updateSupport(id)
            updating = True    

                

        

def updateValue(id, value):
  updated_value = None
  loop = True
  try:
        if value == TITLE:
            cur.execute('select game_name from store_pages where appid = (%s)', (id,))
            cur_value = nullStr(cur.fetchall()[0][0])
            
            print('current Title of game %d is: %s' % (id,cur_value))
            updated_value = str(input('Enter new value: '))
            try:  
                cur.execute('update store_pages set game_name = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\nSuccesfully updated game title to %s \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()
        elif value == DATE:
            cur.execute('select release_date from store_pages where appid = (%s)', (id,))
            cur_value = nullStr(cur.fetchall()[0][0])
            
            print('current release date of game %d is: %s' % (id,cur_value))
            updated_value = str(input('Enter new value: '))
            try:  
                cur.execute('update store_pages set release_date = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\nSuccesfully updated release date to %s \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()
        elif value == ACHIEVEMENTS:
            cur.execute('select achievements from store_pages where appid = (%s)', (id,))
            cur_value = nullInt(cur.fetchall()[0][0])
            
            print('current achievemnt count of game %d is: %s' % (id,cur_value))
            while loop:
                updated_value = str(input('Enter new value: '))
                try:
                    updated_value = int(updated_value)
                    loop = False
                except:
                    print('error, input not a number')
            try:  
                cur.execute('update store_pages set achievements = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\nSuccesfully updated achievement count to %d \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()
        elif value == IMAGE:
            cur.execute('select header_image from store_pages where appid = (%s)', (id,))
            cur_value = nullStr(cur.fetchall()[0][0])
            
            print('current header image of game %d is: %s' % (id,cur_value))
            updated_value = str(input('Enter new value: '))
            try:  
                cur.execute('update store_pages set header_image = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\nSuccesfully updated header image to %s \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()      
        elif value == DLC:
            cur.execute('select dlc_count from store_pages where appid = (%s)', (id,))
            cur_value = nullInt(cur.fetchall()[0][0])
            
            print('current dlc count of game %d is: %s' % (id,cur_value))
            while loop:
                updated_value = nullStr(input('Enter new value: '))
                try:
                    updated_value = int(updated_value)
                    loop = False
                except:
                    print('error, input not a number')
            try:  
                cur.execute('update store_pages set dlc_count = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\nSuccesfully updated dlc count to %d \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()
        if value == AGE:
            cur.execute('select required_age from store_pages where appid = (%s)', (id,))
            cur_value = nullInt(cur.fetchall()[0][0])
            
            print('current age requirement of game %d is: %s' % (id,cur_value))
            while loop:
                updated_value = str(input('Enter new value: '))
                try:
                    updated_value = int(updated_value)
                    loop = False
                except:
                    print('error, input not a number')
            try:  
                cur.execute('update store_pages set required_age = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\nSuccesfully updated age requirement to %d \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()
        elif value == PRICE:
            cur.execute('select price from store_pages where appid = (%s)', (id,))
            cur_value = nullFloat(cur.fetchall()[0][0])
            
            print('current price of game %d is: %s' % (id,cur_value))
            while loop:
                updated_value = str(input('Enter new value: '))
                try:
                    updated_value = float(updated_value)
                    loop = False
                except:
                    print('error, input not a number')
            try:  
                cur.execute('update store_pages set price = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\n Succesfully updated price to %f.2 \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()
        elif value == WEBSITE:
            cur.execute('select website from store_pages where appid = (%s)', (id,))
            cur_value = nullStr(cur.fetchall()[0][0])
            
            print('current website of game %d is: %s' % (id,cur_value))
            updated_value = str(input('Enter new value: '))
            try:  
                cur.execute('update store_pages set website = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\n Succesfully updated website link to %s \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()
        elif value == DISCLAIMERS:
            cur.execute('select notes from store_pages where appid = (%s)', (id,))
            cur_value = nullStr(cur.fetchall()[0][0])
            
            print('current disclaimers of game %d is: %s' % (id,cur_value))
            updated_value = str(input('Enter new value: '))
            try:  
                cur.execute('update store_pages set notes = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\n Succesfully updated disclaimers to %s \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()
        elif value == DESCRIPTION:
            cur.execute('select about_the_game from store_pages where appid = (%s)', (id,))
            cur_value = nullStr(cur.fetchall()[0][0])
            
            print('current description of game %d is: %s' % (id,cur_value))
            updated_value = str(input('Enter new value: '))
            try:  
                cur.execute('update store_pages set about_the)game = %s where appid = %s', (updated_value,id))
                conn.commit()
                print('\n Succesfully updated description to %s \n' % (updated_value))
            except:
                print('Error while updating value')
                conn.rollback()


  except:

        print('Error fetching from database')
    


def updateMCPage(id):
    mc_data = []
    try:
        mc_data = cur.execute('select metacritic_url, metacritic_score from store_pages where appid = (%s)', (id,))
        cur_page = nullStr(mc_data[0][0])
        cur_score = nullInt(mc_data[0][1])                   
        print('Game {0}, with metacritic page {1}, and metacritic score {2}'.format(id, cur_page, cur_score))   
        updated_value = str(input('Enter new metacritic url: '))
        try:  
            conn.execute('update store_pages set metacritic_url = %s where appid = %s', (updated_value,id))
            conn.commit()
            print('/nSuccesfully updated metacritic_url of Game: %d to %s', (id, updated_value))
        except:
            print('Error while updating value')
            conn.rollback()
            
        loop = True
        while loop:
            updated_value = str(input('Enter new metacritic score (0-100): '))
            try:
                updated_value = int(updated_value)
                assert updated_value in range(101)
                loop = False
            except:
                print('error, input invalid')
        try:  
            conn.execute('update store_pages set metacritic_score = %s where appid = %s', (updated_value,id))
            conn.commit()
            print('/nSuccesfully updated metacritic_score of Game: %d to %s', (id, updated_value))
        except:
            print('Error while updating value')
            conn.rollback()
       
    except:
        print('error fetching metacritic data')
        return
    


def updateSupport(id):
    return
    supp_data = []
    try:
        mc_data = cur.execute('select support_url, support_email from store_pages where appid = (%s)', (id,))
        cur_page = nullStr(mc_data[0][0])
        cur_email = nullInt(mc_data[0][1])      
        print('Game {0}, with support page {1}, and support email {2}'.format(id, cur_page, cur_email))
        
            
        updated_value = str(input('Enter new support url: '))
        try:  
            cur.execute('update store_pages set support_url = %s where appid = %s', (updated_value,id))
            conn.commit()
            print('/nSuccesfully updated support_url of Game: %d to %s', (id, updated_value))
        except:
            print('Error while updating value')
            conn.rollback()
            
           
        updated_value = str(input('Enter new support email'))
               
        try:  
            cur.execute('update store_pages set support_email = %s where appid = %s', (updated_value,id))
            conn.commit()
            print('/nSuccesfully updated support_email of Game: %d to %s', (id, updated_value))
        except:
            print('Error while updating value')
            conn.rollback()
       
    except:
        print('error fetching metacritic data')
        return
    

if __name__ == "__main__":
    main()