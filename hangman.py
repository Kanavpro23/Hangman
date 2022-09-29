import random #Importing a library called Random
def hangman(): #defining hangman

    list_of_words = ['barcelona',#List of words that will be in the game
              'bayern',
              'pumas',
              'losangeles',
              'santos',
              'nacional',
              'bocajuniors',
              'mumbaicity',
              'bournemouth',
              'parissaintgermain',
              'acmilan',
              'shenzhenfc',
              'visselkobe',
              'seoulfc',
              'alsadd',
              'alhilal',
              'youngboys',
              'burnley',
              'zenit',
              'sheriff',
              'moldefk',
              'malmoff',
              'legiawarsaw',
              'wrexham',
              'melbournevictory',
              'copenhagen',
              'suzukapointgetters',
              'charlotte'
              'maccabihaifa']
    word = random.choice(list_of_words)#Random words will appear in the game
    tries = 10
    guessmade = ''
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')#The valid characters that can be used to guess

    while len(word)>0:
        main_word = ""
       

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "

                
        if main_word == word:
            print(main_word)
            print("Congrats! You Won!!!!")
            break
             

        print("Guess the word", main_word)
        guess = input()


        if guess in valid_entry:
            if(len(guess)>1):
                print("Only one letter allowed!")
            else:
                guessmade = guessmade+guess
        else:
            print("enter the valid characters")
            guess=input()


            
            
            
            

        if guess not in word:
            tries = tries-1
            if tries==9:
                print("9 tries left")
                print("----------")
            elif tries == 8:
                print("8 tries left")
                print("----------")
                print("     O    ")    
            elif tries == 7:  
                print("7 tries left")
                print("----------")
                print("     O    ")
                print("     |    ")
            elif tries == 6:
                print("6 tries left")
                print("----------")
                print("     O    ")
                print("     |    ")  
                print("    /     ")
            elif tries == 5:
                print("5 tries left")
                print("----------")
                print("     O    ")
                print("     |    ")  
                print("    / \    ")
            elif tries == 4:
                print("4 tries left")
                print("----------")
                print("    \O    ")
                print("     |    ")  
                print("    / \    ")
            elif tries == 3:
                print("3 tries left")
                print("----------")
                print("    \O/    ")
                print("     |    ")  
                print("    / \    ")
            elif tries == 2:
                print("2 tries left")
                print("----------")
                print("    \O/ |   ")
                print("     |    ")  
                print("    / \    ")
            elif tries == 1:
                print("only 1 try left!",name,"on his last few breaths")
                print("----------")
                print("     O_|   ")
                print("    /|\    ")  
                print("    / \    ")
            elif tries == 0:
                   print("You lost")
                   print("You let a good footballer die")
                   print("The word was",word)
                   break



          
                    
                    
                
            
                   

        
            

        
                   
                

                


                
    
    


name = input("Enter Your Name ->")
print("Welcome to Hangman",name,"!")
print("---------------------------")
print("try to guess the word in less than 10 turns")
action = 1
while action:
    hangman()
    action = int(input("Press 1 to start, 0 to exit"))
        



