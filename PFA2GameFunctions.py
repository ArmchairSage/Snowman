import random
import datetime
dt = datetime.datetime.now()

def playGame(wordLst, catLst, scoreboardLst):
    # Setting up initial variables for playGame function
    choice = 0 # variable for menu-based choices - Category and Difficulty

    categorySelect = False # Is set to True when a player selects a Category
    category = "" # Stores which category the player picked

    diffSelect = False # Is set to True when a player selects a Difficulty
    difficulty = "" # Stores which difficulty the player picked

    points = 0 # Points earned depending on which difficulty the player selected
    chance = 5 # The amount of chances a player has left before losing the game
    validGuess = False # Is set to True whenever the player makes a correct guess
    noRepeat = False # Is set to True to ensure a player doesn't guess the same correct letters again (doesn't apply to incorrect letters)

    shortLst = [] # List of the words from Words.txt file which have the category and difficulty the player selected
    snowmanWord = [] # Random word selected from shortLst
    maskedWord = [] # snowmanWord but masked with hyphens

    while choice != (len(catLst) + 1) and categorySelect == False: # Loops the Category selection menu unless the player selects the exit option
        try:
            print("\n\t== CHOOSE A CATEGORY ==")

            for index in range(len(catLst)):
                print("\t" + str(index + 1) + ")", catLst[index]) # Categories list can change and grow larger, unlike Difficulty list, so the 'for' loop is formatted differently

            print("\t" + str(len(catLst) + 1) + ") Exit")
            choice = int(input("\t> Enter your choice: "))

        except Exception as ex:
            print("\n\t" + str(ex))
            choice = 0

        if choice == len(catLst) + 1: # Exit option - returns to Main Menu
            return

        elif choice < 1 or choice > len(catLst): # Validation - inputs can only be based on the choices shown in the Category selection menu
            print("\n\tInvalid Choice!")

        else:
            print("\n\t> Your selected category is", "'" + catLst[choice - 1] + "'")
            categorySelect = True
            category = catLst[choice - 1]

    if categorySelect: # Will only proceed to Difficulty selection menu if the player has chosen a Category
        while choice != 4 and diffSelect == False: # Loops the Difficulty selection menu unless the player selects the exit option
            try:
                print("\n\t== CHOOSE A DIFFICULTY ==")

                print("\t1) Easy")
                print("\t2) Medium")
                print("\t3) Hard")
                print("\t4) Exit")

                choice = int(input("\t> Enter your choice: "))

            except Exception as ex:
                print("\n\t" + str(ex))
                choice = 0

            if choice == 1:
                print("\n\t> Your selected difficulty is 'Easy'")
                diffSelect = True
                difficulty = "easy"
                points = 1

            elif choice == 2:
                print("\n\t> Your selected difficulty is 'Medium'")
                diffSelect = True
                difficulty = "medium"
                points = 5

            elif choice == 3:
                print("\n\t> Your selected difficulty is 'Hard'")
                diffSelect = True
                difficulty = "hard"
                points = 10

            elif choice == 4: # Exit option - returns to Main Menu
                return

            else:
                print("\n\tInvalid Choice!")  # Validation - inputs can only be based on the choices shown in the Difficulty selection menu
    else:
        return

    for row in wordLst:
        if row[0] == category and row[1] == difficulty:
            shortLst.append(row[2])


    rnd = random.randint(0, len(shortLst) - 1) # Chooses a random word from shortLst
    print("\n\t\t'" + category + "' Category") # Reminds the player which Category they selected
    print("\t\t'" + difficulty + "' Difficulty") # Reminds the player which Difficulty they selected

    print("\n\t\t" + "_ " * len(shortLst[rnd]))
    print("\t\t" + str(len(shortLst[rnd])) + " letter word.") # States how many letters are in the word

    for letter in range (len(shortLst[rnd])):
        snowmanWord.append((shortLst[rnd][letter]).lower())
        maskedWord.append("_")

    while chance > 0 and "_" in maskedWord: # Game keeps running unless the player completes the word or loses all their chances
        guess = input("\n\t> Guess what letter might be in this word: ")

        while guess.strip() == "": # Validation - no blank space guesses
            print("\t Guess cannot be blank!")
            guess = input("\n\t> Guess what letter might be in this word: ")

        while len(guess) > 1: # Validation - guesses can only be one letter
            print("\t Only guess one letter at a time!")
            guess = input("\n\t> Guess what letter might be in this word: ")

        while not guess.isalpha(): # Validation - guesses can only be letters
            print("\t Guesses need to be letters only!")
            guess = input("\n\t> Guess what letter might be in this word: ")

        for letter in range (len(shortLst[rnd])):
            if guess.lower() in maskedWord[letter]:
                noRepeat = True
            else:
                print(end="")

            if snowmanWord[letter] == guess.lower():
                maskedWord[letter] = guess.lower() # reveals the correct guess at all instances in maskedWord
                validGuess = True
            else:
                print(end="")


        if noRepeat:
            print("\t  You already guessed this letter! Please try a different letter.")
        elif validGuess:
            print("\t  Success!")
        else:
            chance -= 1
            if chance > 0:
                print("\t  Incorrect! You have", chance, "chances left.")
            else:
                print(end="")


        if "_" in maskedWord and chance == 0: # Game Over print statement
            print("\n\tGame Over! The word was '" + ''.join(snowmanWord) + "'!")

        elif "_" in maskedWord and chance > 0: # Print the word with letters and underscores as the Snowman game continues
            print("\n\t\t", end="")
            for letter in maskedWord:
                print(letter, end=" ")
            print("\t\tCategory: '" + category + "'") # Reminder for the category selected at each guess

        else:
            print("\n\tYou guessed the word! It was '" + ''.join(snowmanWord) + "'!")
            name = input("\t> Please enter your initials (3 letters) to add your score to the scoreboard: ")
            index = -1

            while not name.isalpha() or name.strip() == "" or len(name) != 3: # Validation for initials input
                print("\n\t** Invalid initials! There must be no numbers, and it has to be 3 letters long! **")
                name = input("\n\t> Please enter your initials (3 letters) to add your score to the scoreboard: ")

            for indexValue in range(len(scoreboardLst)):
                if name.upper() in scoreboardLst[indexValue]: # Checks if the player is already stored in Scoreboard.txt
                    index = indexValue

            if index != -1: # Adds more points onto existing player's score
                currentScore = scoreboardLst[index][1]
                newScore = int(currentScore)
                newScore += points

                for row in scoreboardLst:
                    if row[0] == name.upper():
                        row[1] = int(row[1])
                        row[1] = newScore
                        row[1] = str(row[1])

                fileObj = open("Scoreboard.txt", "w")
                for row in scoreboardLst:
                    fileObj.write(str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "\n")
                fileObj.close()

            else: # Adds a new player into Scoreboard.txt
                day = dt.day
                month = dt.month
                year = dt.year
                date = (str(day) + "/" + str(month) + "/" + str(year))

                hours = dt.strftime("%H")
                minutes = dt.strftime("%M")
                time = str(hours) + ":" + str(minutes)

                fulldate = date + " " + time # The date and time the new player first played this game

                fileObj = open("Scoreboard.txt", "a")
                fileObj.write("\n" + name.upper() + "," + str(points) + "," + fulldate)
                fileObj.close()

        validGuess = False # Resets the following values after the game is finished
        noRepeat = False


def manageGame(catLst):
    # Setting up initial variables for manageGame function
    choice = 0  # variable for menu-based choices - Category and Difficulty

    categorySelect = False # Is set to True when a user selects a Category
    category = ""  # Stores which category you picked

    diffSelect = False  # Is set to True when a user selects a Difficulty
    difficulty = ""  # Stores which difficulty you picked

    while choice != (len(catLst)+2) and categorySelect == False:  # Loops the Category assignment menu unless the user selects the exit option
        try:
            print("\n\t== ASSIGN A CATEGORY ==")

            for index in range(len(catLst)):
                print("\t" + str(index + 1) + ")", catLst[index])

            print("\t" + str(len(catLst)+1) + ") Add a new category")
            print("\t" + str(len(catLst) + 2) + ") Exit")
            choice = int(input("\t> Enter your choice: "))

        except Exception as ex:
            print("\n\t" + str(ex))
            choice = 0


        if choice == len(catLst) + 1:
            newcat = input("\n\t\t> Enter new category: ")
            if newcat.strip() != "": # Checks if the Category input isn't blank spaces
                if newcat.lower() not in catLst: # Checks if the Category input doesn't already exist in Categories.txt
                    catLst.append(newcat)
                    fileObj = open("Categories.txt", "a")
                    fileObj.write(newcat.lower())
                    fileObj.close()
                    print("\n\t\t> New Category Added!", "'" + newcat.lower() + "'")
                    categorySelect = True
                    category = newcat.lower()
                else:
                    print("\t\t> This category already exists!")
            else:
                print("\t\t> Category cannot be blank!")

        elif choice == len(catLst) + 2:  # Exit option - returns to Main Menu
            return

        elif choice < 1 or choice > len(catLst): # Validation - inputs can only be based on the choices shown in the Category assignment menu
            print("\n\t> Invalid Choice!")

        else:
            print("\n\t> Your selected category is", "'" + catLst[choice - 1] + "'")
            categorySelect = True
            category = catLst[choice - 1]


    if categorySelect: # Will only proceed to Difficulty assignment menu if the user has chosen a Category
        while choice != (len(catLst) + 1) and diffSelect == False: # Loops the Difficulty selection menu unless the player selects the exit option
            try:
                print("\n\t== ASSIGN A DIFFICULTY ==")

                print("\t1) Easy")
                print("\t2) Medium")
                print("\t3) Hard")
                print("\t4) Exit")

                choice = int(input("\t> Enter your choice: "))

            except Exception as ex:
                print("\n\t" + str(ex))
                choice = 0

            if choice == 1:
                print("\n\t> Your selected difficulty is 'Easy'")
                diffSelect = True
                difficulty = "easy"

            elif choice == 2:
                print("\n\t> Your selected category is 'Medium'")
                diffSelect = True
                difficulty = "medium"

            elif choice == 3:
                print("\n\t> Your selected category is 'Hard'")
                diffSelect = True
                difficulty = "hard"

            elif choice == 4:
                return

            else:
                print("\n\tInvalid Choice!")  # Validation - inputs can only be based on the choices shown in the Difficulty assignment Menu
    else:
        return

    if choice == 1 or choice == 2 or choice == 3:
        word = input("\n\t> Enter your new word to add: ")
        while word.strip() == "": # Validation - no blank space inputs allowed
            print("\t> Word cannot be blank!")
            word = input("\n\t> Enter your new word to add: ")

        fileObj = open("Words.txt", "a") # Adds the new word to Words.txt, with its assigned Category and Difficulty
        fileObj.write(category + "," + difficulty + "," + word + "\n")
        fileObj.close()
        print("\n\tWords file updated!")
    else:
        return