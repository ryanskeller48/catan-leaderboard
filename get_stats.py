from scoreboard import Scoreboard
import sys

def main():
    name = sys.argv[1]
    s = Scoreboard("games.csv")
    print (s.get_player_stats(name))

if __name__ == "__main__":
    main()
