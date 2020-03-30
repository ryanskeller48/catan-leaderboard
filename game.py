import logging
import json
import os
from datetime import datetime, date, timedelta
from player import Player

logging.basicConfig(level=logging.DEBUG)
logging.getLogger(__name__)

NAME_INDEX = 0
SCORE_INDEX = 1

class Game:

    def __init__(self, p1, p2, p3, p4, s1, s2, s3, s4, timestamp=None):
        self.players = [[p1, s1], [p2, s2], [p3, s3], [p4, s4]]
        self.timestamp = timestamp

    def winner(self):
        for player in self.players:
            if player[SCORE_INDEX] >= 10:
                return player[NAME_INDEX]

    def winning_score(self):
        for player in self.players:
            if player[SCORE_INDEX] >= 10:
                return player[SCORE_INDEX]
        
