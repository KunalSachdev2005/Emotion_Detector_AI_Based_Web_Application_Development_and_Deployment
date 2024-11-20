'''
Flask Application for Emotion Detection Using Watson NLP Library.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    '''Rendering the Home page.'''
    return render_template('index.html')

# Route Decorator
@app.route('/emotionDetector', methods = ['GET'])
def emotion_detector_endpoint():
    '''Endpoint for emotion detection.'''

    text_to_analyze = request.args.get("textToAnalyze", "")

    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_score'] is None:
        return "Invalid text! Please try again!", 200

    formatted_response = (
    f"For the given statement, the system response is 'anger': {emotions['anger']}, "
    f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
    f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
    f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    return formatted_response, 200

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000)
