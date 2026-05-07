"""
Unit tests for the emotion_detector function.
"""

import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


def mock_response(scores):
    """Create a mock requests response for Watson NLP."""
    mock = MagicMock()
    mock.status_code = 200
    mock.text = (
        '{"emotionPredictions": [{"emotion": {'
        '"anger": ' + str(scores.get('anger', 0.001)) + ', '
        '"disgust": ' + str(scores.get('disgust', 0.001)) + ', '
        '"fear": ' + str(scores.get('fear', 0.001)) + ', '
        '"joy": ' + str(scores.get('joy', 0.001)) + ', '
        '"sadness": ' + str(scores.get('sadness', 0.001)) + '}'
        '}]}'
    )
    return mock


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for emotion_detector function."""

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy_emotion(self, mock_post):
        """Test that joy is the dominant emotion for a joyful statement."""
        mock_post.return_value = mock_response({
            'anger': 0.006, 'disgust': 0.002, 'fear': 0.009,
            'joy': 0.986, 'sadness': 0.001
        })
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger_emotion(self, mock_post):
        """Test that anger is the dominant emotion for an angry statement."""
        mock_post.return_value = mock_response({
            'anger': 0.902, 'disgust': 0.065, 'fear': 0.011,
            'joy': 0.002, 'sadness': 0.020
        })
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust_emotion(self, mock_post):
        """Test that disgust is the dominant emotion for a disgusting statement."""
        mock_post.return_value = mock_response({
            'anger': 0.050, 'disgust': 0.850, 'fear': 0.020,
            'joy': 0.010, 'sadness': 0.070
        })
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness_emotion(self, mock_post):
        """Test that sadness is the dominant emotion for a sad statement."""
        mock_post.return_value = mock_response({
            'anger': 0.010, 'disgust': 0.005, 'fear': 0.020,
            'joy': 0.015, 'sadness': 0.950
        })
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear_emotion(self, mock_post):
        """Test that fear is the dominant emotion for a fearful statement."""
        mock_post.return_value = mock_response({
            'anger': 0.030, 'disgust': 0.010, 'fear': 0.880,
            'joy': 0.005, 'sadness': 0.075
        })
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input(self):
        """Test that blank input returns None for all values."""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['joy'])


if __name__ == '__main__':
    unittest.main()
