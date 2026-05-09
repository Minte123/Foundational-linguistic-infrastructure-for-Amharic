class ConsensusAgent:

    '''
    Multi-agent consensus voting.
    '''

    def vote(self, predictions):

        votes = {}

        for prediction in predictions:

            label = prediction["label"]

            votes[label] = votes.get(label, 0) + 1

        best = max(votes, key=votes.get)

        return {
            "consensus": best,
            "votes": votes
        }