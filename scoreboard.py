import logging
import json
import os
from datetime import datetime, date, timedelta
from game import Game
from player import Player
import csv

logging.basicConfig(level=logging.DEBUG)
logging.getLogger(__name__)

class Scoreboard:

    def __init__(self, input_file):
        self.games, self.players = self.process_games(input_file)

    def processCSV(self, input_file):
        with open(input_file) as f:
            input_reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in input_reader:
                yield row

    def process_games(self, input_file):
        tick = 0
        games = []
        players = {}
        for s1, p1, s2, p2, s3, p3, s4, p4 in self.processCSV(input_file):
            if tick < 3: # headers
                tick += 1
            #elif tick > 8:
                #break
            else:
                if p4 == "": 
                    p4 = None; s4 = None
                    g = Game(p1, p2, p3, p4, int(s1), int(s2), int(s3), s4)
                else:
                    g = Game(p1, p2, p3, p4, int(s1), int(s2), int(s3), int(s4))
                games += [g]

                for p in [p1, p2, p3, p4]:
                    if p in players:
                        players[p].add_game(g)
                    else:
                        new_player = Player(p)
                        players[p] = new_player
                        players[p].add_game(g)
                tick += 1
        return games, players

    def get_player_stats(self, name):
        if name not in self.players:
            return "Bad player name"
        else:
            outstring = ""
            p = self.players[name]
            outstring += "Player: " + p.name + "\n"
            outstring += "Wins: " + str(p.num_wins()) + "\n"
            outstring += "Win % 3man: " + str(p.win_pct_3man()) + "\n"
            outstring += "Win % 4man: " + str(p.win_pct_4man()) + "\n"
            outstring += "Win % by opponent:" + "\n"
            outstring += p.win_pct_by_opp()
            return outstring