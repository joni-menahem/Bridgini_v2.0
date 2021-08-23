import random


def rotateList(list_in, x):
    # rotating the list to the left by 'x' steps
    return list_in[-x % len(list_in):] + list_in[:-x % len(list_in)]


def is_valid_card(leading_color, card, cards):
    # check if the card chosen is valid for play: True-Valid / False-Not Valid
    # input: "leading_color" as a single letter, "card" as string, "cards" as list.
    if card in cards and card[0] == leading_color:
        return True
    elif is_color_in_list(cards, leading_color):
        return False
    else:
        return True


def is_color_in_list(cards, color):
    # check if a list of cards contains a specific color
    inList = False
    count = 0
    for i in range(len(cards)):
        if cards[i][0] == color:
            count += 1
    if count != 0:
        inList = True
    return inList


def get_card_score(card):
    # input the cards in turn and current score and updates the current score
    scoreDict = {"r1": 1, "r2": 1, "r3": 1, "r4": 1, "r5": 1, "r6": 1, "r7": 1, "r8": 1, "r9": 5, "r10": 1,
                 "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 0, "b9": 3, "b10": 0,
                 "o1": 0, "o2": 0, "o3": 0, "o4": 0, "o5": 0, "o6": 0, "o7": 0, "o8": 0, "o9": 3, "o10": 0,
                 "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "g9": 3, "g10": 0}
    score = scoreDict[card]
    return score


def get_max_card(list_of_cards):
    # finding the max card in a turn to check who takes all
    leadColor = list_of_cards[0][0]
    maxList = []
    for i in range(len(list_of_cards)):
        if list_of_cards[i][0] == leadColor:
            maxList.append(int(list_of_cards[i][1:]))
    maxNumber = max(maxList)
    maxCard = leadColor + str(maxNumber)
    return maxCard


def get_player_index_with_max_card(list_of_cards, max_card):
    # find the player name with the highest card per turn
    for index in range(len(list_of_cards)):
        if list_of_cards[index] == max_card:
            return index


def get_turn_score(turn):
    # find the total score per turn (sum of 4 cards)
    turnScore = 0
    for i in range(len(turn)):
        turnScore += get_card_score(turn[i])
    return turnScore


class Bridgini:
    def __init__(self, player_names, rounds_to_play, player_scores, who_lost_round, who_lost_turn, leading_color):
        self.player_names = player_names
        self.rounds_to_play = rounds_to_play
        self.player_scores = player_scores
        self.player_cards = [0] * len(self.player_names)
        self.who_lost_round = who_lost_round
        self.who_lost_turn = who_lost_turn
        self.leading_color = leading_color

    def get_who_lost_turn(self, name):
        return self.who_lost_turn

    def set_who_lost_turn(self, name):
        self.who_lost_turn = name

    def get_who_lost_round(self, name):
        return self.who_lost_round

    def set_who_lost_round(self, name):
        self.who_lost_round = name

    def get_players_score(self):
        return self.player_scores

    def update_players_score(self, index, score):
        self.player_scores[index] += score

    def set_players_score(self, new_score):
        self.player_scores = new_score

    def set_leading_color(self, color):
        self.leading_color = color

    def update_round_number_by_one(self):
        self.rounds_to_play -= 1

    def get_round_number(self):
        return self.rounds_to_play

    def get_number_of_players(self):
        return len(self.player_names)

    def get_player_names(self):
        return self.player_names

    def get_who_lost_round(self):
        return self.who_lost_round

    def get_who_lost_turn(self):
        return self.who_lost_turn

    def deal_cards_4_players(self):
        # dealing the cards for 4 players
        deck = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
                "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
                "o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
                "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]
        self.player_cards[0] = []
        self.player_cards[1] = []
        self.player_cards[2] = []
        self.player_cards[3] = []
        while len(self.player_cards[0]) < 10:
            # player number 1
            card = random.choice(deck)
            deck.remove(card)
            self.player_cards[0].append(card)
            # player number 2
            card = random.choice(deck)
            deck.remove(card)
            self.player_cards[1].append(card)
            # player number 3
            card = random.choice(deck)
            deck.remove(card)
            self.player_cards[2].append(card)
            # player number 4
            card = random.choice(deck)
            deck.remove(card)
            self.player_cards[3].append(card)

        return self.player_cards[0], self.player_cards[1], self.player_cards[2], self.player_cards[3]

    def deal_card_3_players(self):
        # dealing the cards for 3 players
        deck = ["r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
                "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
                "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
                "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]
        self.player_cards[0] = []
        self.player_cards[1] = []
        self.player_cards[2] = []

        while len(self.player_cards[0]) < 10:
            # player number 1
            card = random.choice(deck)
            deck.remove(card)
            self.player_cards[0].append(card)
            # player number 2
            card = random.choice(deck)
            deck.remove(card)
            self.player_cards[1].append(card)
            # player number 3
            card = random.choice(deck)
            deck.remove(card)
            self.player_cards[2].append(card)

        return self.player_cards[0], self.player_cards[1], self.player_cards[2]

    def get_looser_name(self):
        # returns the player with the most amount of bad points (if a tie will select randomly)
        # the looser will start the next round
        maxScore = max(self.player_scores)
        looser = []
        for i in range(len(self.player_scores)):
            if self.player_scores[i] == maxScore:
                looser.append(self.player_names[i])
        if len(looser) == 1:
            return looser[0]
        else:
            index = random.randint(0, len(looser) - 1)
            return looser[index]

    def get_winner_name(self):
        # returns the winner score with the least amount of bad score (if a tie will display both)
        minScore = min(self.player_scores)
        winner = []
        for i in range(len(self.player_scores)):
            if self.player_scores[i] == minScore:
                winner.append(self.player_names[i])
        if len(winner) == 1:
            return winner[0]
        else:
            print('There is a tie! there are multiple winners !')
            return winner


class Player:
    def __init__(self, name, cards):
        self.name = name
        self.score = 0
        self.cards = cards

    def sort_cards(self, cards):
        # will sort based on color first (blue, green, orange, red) and then by value
        self.cards = sorted(cards, key=lambda x: (x[0], int(x[1:])))
        return self.cards

    def update_cards(self, cards):
        self.cards = cards

    def get_player_cards(self):
        return self.cards

    def get_card_count(self):
        return len(self.cards)

    def get_player_name(self):
        return self.name

    def get_player_score(self):
        return self.score
