from stat_finder import StatFinder
from team_finder import TeamFinder

if __name__ == "__main__":
    statFinder = StatFinder()

    team_name = input("Enter the team you are looking for: ")
    team_stats = statFinder.find(team_name)
