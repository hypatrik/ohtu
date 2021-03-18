class Player:
    def __init__(
        self,
        name,
        nationality,
        assists,
        goals,
        penalties,
        team,
        games,
    ):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return "{} team {} goals {} assists {}".format(
            self.name,
            self.team,
            self.goals,
            self.assists,
        )
