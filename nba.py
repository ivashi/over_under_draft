from nba_api.stats.static import teams
from nba_api.stats.endpoints import TeamDashboardByTeamPerformance

class Person:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def get_score(self):
        return self.score

    def add_to_score(self, value):
        self.score += value
        return self.score

    def get_name(self):
        return self.name

shreya = Person(name="Shreya")
shree = Person(name="Shree")
anuraag = Person(name="Anuraag")
brad = Person(name="Brad")
gary = Person(name="Gary")
joel = Person(name="Joel")
ishan = Person(name="Ishan")
leftovers = Person(name="Leftovers")

person_list = [shreya, shree, anuraag, brad, gary, joel, ishan]

GAMES_IN_SEASON = 82
VEGAS_OVER_UNDER_DICT = {
    'ATL': {
        'vegas_line': 45.5,
        'over': anuraag,
        'under': shreya,
    },
    'BOS': {
        'vegas_line': 53.5,
        'over': anuraag,
        'under': joel,
    },
    'CLE': {
        'vegas_line': 47.5,
        'over': brad,
        'under': gary,
    },
    'NOP': {
        'vegas_line': 44.5,
        'over': ishan,
        'under': gary,
    },
    'CHI': {
        'vegas_line': 41.5,
        'over': joel,
        'under': shree,
    },
    'DAL': {
        'vegas_line': 48.5,
        'over': anuraag,
        'under': shree,
    },
    'DEN': {
        'vegas_line': 50.5,
        'over': shreya,
        'under': brad,
    },
    'GSW': {
        'vegas_line': 51.5,
        'over': shreya,
        'under': brad,
    },
    'HOU': {
        'vegas_line': 23.5,
        'over': anuraag,
        'under': leftovers,
    },
    'LAC': {
        'vegas_line': 52.5,
        'over': ishan,
        'under': shree,
    },
    'LAL': {
        'vegas_line': 45.5,
        'over': anuraag,
        'under': gary,
    },
    'MIA': {
        'vegas_line': 48.5,
        'over': shreya,
        'under': brad,
    },
    'MIL': {
        'vegas_line': 52.5,
        'over': brad,
        'under': leftovers,
    },
    'MIN': {
        'vegas_line': 49.5,
        'over': shreya,
        'under': shree,
    },
    'BKN': {
        'vegas_line': 50.5,
        'over': anuraag,
        'under': gary,
    },
    'NYK': {
        'vegas_line': 38.5,
        'over': shreya,
        'under': anuraag,
    },
    'ORL': {
        'vegas_line': 26.5,
        'over': ishan,
        'under': shree,
    },
    'IND': {
        'vegas_line': 23.5,
        'over': gary,
        'under': ishan,
    },
    'PHI': {
        'vegas_line': 50.5,
        'over': joel,
        'under': gary,
    },
    'PHX': {
        'vegas_line': 52.5,
        'over': shree,
        'under': ishan,
    },
    'POR': {
        'vegas_line': 39.5,
        'over': brad,
        'under': shreya,
    },
    'SAC': {
        'vegas_line': 33.5,
        'over': shreya,
        'under': joel,
    },
    'SAS': {
        'vegas_line': 22.5,
        'over': gary,
        'under': joel,
    },
    'OKC': {
        'vegas_line': 23.5,
        'over': ishan,
        'under': brad,
    },
    'TOR': {
        'vegas_line': 45.5,
        'over': brad,
        'under': leftovers,
    },
    'UTA': {
        'vegas_line': 24.5,
        'over': shree,
        'under': ishan,
    },
    'MEM': {
        'vegas_line': 48.5,
        'over': joel,
        'under': anuraag,
    },
    'WAS': {
        'vegas_line': 35.5,
        'over': leftovers,
        'under': joel,
    },
    'DET': {
        'vegas_line': 29.5,
        'over': joel,
        'under': shree,
    },
    'CHA': {
        'vegas_line': 33.5,
        'over': gary,
        'under': ishan,
    },
}


teams = teams.get_teams()

for team in teams:
    try:
        team_dict = TeamDashboardByTeamPerformance(team_id=team['id']).overall_team_dashboard.get_dict()
        wins = team_dict['data'][0][3]
        losses = team_dict['data'][0][4]
        vegas_line = VEGAS_OVER_UNDER_DICT[team['abbreviation']]['vegas_line']

        if losses > 0:
            expected_wins = round(((wins * 1.0) / losses) * GAMES_IN_SEASON)
        else:
            expected_wins = GAMES_IN_SEASON
        if wins > 0:
            expected_losses = round(((losses * 1.0) / wins) * GAMES_IN_SEASON)
        else: 
            expected_losses = GAMES_IN_SEASON

        over_value_prediction = expected_wins - vegas_line
        under_value_prediction = vegas_line - expected_wins

        over_predictor = VEGAS_OVER_UNDER_DICT[team['abbreviation']]['over']
        under_predictor = VEGAS_OVER_UNDER_DICT[team['abbreviation']]['under']

        over_predictor.add_to_score(over_value_prediction)
        under_predictor.add_to_score(under_value_prediction)

        # Print out team information
        print(f"Team: {team['full_name']}")
        print(f"{wins} wins {losses} losses")
        print(f"Based on records Expected Wins: {expected_wins} Expected Losses: {expected_losses}")
        print(f"Vegas Line at: {vegas_line}")
        print(f"Estimated value of OVER: {over_value_prediction} for {over_predictor.get_name()}")
        print(f"Estimated value of UNDER: {under_value_prediction} for {under_predictor.get_name()}\n\n")
        
    except Exception:
        continue

for person in person_list:
    print(f"NAME: {person.get_name()}")
    print(f"Expected Overall Score: {person.get_score()}")
