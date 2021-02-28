import random
from random import choice
import time

#Does the match play itself
automate = True

def pause_hand():
    input("Hit enter to go to next battle")

suits = ['hearts', 'diamonds', 'spades', 'clubs']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
numbers_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

card_dict = dict(list(zip(numbers, numbers_values)))




def rungame():
    p1cards_deck = []
    p2cards_deck = []
    masterDeck = []

    # Create random decks of cards for each player
    while len(masterDeck) < 52:
        card_suit = choice(suits)
        card_num = choice(numbers)
        card = (card_num, card_suit)
        if card not in masterDeck:
            masterDeck.append(card)

    # print(masterDeck)
    # Create random decks of cards for each player
    while len(masterDeck) > 0:
        c1 = masterDeck.pop()
        c2 = masterDeck.pop()

        p1cards_deck.append(c1)
        p2cards_deck.append(c2)

    # Initialize variables for play and scores
    turncount = 0
    p1_score = 0
    p2_score = 0
    tie = 0
    tie_pile = [] #used to track the cards dealt in a tie. The next winner gets the whole pile.

    while len(p1cards_deck) > 0 and len(p2cards_deck) > 0:
        turncount += 1
        #pause_weapon() #I didn't like hitting enter twice
        # print(len(p1cards_deck), len(p2cards_deck))
        # print()
        deal_player1 = p1cards_deck.pop(0)  # remove player1 next card from the deck to play
        deal_player2 = p2cards_deck.pop(0)
        value1 = deal_player1[0]  # string value of card player 1
        value2 = deal_player2[0]  # string value of card player 2

        # print('Player 1 - ', deal_player1[0], 'of', deal_player1[1])
        # print('Player 2 - ', deal_player2[0], 'of', deal_player2[1], '\n')

        chance = random.randrange(0, 100) #choose the random value for the order of the winnings
        if card_dict[value1] > card_dict[value2]:
            p1_score += 1
            # print("Player 1 wins!!\n")
            if len(tie_pile): #if there are cards in the tie pile
                # print("Player 1 won ", tie_pile, " from the tie pile") #state what the player wins
                for card in tie_pile: #for each card
                    p1cards_deck.append(card) #add it to the winner's pile
                tie_pile.clear() #clear the tie pile
            if chance >= 50: #50/50 chance for one player's card to be put in "on top"
                p1cards_deck.append(deal_player1)
                p1cards_deck.append(deal_player2)
            else:
                p1cards_deck.append(deal_player2)
                p1cards_deck.append(deal_player1)


        elif card_dict[value2] > card_dict[value1]: #this whole elif is the same as above
            p2_score += 1
            # print("Player 2 wins!!\n")
            if len(tie_pile):
                # print("Player 2 won ", tie_pile, " from the tie pile")
                for card in tie_pile:
                    p2cards_deck.append(card)
                tie_pile.clear()
            if chance >= 50:
                p2cards_deck.append(deal_player1)
                p2cards_deck.append(deal_player2)
            else:
                p2cards_deck.append(deal_player2)
                p2cards_deck.append(deal_player1)
        else:
            # print("It's a tie")
            tie += 1
            for i in range(0, 3): #put 3 cards from each person in the tie pile.
                if len(p1cards_deck) >= 1 and len(p2cards_deck) >= 1:
                    tie_pile.append(p1cards_deck.pop(0))
                    tie_pile.append(p2cards_deck.pop(0))
                else:
                    break
        if not automate: #used for testing purposes the play the whole match in a second
            pause_hand()

    # print("Final Score: Player 1:", p1_score, 'and Player 2:', p2_score, "There were", tie, 'ties')
    # if p1_score > p2_score:
    #     print("Player 1 is victorious")
    # elif p2_score > p1_score:
    #     print("Player 2 is victorious")
    # else:
    #     print("It's a draw")
    return turncount

master_list = []

games_to_run = 100000
update_factor = 100
update_interval = games_to_run/update_factor
start = time.time()
for i in range(0, games_to_run):
    master_list.append(rungame())
    if i != 0 and i%update_interval == 0:
        percentage = (i/games_to_run)*100
        timelapsed = time.time()-start
        timecalc = timelapsed/(percentage/100) - timelapsed
        print(str(percentage) + "% done. " + str(timecalc) + " seconds left.")
        #print("Approximately " + str(timecalc) + " seconds left.")

minimum = 1000
maximum = 0
mean_list = 0

for game in master_list:
    length = game
    if length > maximum:
        maximum = length
    elif length < minimum:
        minimum = length

    mean_list += length

mean = mean_list/games_to_run
print("\n-----War Analysis-----")
print("Over " + str(games_to_run) + " games, the average number of turns was " + str(mean))
print("The max number of turns was " + str(maximum) + " and the minimum number of turns was " + str(minimum))


##Over 100000 games, the average number of turns was 146.39753
##The max number of turns was 582 and the minimum number of turns was 10














