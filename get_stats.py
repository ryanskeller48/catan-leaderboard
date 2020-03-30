from scoreboard import Scoreboard
import sys

def main():
    name = sys.argv[1]
    s = Scoreboard("games.csv")
    print (s.get_win_pct_leaderboard(min_games=3))

if __name__ == "__main__":
    main()
