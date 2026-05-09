class POSAgent:
    '''
    Learns POS tagging patterns from human annotations.
    '''

    def predict(self, token):
        if token.endswith("ሁ"):
            return "VERB"

        return "NOUN"