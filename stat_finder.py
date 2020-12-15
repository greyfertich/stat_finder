from nfl_stat_finder import NFLStatFinder
from team_finder import TeamFinder
import const

class StatFinder:
    def __init__(self):
        self.teamFinder = TeamFinder()
        self.NFLStatFinder = NFLStatFinder()

    def find(team_name):
        team = self.teamFinder.find(team_name)
        statFinder = getStatFinderForLeague(team.league)
        return statFinder.find(team.name)

    def getStatFinderForLeague(league):
        if league == const.NFL:
            return self.NFLStatFinder
        raise ValueError("Invalid League Name")
