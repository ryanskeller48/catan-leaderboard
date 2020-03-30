import logging
import json
import os
import statistics
from datetime import datetime, date, timedelta

logging.basicConfig(level=logging.DEBUG)
logging.getLogger(__name__)

NAME_INDEX = 0
SCORE_INDEX = 1

class Player:

    def __init__(self, name):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games += [game]

    def tally_points(self):
        total = 0
        for game in self.games:
            for player in game.players:
                if player[NAME_INDEX] == self.name:
                    total += player[SCORE_INDEX]
        return total

    def num_wins(self):
        wins = 0
        for game in self.games:
            if game.winner() == self.name:
                wins += 1
        return wins

    def num_wins_3man(self):
        wins = 0
        for game in self.games:
            if game.players[3][0] is None: # no 4th player
                if game.winner() == self.name:
                    wins += 1
        return wins

    def num_wins_4man(self):
        wins = 0
        for game in self.games:
            if game.players[3][0] is not None:
                if game.winner() == self.name:
                    wins += 1
        return wins

    def avg_points(self):
        points = self.tally_points()
        return float(points) / len(self.games)

    def median_score(self):
        scores = []
        for game in self.games:
            for player in game.players:
                if player[NAME_INDEX] == self.name:
                    scores += [player[SCORE_INDEX]]
        return statistics.median(scores)

    def lowest_score(self):
        lowest = 11
        for game in self.games:
            for player in game.players:
                if player[NAME_INDEX] == self.name:
                    if player[SCORE_INDEX] < lowest:
                        lowest = player[SCORE_INDEX]
        return lowest

    def win_pct(self):
        wins = self.num_wins()
        return (str(float(wins)/len(self.games) * 100) + "%")

    def win_pct_3man(self):
        """ win % in 3-man games """
        wins = 0
        num_games = 0
        for game in self.games:
            if game.players[3][0] is None: # no 4th player
                num_games += 1
                if game.winner() == self.name:
                    wins += 1
        if num_games == 0: return "No 3-man games played"
        else: return (str(float(wins)/num_games * 100) + "%")

    def win_pct_4man(self):
        """ win % in 4-man games """
        wins = 0
        num_games = 0
        for game in self.games:
            if game.players[3][0] is not None:
                num_games += 1
                if game.winner() == self.name:
                    wins += 1
        if num_games == 0: return "No 4-man games played"
        else: return (str(float(wins)/num_games * 100) + "%")

    def win_pct_by_opp(self):
        """ win % broken down per-opponent """
        opps = {}
        for game in self.games:
            win = (game.winner() == self.name)
            for player in game.players:
                if player[NAME_INDEX] == self.name:
                    continue
                elif player[NAME_INDEX] is None:
                    continue
                elif player[NAME_INDEX] in opps:
                    opps[player[NAME_INDEX]][0] += 1 # add one to the games played tally
                    if win:
                        opps[player[NAME_INDEX]][1] += 1 # add one to the games won tally
                else:
                    if win:
                        opps[player[NAME_INDEX]] = [1, 1]
                    else:
                        opps[player[NAME_INDEX]] = [1, 0]
        #return opps
        outstring = ""
        for opp in opps:
            outstring += f"{opp}: {float(opps[opp][1])/opps[opp][0] * 100}% \n"
        return outstring
