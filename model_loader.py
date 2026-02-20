import tensorflow as tf

class ModelLoader:
    def __init__(self):
        self.model_path = 'model/lstm_model.h5'

    def load_model(self):
        try:
            # Load the trained LSTM model
            model = tf.keras.models.load_model(self.model_path)
            logging.info("Model loaded successfully.")
            return model
        except Exception as e:
            logging.error(f"Failed to load model: {str(e)}")
            raise