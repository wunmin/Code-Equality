


### This function tells player what number to pick for each spot on the board.
def guideBoard():
    print "Refer to this board for the spot number:"
    print "   |   |"
    print " 0 | 1 | 2"
    print "   |   |"
    print "-----------"
    print "   |   |"
    print " 3 | 4 | 5"
    print "   |   |"
    print "-----------"
    print "   |   |"
    print " 6 | 7 | 8"
    print "   |   |"


### This function willl take in a list of 9 items and display each item. To display the item in the list, we do list[x], where [x] begins with 0, instead of 1.
def drawBoard(game):
    print('   |   |')
    print(' ' + game[0] + ' | ' + game[1] + ' | ' + game[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game[3] + ' | ' + game[4] + ' | ' + game[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game[6] + ' | ' + game[7] + ' | ' + game[8])
    print('   |   |')


### We keep a total count of plays made, starting with 1. If the total count divided by 2 has a remainder of 1, it means the current player is Player 1.
### If the total count divided by 2 has not remainder, it means the current player is Player 2. 
def playerNumber(playerNo):
    ## Write your code below
    ## You take in 1 input called playerNo, and output 2 numbers: 1 and 2


    """ 
    To test your codes, try the following:

    def playerNumber(playerNo):
        Your codes here

    playerNumber(5)
    >>> 1

    playerNumber(4)
    >>> 2

    """

    if ??? % ??? == ???:
        return ???
    else:
        return ???


### First player's letter is "O" while second player's letter is "X" 
def playerLetter(num):
    ## Write your code below
    ## You take in 1 input called num, and output 2 letters: "O" or "X"
    ## You will be using the function playerNumber(playerNo) 

    """
    To test your codes, try the following:

    def playerNumber(playerNo):
        Your codes here

    def playerLetter(num):
        Your codes here
        In your test code, do a print to check if you're printing the right sign, i.e. "X" or "O".
        Once you verify that you do have the correct codes, take away your print statements.

    playerLetter(1)
    >>> O

    playerLetter(2)
    >>> X

    """
    if ???(num) == ???:
        return "O"
    else:
        return "X"


### Here we check if the spot that the Player picks is clearn, i.e. contains a spacebar " ".
def spotClear(spotPicked):
    return boardList[spotPicked] == " "
    ## You don't need to do anything for this



### Here we ask the Player to give us an input on which spot on the board they would like to play. While 
def playerMove():
    numbers = range(9)
    spot = validateInput("Pick a spot by keying in a number between 0 to 8.\n")
    spot = int(spot)

    ## Write your code below
    ## You will need a while loop here. There are two conditions here:
    ## Condition 1: "spot" not in numbers list, i.e. not a number in 0 - 8
    ## Condition 2: the "spot" the player pick is no longer available. Use the "spotClear(spotPicked)" function to check if spot is clear
    ## If both Condition 1 and Condition 2 are true, this means you need to get the player to pick a spot again.
    ## You can re-use one line of code from above in this same function. Pick wisely!

    """
    To test your codes, do the following:

    When prompted for an input, try these 3 inputs:
    (1) "e". The computer should print "Whoops, that is not a number!"
    (2) 3. The computer will check and discover that spot #3 is taken, and ask you to key in the input again
    (3) 2. The computer will check and discover that spot #2 is free, and print out and return the spot name.
        The "print spot" is only to be used in the test. Don't include it in your actual code.



    boardList = [" "] * 9
    boardList[3] = "X"

    def spotClear(spotPicked):
        return boardList[spotPicked] == " "

    def playerMove():
        numbers = range(9)
        spot = validateInput("Pick a spot by keying in a number between 0 to 8.\n")
        spot = int(spot)

        YOUR CODES HERE

        print spot
        return int(spot)
  
    def validateInput(inputMsg):
        while True:
            try:
                userInput = int(raw_input(inputMsg))
                return userInput
             except ValueError:
                print "Whoops, that is not a number!"
            

    playerMove()

    """

    while ??? or not ???(spot):
        spot = validateInput("Pick a spot by keying in a number between 0 to 8.\n")

    return int(spot)



### Here we check if the input is an integer. If it is not an integer, print an error message. 
### Thanks SM for helping fix this!    
def validateInput(inputMsg):
    while True:
        try:
            userInput = int(raw_input(inputMsg))
            return userInput
        except ValueError:
            print "Whoops, that is not a number!"



    
### Here we change the item in the list to the player's letter, which is either "O" or "X"
### This function may look simple, but you'll see that it combines 3 functions in one line
def markSpot():
    boardList[playerMove()] = playerLetter(playerNum)


### This function checks all the combinations that would enable the player to win the game.
def hasWon(bo, le):
    if (
    (bo[0] == le and bo[1] == le and bo[2] == le) or # across the top
    (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
    (bo[6] == le and bo[7] == le and bo[8] == le) or # across the bottom
    (bo[0] == le and bo[3] == le and bo[6] == le) or # down the left side
    (bo[1] == le and bo[4] == le and bo[7] == le) or # down the middle
    (bo[2] == le and bo[5] == le and bo[8] == le) or # down the right side
    (bo[0] == le and bo[4] == le and bo[8] == le) or # diagonal
    (bo[2] == le and bo[4] == le and bo[6] == le)):# diagonal
        drawBoard(boardList)
        print "You have won!"
        return False
    else:
    	return True

## Check if the board has already been fully played, i.e. no more empty spots left
def boardIsFull():
    ## Tips: use a for loop combined with an if statement. This function needs to either return a True or a False
    ## If there are spots left (i.e.board is not full), return True. Else, if no spots are left, return False.

    for i in range(???):
        if ???(i):
            return True
    return False



boardList = [" "] * 9


print "Welcome to Tic Tac Toe!"
	
playerNum = 1

runGame = True

while runGame == True:
    ## When all your codes above are ready, uncomment the 3 lines below by taking away the "#"
    runGame = boardIsFull()
    guideBoard()
    #print "It is Player " + str(playerNumber(playerNum)) + "\'s turn. The letter you play is " + playerLetter(playerNum)
    drawBoard(boardList)
    #markSpot()
    #runGame = hasWon(boardList, playerLetter(playerNum))
    playerNum += 1