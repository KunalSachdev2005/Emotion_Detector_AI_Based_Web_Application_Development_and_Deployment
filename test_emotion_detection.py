import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    # Testing Joy sentiment
    def test_joy_sentiment(self):
        emotions = emotion_detector("I am glad this happened")
        self.assertEqual(emotions['dominant_emotion'], "joy")
    
    # Testing Anger sentiment
    def test_anger_sentiment(self):
        emotions = emotion_detector("I am really mad about this")
        self.assertEqual(emotions['dominant_emotion'], "anger")
    
    # Testing Disgust sentiment
    def test_disgust_sentiment(self):
        emotions = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotions['dominant_emotion'], "disgust")
    
    # Testing Sadness sentiment
    def test_sadness_sentiment(self):
        emotions = emotion_detector("I am so sad about this")
        self.assertEqual(emotions['dominant_emotion'], "sadness")
    
    # Testing Fear sentiment
    def test_fear_sentiment(self):
        emotions = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotions['dominant_emotion'], "fear")
    
unittest.main() # Run all test cases defined in the module
