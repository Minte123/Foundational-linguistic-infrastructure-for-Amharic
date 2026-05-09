class ConsensusValidation:

    '''
    Validates annotations using majority agreement.
    '''

    def validate(self, annotations):

        labels = [a["label"] for a in annotations]

        winner = max(set(labels), key=labels.count)

        return winner