import unittest
from EmotionDetection import emotion_predictor

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_predictor("I am glad this happened")
        self.assertIn('joy', result['dominant_emotion'])

    def test_anger(self):
        result = emotion_predictor("I am really mad about this")
        self.assertIn('anger', result['dominant_emotion'])

    def test_disgust(self):
        result = emotion_predictor("I feel disgusted just hearing about this")
        self.assertIn('disgust', result['dominant_emotion'])

    def test_sadness(self):
        result = emotion_predictor("I am so sad about this")
        self.assertIn('sadness', result['dominant_emotion'])

    def test_fear(self):
        result = emotion_predictor("I am really afraid that this will happen")
        self.assertIn('fear', result['dominant_emotion'])
if __name__ == "__main__":
    unittest.main()
