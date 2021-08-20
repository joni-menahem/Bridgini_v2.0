class Bridgini:
    def __init__(self, player_names, rounds_to_play, player_scores, who_lost, leading_color):
        self.player_names = player_names
        self.rounds_to_play = rounds_to_play
        self.player_scores = player_scores
        self.who_lost = who_lost
        self.leading_color = leading_color

    def get_number_of_players(self):
        pass

    def change_playing_order(self):
        pass

    def deal_cards_4_players(self):
        pass

    def deal_card_3_players(self):
        pass

    def get_leading_color(self):
        pass

    def is_color_in_list(self):
        pass

    def is_valid_color(self):
        pass

    def is_card_in_list(self):
        pass

    def get_card_score(self):
        pass

    def get_max_card(self):
        pass

    def get_player_holding_max_card(self):
        pass

    def get_turn_score(self):
        pass

    def get_looser_name(self):
        pass

    def get_winner_name(self):
        pass


class Player:
    def __init__(self, name, score, number_of_wins_in_a_row):
        self.name = name
        self.score = score
        self.number_of_wins_in_a_row = number_of_wins_in_a_row

    def get_player_name(self):
        pass

    def get_player_score(self):
        pass

    def get_number_of_wins_in_a_row(self):
        pass


class Deck:
    def __init__(self, number_of_cards):
        self.number_of_cards = number_of_cards
