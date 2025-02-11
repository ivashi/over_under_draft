from datetime import date
from nba_api.stats.static import teams


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


def person_sort(person_list):
    return sorted(person_list, key=lambda x: x.score, reverse=True)


shreya = Person(name="Shreya")
joel = Person(name="Joel")
ishan = Person(name="Ishan")
kevin = Person(name="Kevin")
malcolm = Person(name="Malcolm")
evan = Person(name="Evan")
sam = Person(name="Sam")
fardhi = Person(name="Fardhi")
leftovers = Person(name="Leftovers")

person_list = [
    shreya,
    joel,
    ishan,
    kevin,
    malcolm,
    evan,
    sam,
    fardhi,
    leftovers,
]
GAMES_IN_SEASON = 82
VEGAS_OVER_UNDER_DICT = {
    'ATL': {
        'wins': 25,
        'losses': 28,
        'vegas_line': 36.5,
        'over': shreya,
        'under': leftovers,
    },
    'BOS': {
        'wins': 37,
        'losses': 16,
        'vegas_line': 58.5,
        'over': kevin,
        'under': malcolm,
    },
    'CLE': {
        'wins': 42,
        'losses': 10,
        'vegas_line': 48.5,
        'over': shreya,
        'under': fardhi,
    },
    'NOP': {
        'wins': 12,
        'losses': 40,
        'vegas_line': 45.5,
        'over': sam,
        'under': leftovers,
    },
    'CHI': {
        'wins': 22,
        'losses': 31,
        'vegas_line': 28.5,
        'over': sam,
        'under': fardhi,
    },
    'DAL': {
        'wins': 28,
        'losses': 25,
        'vegas_line': 49.5,
        'over': malcolm,
        'under': kevin,
    },
    'DEN': {
        'wins': 34,
        'losses': 19,
        'vegas_line': 50.5,
        'over': joel,
        'under': malcolm,
    },
    'GSW': {
        'wins': 26,
        'losses': 26,
        'vegas_line': 43.5,
        'over': joel,
        'under': evan,
    },
    'HOU': {
        'wins': 33,
        'losses': 20,
        'vegas_line': 42.5,
        'over': evan,
        'under': leftovers,
    },
    'LAC': {
        'wins': 29,
        'losses': 23,
        'vegas_line': 35.5,
        'over': fardhi,
        'under': joel,
    },
    'LAL': {
        'wins': 31,
        'losses': 19,
        'vegas_line': 43.5,
        'over': ishan,
        'under': fardhi,
    },
    'MIA': {
        'wins': 25,
        'losses': 25,
        'vegas_line': 43.5,
        'over': shreya,
        'under': ishan,
    },
    'MIL': {
        'wins': 28,
        'losses': 23,
        'vegas_line': 49.5,
        'over': malcolm,
        'under': joel,
    },
    'MIN': {
        'wins': 30,
        'losses': 23,
        'vegas_line': 51.5,
        'over': kevin,
        'under': malcolm,
    },
    'BKN': {
        'wins': 18,
        'losses': 34,
        'vegas_line': 19.5,
        'over': leftovers,
        'under': kevin,
    },
    'NYK': {
        'wins': 34,
        'losses': 18,
        'vegas_line': 53.5,
        'over': kevin,
        'under': shreya,
    },
    'ORL': {
        'wins': 26,
        'losses': 28,
        'vegas_line': 47.5,
        'over': evan,
        'under': fardhi,
    },
    'IND': {
        'wins': 29,
        'losses': 22,
        'vegas_line': 46.5,
        'over': sam,
        'under': ishan,
    },
    'PHI': {
        'wins': 20,
        'losses': 32,
        'vegas_line': 49.5,
        'over': shreya,
        'under': malcolm,
    },
    'PHX': {
        'wins': 26,
        'losses': 26,
        'vegas_line': 48.5,
        'over': evan,
        'under': ishan,
    },
    'POR': {
        'wins': 23,
        'losses': 30,
        'vegas_line': 20.5,
        'over': joel,
        'under': kevin,
    },
    'SAC': {
        'wins': 26,
        'losses': 26,
        'vegas_line': 46.5,
        'over': joel,
        'under': malcolm,
    },
    'SAS': {
        'wins': 22,
        'losses': 28,
        'vegas_line': 35.5,
        'over': sam,
        'under': fardhi,
    },
    'OKC': {
        'wins': 42,
        'losses': 9,
        'vegas_line': 57.5,
        'over': ishan,
        'under': joel,
    },
    'TOR': {
        'wins': 16,
        'losses': 37,
        'vegas_line': 28.5,
        'over': kevin,
        'under': evan,
    },
    'UTA': {
        'wins': 12,
        'losses': 39,
        'vegas_line': 27.5,
        'over': sam,
        'under': shreya,
    },
    'MEM': {
        'wins': 35,
        'losses': 17,
        'vegas_line': 46.5,
        'over': sam,
        'under': ishan,
    },
    'WAS': {
        'wins': 9,
        'losses': 43,
        'vegas_line': 19.5,
        'over': fardhi,
        'under': evan,
    },
    'DET': {
        'wins': 27,
        'losses': 26,
        'vegas_line': 26.5,
        'over': ishan,
        'under': evan,
    },
    'CHA': {
        'wins': 13,
        'losses': 37,
        'vegas_line': 30.5,
        'over': sam,
        'under': shreya,
    },
}


nba_teams = teams.get_teams()

for team in VEGAS_OVER_UNDER_DICT.keys():
    try:
        print(f"Getting data for {team}")
        vegas_line = VEGAS_OVER_UNDER_DICT[team]['vegas_line']
        wins = VEGAS_OVER_UNDER_DICT[team]['wins']
        losses = VEGAS_OVER_UNDER_DICT[team]['losses']
        expected_wins = round(GAMES_IN_SEASON * (wins / (wins + losses)))
        print(f"Expected Wins: {expected_wins}")

        over_value_prediction = expected_wins - vegas_line
        under_value_prediction = vegas_line - expected_wins

        print(f"OVER VALUE PREDICTION {team}: {over_value_prediction}")
        print(f"UNDER VALUE PREDICTION {team}: {under_value_prediction}")
        over_predictor = VEGAS_OVER_UNDER_DICT[team]['over']
        under_predictor = VEGAS_OVER_UNDER_DICT[team]['under']

        over_predictor.add_to_score(over_value_prediction)
        under_predictor.add_to_score(under_value_prediction)

        # Print out team information
        print(f"{wins} wins {losses} losses")
        print(f"Expected Wins: {expected_wins}")
        print(f"Vegas Line at: {vegas_line}")
        print(f"Value of OVER: {over_value_prediction} for "
              f"{over_predictor.get_name()}")
        print(f"Value of UNDER: {under_value_prediction} for "
              f"{under_predictor.get_name()}\n\n")

    except Exception as e:
        print(e)
        continue

person_list = person_sort(person_list)  

print(f"STANDINGS AS OF {date.today()}")
place = 0
for person in person_list:
    place += 1
    print(f"{place}. {person.get_name()}")
    print(f"Expected Overall Score: {person.get_score()}")
