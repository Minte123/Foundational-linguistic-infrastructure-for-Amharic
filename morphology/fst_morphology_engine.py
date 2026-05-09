class FSTMorphologyEngine:

    '''
    Finite State inspired morphology decomposition.

    Real systems would use:
    - finite state transducers
    - lexicon graphs
    - root-pattern mapping
    '''

    PREFIXES = ["እ", "ል", "በ", "ላ"]
    SUFFIXES = ["ሁ", "ሽ", "ቸው", "ልሁ"]

    def analyze(self, word):

        detected_prefixes = []
        detected_suffixes = []

        for prefix in self.PREFIXES:

            if word.startswith(prefix):
                detected_prefixes.append(prefix)

        for suffix in self.SUFFIXES:

            if word.endswith(suffix):
                detected_suffixes.append(suffix)

        return {
            "word": word,
            "prefixes": detected_prefixes,
            "suffixes": detected_suffixes
        }