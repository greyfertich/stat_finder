import const
from teams import TEAMS
import collections

class TeamFinder:
    def __init__(self):
        self.Team = collections.namedtuple('Team', 'name abbrev league')

    def find(self, team_name):
        for sport in TEAMS:
            if team_name in TEAMS[sport]:
                return self.Team(name=team_name, abbrev=TEAMS[sport][team_name], league=sport)

        raise ValueError("Invalid Team Name")
