scores = [ 'Love', 'Fifteen', 'Thirty', 'Forty']
overtime_treshold = 4
win_treshold = 2
end_score = 4

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.name =  [player1_name, player2_name]
        self.score = [0,0]

    def won_point(self, player_name):
        self.score[self.name.index(player_name)] += 1


    def check_score(self):
        score_difference = self.score[0] - self.score[1]
        max_score = max(self.score)
        overtime = max_score >= overtime_treshold
        ended = (max_score >= end_score or overtime) and abs(score_difference) >= win_treshold
        lead = -1
        if score_difference != 0:
            lead = 0 if score_difference > 0 else 1

        return (
            score_difference,
            overtime,
            ended,
            lead,
        )

    def get_score(self):
        score_difference, overtime, ended, lead = self.check_score()
        print(overtime, ended, self.score)

        if ended:
            return "Win for " + self.name[lead]
        if overtime:
            if lead == -1:
                return "Deuce"
            return "Advantage " + self.name[lead]

        if score_difference == 0:
            return "{}-All".format(scores[self.score[0]])
        
        return "{}-{}".format(scores[self.score[0]], scores[self.score[1]])
