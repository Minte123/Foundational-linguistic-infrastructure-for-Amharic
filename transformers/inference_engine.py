from transformers import pipeline

class TransformerInferenceEngine:

    def __init__(self):

        # Multilingual transformer baseline
        self.ner_pipeline = pipeline(
            "token-classification",
            model="Davlan/xlm-roberta-base-ner-hrl",
            aggregation_strategy="simple"
        )

    def predict(self, text):

        predictions = self.ner_pipeline(text)

        return {
            "text": text,
            "predictions": predictions
        }