from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')  # <-- Fixed here
    if not text_to_analyze:
        return "Error: No text provided", 400
    try:
        result = emotion_detector(text_to_analyze)
        if result:
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
        else:
            return "Could not analyze the text. Try again!"
    except Exception as e:
        return f"Error processing the request: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
