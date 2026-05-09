class RewardEngine:

    def __init__(self):

        self.points = {}

    def reward(self, username, amount=5):

        self.points[username] = (
            self.points.get(username, 0) + amount
        )

        return self.points[username]