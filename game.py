import logging
import json
import os
from datetime import datetime, date, timedelta
from player import Player

logging.basicConfig(level=logging.DEBUG)
logging.getLogger(__name__)

class Game:

    def __init__(self, p1, p2, p3, p4, s1, s2, s3, s4):
        player1 = Player(p1, s1)
        player2 = Player(p2, s2)
        player3 = Player(p3, s3)
        player4 = Player(p4, s4)
        self.players = [player1, player2, player3, player4]

    def winner(self):
        for player in self.players:
            if player.score >= 10:
                return player.name

    def winning_score(self):
        for player in self.players:
            if player.score >= 10:
                return player.score
        
