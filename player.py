import logging
import json
import os
from datetime import datetime, date, timedelta

logging.basicConfig(level=logging.DEBUG)
logging.getLogger(__name__)

class Player:

    def __init__(self, name, score, color=None):
        self.name = name
        self.score = score
        self.color = color
