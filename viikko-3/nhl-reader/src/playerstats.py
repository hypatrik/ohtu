from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.players = [Player(**p) for p in reader.fetch()]

    
    def top_scorers_by_nationality (self, nationality):
        return filter(lambda p: p.nationality == "FIN", self.players)
