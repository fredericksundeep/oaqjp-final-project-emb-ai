"""Flask application to detect emotion from user text using Watson NLP API."""

from flask import Flask, request, render_template
import requests
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)

@app.route('/')
def index():
    """Renders the index HTML page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Endpoint to analyze user-submitted text and detect emotions.

    Returns:
        str: A formatted string showing emotion scores or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    try:
        result = emotion_detector(text_to_analyze)
        if result['dominant_emotion'] is None:
            return "Invalid text! Please try again!"

        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response_text

    except requests.exceptions.RequestException:
        return "Invalid text! Please try again!"


if __name__ == "__main__":
    app.run(debug=True)
