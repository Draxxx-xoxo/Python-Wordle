from wonderwords import RandomWord
from nltk.corpus import wordnet
import random 

# Welcome message
print("WELCOME TO WORDLE")
print("This is a game of WORDLE")

game_mode = input("Choose Single(0) or Multiplayer(1): ")


if game_mode == "0":
    print("You are playing in single player mode")
elif game_mode == "1":
    print("You are playing in multiplayer player mode")
    user_player_1 = input("Enter username of Player 1: ")
    user_player_2 = input("Enter username of Player 2: ")
    players = [user_player_1, user_player_2]
    players_id = [None, None]
    print("CALCUALTING LUCK.....")
    random_player = random.choice(players)
    print(f"{random_player} goes first")

    if random_player == user_player_1:
        players_id[0] = 0
        players_id[1] = 1
    elif random_player == user_player_2:
        players_id[0] = 1
        players_id[1] = 0
else:
    print("Please input 0 or 1 as your choice") 

length = int(input("Please enter a length greater than 5: "))
# Check if the length is greater than 5
check_length = False
while not check_length:
    if length < 5:
        print("Please enter a length greater than 5")
        length = int(input("Please enter a length greater than 5: "))
    else:
        check_length = True

# Function to randomise a word 
def random_word():
    r = RandomWord()
    # Get a random word
    random_word = r.word(word_max_length=length, word_min_length=length)
    word_list = []
    # Append the word into a list
    for letter in random_word:
        word_list.append(letter)

    return word_list 

# Check if the word actually exsist (This lib does not work so well)
def check_real_word(word):
    if wordnet.synsets(word):
        return True
    else:
        return False

# Get user input of the 5 letters

correct = False
word_list = random_word() 
print(word_list) # this would not be in the actual game, its just for testing
total_results = []
tries = 0

correct_length_lis = []

for i in range(length):
    correct_length_lis.append("🟩" )

# Run while loop until the player guess or they ran out of tries
while not correct and tries < length :
    letters = (input("Please enter five letters: ")).lower()    

    # Check if the word is real and if the length is of letter is the equal
    if check_real_word(letters) == False:
        print("Please enter a real word")
        continue
    elif len(letters) != length:
        print(f"Please enter {length} letters")
        continue

    letter_place = 0
    results= []
    print(letters)

    # Loop through to check for the letters
    for alpha in letters:   
        if str(alpha) == str(word_list[letter_place]):
            results.append("🟩")
        elif alpha in word_list:
            results.append("🟨") 
        else:                       
            results.append("⬜")
        letter_place += 1

    tries += 1
    total_results.append(results)
    
    if results == correct_length_lis:
        correct = True
        print("Correct")
        print(" ".join(results))


#Output the results
print("--------------------------------")
print("ALL RESULTS")
print("--------------------------------")
for row in total_results:
    print(" ".join(row))
    print("--------------------------------")




            
# 🟨 🟩 ⬜        

        
        

    
# Check the 5 letters if they are in the right spot or not

# If the letter is in the right spot, it will be green

# If the letter is in the word but not in the right spot, it will be yellow

# If the letter is not in the word, it will be grey

# If the letter is in the word but not in the right spot, it will be red

# User tets 5 times to guess the word

# If the user guesses the word, the game will end

# Output users score and the color of each letter in a round

# Optional: Export the users score to a file and the color of each letter in a round to a file

# Optional: Allow for more than 5 letter words

# Multiplayer???
