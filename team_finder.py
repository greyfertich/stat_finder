import const
from teams import TEAMS
import collections

class TeamFinder:
    def __init__(self):
        self.Team = collections.namedtuple('Team', 'name sport')

    def find(team_name):
        for sport in TEAMS:
            if team_name in sport:
                return self.Team(name=team_name, sport=sport)
                
        raise ValueError("Invalid Team Name")
