# Higher or Lower

import random

# card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pop one of the top of the deck and return
    return thisCard

# pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # make a copy of the starting deck
    random.shuffle(deckListIn)
    return deckListOut

#Main Code
print('Welcome to Higher or Lower !')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisvalue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisvalue + 1}
        startingDeckList.append(cardDict)
    score = 50

while True: # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuite = currentCardDict['suit']
    print('Starting card is:', currentCardRank + 'of ' + currentCardSuite)
    print()

    for cardNumber in range(0, NCARDS): # play one game of this many cards
        answer = input('Will the next card be higher or lower than the'
                       + currentCardRank + 'of '
                       + currentCardSuite + '? (enter h or l): ')
        answer = answer.casefold() # force lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardValue = nextCardDict['value']
        nextCardSuite = nextCardDict['suit']
        print('Next card is:', nextCardRank + ' of ' + nextCardSuite)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
            else:
                print('Sorry, it was not higher')
                score = score - 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')
            else:
                print('Sorry, it was not lower')
                score = score - 15

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue # don't need current suit

        goAgain = input('To play again, press Enter, or "q" to quit:')
        if goAgain.lower() == 'q':
            break
    print('OK, bye')

