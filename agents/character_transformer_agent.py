class CharacterTransformerAgent:

    '''
    Character-aware learning.

    Important for:
    - morphology
    - affixes
    - Semitic structures
    '''

    def tokenize_characters(self, word):

        return list(word)