import random
from functions import Bridgini
from functions import Player
from functions import rotateList
from functions import is_valid_card
from functions import is_color_in_list
from functions import get_card_score
from functions import get_max_card
from functions import get_player_index_with_max_card
from functions import get_turn_score


# initializing 4 players for the game
Player1 = Player(name='Ido', cards=[])
Player2 = Player(name='Liran', cards=[])
Player3 = Player(name='Yoni', cards=[])
Player4 = Player(name='Dor', cards=[])

# creating the data for the Bridgini class
player_names = [Player1.get_player_name(), Player2.get_player_name(),
                Player3.get_player_name(), Player4.get_player_name()]
player_scores = [Player1.get_player_score(), Player2.get_player_score(),
                 Player3.get_player_score(), Player4.get_player_score()]
rounds_to_play = 4
who_lost_round = ''
who_lost_turn = ''

# initializing Bridgini Game
Game = Bridgini(player_names=player_names, rounds_to_play=rounds_to_play, player_scores=player_scores,
                who_lost_round=who_lost_round, who_lost_turn=who_lost_turn, leading_color='')

firstPlayer = random.choice(Game.player_names)

while Game.get_number_of_players() != 4:  # checking for legal player count
    print("can't play, my Bridgini is designed for 4 players, try again")
    break

while Game.get_round_number() != 0:
    # the first player decides what card to throw based on the name of the card (exact match)
    if Game.get_round_number() == 4:  # first round of the new game
        print('The first player (randomly chosen) is:', firstPlayer)
        rotate = Game.get_player_names().index(firstPlayer)
        newNames = rotateList(Game.get_player_names(), -rotate)  # the correct playing order when first player is known
    else:
        print('The first player (lost the previous round) is:', Game.get_who_lost_round())
        rotate = Game.get_player_names().index(Game.get_who_lost_round())
        newNames = rotateList(Game.get_player_names(), -rotate)  # the correct playing order when first player is known

    if Game.get_number_of_players() == 4:
        player1Cards, player2Cards, player3Cards, player4Cards = Game.deal_cards_4_players()
        Player1.sort_cards(Player1.update_cards(player1Cards))
        Player2.sort_cards(Player2.update_cards(player2Cards))
        Player3.sort_cards(Player3.update_cards(player3Cards))
        Player4.sort_cards(Player4.update_cards(player4Cards))

        while Player1.get_card_count() != 0:  # the actual game for 4 players

            print("cards for", newNames[0], ':', Player1.get_player_cards())
            print("cards for", newNames[1], ':', Player2.get_player_cards())
            print("cards for", newNames[2], ':', Player3.get_player_cards())
            print("cards for", newNames[3], ':', Player4.get_player_cards())

            # player 1 turn
            print(newNames[0], ', You are the first to play')
            card1 = input('choose a card to throw:')
            while not is_valid_card(card1[0], card1, player1Cards):
                print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                card1 = input('choose a card to throw:')
            player1Cards.remove(card1)
            Game.set_leading_color(get_leading_color(card1))
            print("Leading Color Is:", get_leading_color(card1))

            # player 2 turn
            print(newNames[1], ', Your turn to play')
            card2 = input('choose a card to throw:')
            while not is_valid_card(card1[0], card2, player2Cards):
                print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                card2 = input('choose a card to throw:')
            player2Cards.remove(card2)

            # player 3 turn
            print(newNames[2], ', Your turn to play')
            card3 = input('choose a card to throw:')
            while not is_valid_card(card1[0], card3, player3Cards):
                print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                card3 = input('choose a card to throw:')
            player3Cards.remove(card3)

            # player 4 turn
            print(newNames[3], ', Your turn to play')
            card4 = input('choose a card to throw:')
            while not is_valid_card(card1[0], card4, player4Cards):
                print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                card4 = input('choose a card to throw:')
            player4Cards.remove(card4)

            turn = [card1, card2, card3, card4]
            print(newNames[0] + ':', card1)
            print(newNames[1] + ':', card2)
            print(newNames[2] + ':', card3)
            print(newNames[3] + ':', card4)

            maxCard = get_max_card(turn)
            index = get_player_index_with_max_card(turn, maxCard)
            turnScore = get_turn_score(turn)
            Game.update_players_score(index, turnScore)
            print("this turn score is:", Game.get_players_score())
            print('Turn is over. the looser is:', Game.get_looser_name())
            rotate = newNames.index(Game.get_who_lost_turn())
            newNames = rotateList(newNames, -rotate)
            Game.set_players_score(rotateList(Game.get_players_score(), -rotate))

        print('Round is over. the looser is:', Game.get_looser_name())
        Game.set_who_lost_round(Game.get_looser_name())
        Game.update_round_number_by_one()


print('The winner of the game is:', Game.get_winner_name())




