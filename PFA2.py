import PFA2GameFunctions


def menu():
    print("\n== Snowman - Main Menu ==")
    print("1) Play the Game")
    print("2) Show Scoreboard")
    print("3) Manage Game")
    print("4) Exit")
    choice = int(input("> Enter your choice: "))
    return choice


def showScoreboard(scoreboardLst):
    loadScoreboard()
    print(",__________,_______,____________________,") # Table-like formatting for showing scoreboard
    print("| Initials | Score |    First played    |")
    print("|__________|_______|____________________|")
    for row in scoreboardLst[:5]:
        for column in row:
            if column == row[0]: # Spacing for first column - initials
                print("|  ", column, end="    |   ")

            elif column == row[1] and len(row[1]) == 1: # Spacing for second column - if Score is in single digits
                print(column, end="   |  ")

            elif column == row[1] and len(row[1]) == 3:  # Spacing for second column - if Score is in triple digits
                print(column, end=" |  ")

            elif len(row[2]) == 15:  # Spacing for third column - if the date is not in two digits in a given month e.g. the 9th instead of the 10th of December
                print(column, end="  |   ")

            else:
                print(column, end="  |  ")
        print()
        print("|__________|_______|____________________|")


def loadScoreboard():
    fileObj = open("Scoreboard.txt", "r") # Loads Scoreboard.txt into the program

    for line in fileObj: # Stores the .txt file as a 2D List in the program
        line = line.rstrip("\n")
        lineLst = line.split(",")
        lineLst[0] = lineLst[0].lstrip()
        lineLst[1] = lineLst[1].lstrip()
        lineLst[2] = lineLst[2].lstrip()
        scoreboardLst.append(lineLst)

    fileObj.close()
    return scoreboardLst


def sortScore(row):
    return int(row[1])


def loadCategories():
    fileObj = open("Categories.txt", "r") # Loads Categories.txt into the program

    for line in fileObj: # Stores the .txt file as a List in the program
        line = line.rstrip("\n")
        catLst.append(line)

    fileObj.close()
    return catLst


def loadWords():
    fileObj = open("Words.txt", "r") # Loads Scoreboard.txt into the program

    for line in fileObj:  # Stores the .txt file as a 2D List in the program
        line = line.rstrip("\n")
        lineLst = line.split(",")
        lineLst[0] = lineLst[0].lstrip()
        lineLst[1] = lineLst[1].lstrip()
        lineLst[2] = lineLst[2].lstrip()
        wordLst.append(lineLst)

    fileObj.close()
    return wordLst


def main():
    # Initialises Lists as global variables which can be re-used throughout the program
    global scoreboardLst
    global catLst
    global wordLst

    scoreboardLst = []
    catLst = []
    wordLst = []

    scoreboardLst = loadScoreboard()
    catLst = loadCategories()
    wordLst = loadWords()

    scoreboardLst.sort(key=sortScore, reverse=True)

    choice = 0

    while choice != 4: # Loops the Main Menu unless you select the exit option
        try:
            choice = menu()
        except Exception as ex:
            print("\n\tERROR:", ex)
            choice = 0

        if choice == 1:
            PFA2GameFunctions.playGame(wordLst, catLst, scoreboardLst)
        elif choice == 2:
            showScoreboard(scoreboardLst)
        elif choice == 3:
            PFA2GameFunctions.manageGame(catLst)
        elif choice == 4:
            print("\n\tThank you for playing!")
        else:
            print("\n\tInvalid choice!") # Validation - inputs can only be based on the choices shown in the Main Menu


main()