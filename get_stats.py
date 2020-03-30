from scoreboard import Scoreboard
import sys

def main():
    name = sys.argv[1]
    s = Scoreboard("games.csv")
    print (s.get_win_pct_leaderboard(min_games=3))
    print ("---------------")
    print (s.get_wins_leaderboard())
    print ("---------------")
    print (s.get_player_stats("Neville"))

if __name__ == "__main__":
    main()
