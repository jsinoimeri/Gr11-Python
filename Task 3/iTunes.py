import re, random, time

in_file = open("library_small.xml")

artists = []
track_id = []
songs = []

# regular expresions enhance the search by searching
# a key made of one or more digits
patKey = re.compile('<key>[0-9]+</key>')
isKey = False

# reading the lines of the file
for line in in_file:
    # this search in the file for '<key>[0-9]+</key>' and if found isKey becomes True
    if patKey.search(line):
        isKey = True
    # this will search in the file for "<dict>"
    if "<dict>" in line:
        got_dict = True
    
    if "</dict>" in line:
        got_dict = False
        isKey = False
    
    goAhead = isKey and got_dict
    # if goAhead is True then track_ids, song names and artist names will be added to their corresponding lists
    if goAhead:
        if"<key>Track ID</key>" in line:
            line = line.strip()
            line = line.replace("<key>Track ID</key>", "").replace("</integer>", "")
            line = line.replace("<integer>", "")
            track_id += [line]

          
        if "<key>Name</key>" in line:
            line = line.strip()
            line = line.replace("<key>Name</key>", "").replace("</string>", "")
            line = line.replace("<string>", "")
            songs += [line]
            
        if "<key>Artist</key>" in line:
            line = line.strip()
            line = line.replace("<key>Artist</key>", "").replace("</string>", "")
            line = line.replace("<string>", "")
            artists += [line]
in_file.close()
menu = 0

while menu != "5" and menu != "Quit" and menu != "quit":
    menu = raw_input("\n1. Top artists \n2. Artists scramble \n3. Quiz \n4. Memory game\n5. Quit \nYour choice?(number please): ")
    #top Artist 
    
    if menu == "1":
        artist_table={}
        artist_table_num_songs={}
        artists_2 = []
        track_id2 = []
        artists_2 += artists
        track_id2 += track_id
        
        # this will combine the two lists together in one for loop
        for a, s in zip(artists_2, track_id2):
            if artist_table.has_key(a):
                artist_table[a] += "," + s
            else:
                artist_table[a] = s
        # this counts the number of songs by that artist
        for b in artist_table:
            artist_table_num_songs[b] = artist_table[b].count(",")+1
        
        # building a list of sorted artist names by values of artist_table_num_songs
        artist_table_num_songs_items = artist_table_num_songs.items()
        artist_table_num_songs_back_items =[ [v[1],v[0]] for v in artist_table_num_songs_items]
        
        # since artist_table_num_songs_back_items is in ascending order from lowest num songs to the largest
        # I reversed the order so that the highest is in the front and lowest at the back
        artist_table_num_songs_back_items.sort(reverse=True)
        artist_table_num_songs_decr_sorted_list=[ artist_table_num_songs_back_items[i][1] for i in range(0,len(artist_table_num_songs_back_items))]
        # artist_table_num_songs_decr_sorted_list now as very artist in decreasing number of songs
        
        # header of the table
        head = ["ARTIST", "#Songs", "SONG IDS"]
        max_artist_name = len(head[0])
        
        # this will take the max length of "#Songs" and number of digits for number of songs
        max_song_no = max(len(str(artist_table_num_songs[artist_table_num_songs_decr_sorted_list[0]])),len(head[1]))
        max_song_list = len(head[2])
        
        # max length of song list
        for b in artist_table:
            if max_artist_name < len(b):
                max_artist_name = len(b)
            
            if max_song_list < len(artist_table[b]):
                max_song_list = len(artist_table[b])
        
        
        print head[0].center(max_artist_name-12) + "|" + head[1].center(max_song_no) + "|" , head[2].ljust(max_song_list)
        
        # prints "-" as many times as the length of top artist including his name, number of songs and track ids
        print "-"*(max_artist_name-9+max_song_no+max_song_list)
        
        # this will center artist name and number of songs by artists as well as left adjust track ids
        for b in artist_table_num_songs_decr_sorted_list[0:10]:
            print b.center(max_artist_name-12) + "|" + str(artist_table_num_songs[b]).center(max_song_no) + "|" , artist_table[b].ljust(max_song_list)
        
        # this as well will print "-" max number of times
        print "-"*(max_artist_name-9+max_song_no+max_song_list)

    
    
    #Artists scramble    
    
    elif menu == "2":

        artists_2 = []
        artists_2 += artists
        
        random_artist = []
        
        quit = ""
        
        while quit == "" or quit == "n":
            pos = random.randint(0, len(artists_2)-1)
            upper_case_name = ""
            
            # this will assign the name of a random artist the normal_case_artist variable
            normal_case_artist = artists_2[pos]
            
            # this will make the name upper case and remove the spaces
            upper_case_name = normal_case_artist.upper().replace(" ", "")
            random_artist += upper_case_name
            
            scramble_name = ""
            
            # this loop will scramble the name by removing a letter at a random position and adding it to the string
            while len(scramble_name) < len(upper_case_name):
                num = random.randrange(0, len(random_artist))
                scramble_name += random_artist[num]
                random_artist.remove(random_artist[num])
                
            
            print "The scrambled artists name is %s" %(scramble_name)
            
            num_times = 0
            guess = ""
            
            # the user has three trys to get the right answer than he/she is given the artists name
            # as well as being prompt if they wish to continue, if yes, the name is counted
            # how many times it appears in the list and then it is removed that
            # many times
            while num_times < 3 and guess != normal_case_artist and guess!= normal_case_artist.lower() and guess != normal_case_artist.upper() and guess != normal_case_artist.capitalize():
                num_times += 1
                guess = raw_input("Please guess the artists name?: ")
                guess = guess.lower()
            
            if guess == normal_case_artist or guess == normal_case_artist.lower() or guess == normal_case_artist.upper() or guess == normal_case_artist.capitalize():
                print "Correct!"
            
            else:    
                print "The artists name is %s" %(normal_case_artist)
            
            quit = raw_input("Do you wish to quit (y,n)?: ")
            
            if quit == "n" or quit == "no":
                num = artists_2.count(artists_2[pos])
                for num_remove in range(0,num):
                    artists_2.remove(normal_case_artist)
            else:
                quit = "yes"
                print ""

    #Quiz
    
    elif menu == "3":
        quiz_answers = ["d", "b", "a", "c", "a", "d", "b", "c", "b", "a", "b"]
        
        quiz_questions = ["\n1. What is the track id for the song 'Acre of Land'?: \na. 732\nb. 714\nc. 710\nd. 712", "\n2. What category does Ray LaMontagne belong in?: \na. Track Ids\nb. Artist\nc. Gender \nd. Album", "\n3. Find the missing song name: _ _ _ _ _ _ _   _ _ _ _ _?: \na. Killing Birds\nb. Pink Noise(Rock Me Amadeus)\nc. Skinny Dippin\nd. Black Tambourine", "\n4. Who sang Pink Noise (Rock Me Amadeus)?: \na. Ron Sexsmith\nb. Oasis\nc. Beck\nd. Ladyhawk", "\n5. What is the Track Id of the song 'Waiting For You': \na. 5366\nb. 5636\nc. 5663\nd. 6653", "\n6. What type of genre is the song 'Waitin' For A Train'?: \na. Alternative\nb. R&B\nc. Punk\nd. a and c together", "\n7. What year was the song 'Rowboat' created?: \na. 1993\nb. 1994\nc. 1995\nd. 1992", "\n8. What type of file is the song 'Picture In A Frame'?: \na. Wav\nb. Mp3\nc. AAC audio file\nd. Mpeg-4", "\n9. Is it possible to have two songs with the same Track Id?: \na. True\nb. False", "\n10. How big is 'Shelter (live)' 5878363 bytes in megabytes?: \na. 5.6\nb. 6.7\nc. 5.45\nd. 6.6"]
        
        score = 10
        
        # this will print out the questions at that positon in the second list and match it to the answer in the first list
        # if the output matches with the answer then score says the same if not, score is minused 1
        for pos in range(0,10):            
            print quiz_questions[pos]
            question = raw_input("\nYour choice (letter please): ")
            if question != quiz_answers[pos]:
                score -=1
        
        # this prints output your score as well as a percentage
        print "\nYour score is %i and as a percent, it is %i%%" %(score, (score/10.0)*100)
    

    #memory game
    elif menu == "4":    
        
        songs_2 = []        
        songs_2 += songs
        memorize_time = 4
        play_again = "yes"
        score = 0
        
        while play_again == "yes" or play_again == "y":
            output = ""
            output_list = []
            
            # searches for the four songs at random positions
            for num_times in range(4):
                pos = random.randint(0, len(songs_2)-1)
                output += songs_2[pos]+"\n"
                output_list += [songs_2[pos].lower()]
                songs_2.remove(songs_2[pos])
            
            print "\n%s\nYou will only get four guesses and each time your viewing time will get shorter" %(output)
            
            # the program will "sleep" for about 4 seconds first time around
            time.sleep(memorize_time)
            print "\n"*150   
            
            # the user will have 4 turns, one guess for each song and receive a score of +1 if right and -1 if wrong
            for guess_num in range(1,5):        
                guess = raw_input(("Please enter name #%i: ") %(guess_num))
                guess = guess.lower()
                
                if output_list.__contains__(guess):
                    print "Good job. Keep going"
                    output_list.remove(guess)
                    score += 1
                else:
                    score -= 1
            # the amount of time is divided by two each time until the user types "n"
            memorize_time /= 2.0
            
            # if the list becomes empty and the user still wishes to play again, the list is reset to the beginning
            if len(songs_2) == 0:
                play_again = raw_input("There are no more artist names in the list do you still wish to play again(y/n)?: ")
                if play_again == "y":
                    songs_2 += songs
                print ""
            
            # if the list is not empty, the user is prompt with the question "Play again"
            else:
                play_again = raw_input("Play again(y/n)?: ")
                print ""
        
        # this will output your score after you have decided to quit the game
        if play_again == "n" or play_again == "no" or play_again == "":
            print "Your total score during the game was %i." %(score)
        
        # yes it is possible to receive a negative score
        if score < 0:
            print "Yes it is possible to get a negative score in my version of the game."
