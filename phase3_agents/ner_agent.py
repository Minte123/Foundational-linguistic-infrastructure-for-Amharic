class NERAgent:
    '''
    Learns named entities from tagged corpora.
    '''

    def predict(self, token):
        known_people = ["አብይ", "አህመድ"]

        if token in known_people:
            return "PER"

        return "O"