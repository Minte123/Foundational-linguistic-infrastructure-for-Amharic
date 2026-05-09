class MorphologyAgent:
    '''
    Morphological decomposition agent.
    '''

    def analyze(self, word):
        return {
            "word": word,
            "root_guess": word[:2],
            "suffix_guess": word[2:]
        }


if __name__ == "__main__":
    agent = MorphologyAgent()

    result = agent.analyze("እበላለሁ")

    print(result)