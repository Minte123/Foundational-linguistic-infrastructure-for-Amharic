from datasets import Dataset

class TransformerTrainer:

    '''
    Transformer training pipeline.
    '''

    def train(self, records):

        dataset = Dataset.from_list(records)

        print("Dataset size:", len(dataset))

        print("Training pipeline initialized.")