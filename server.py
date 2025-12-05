"""
server.py
Flask application for Emotion Detection.
Provides a web interface and API endpoint to analyze text
and return detected emotions using the EmotionDetection package.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """Process input text and return emotion detection results."""
    text = request.args.get('textToAnalyze', '')
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    return (
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}, "
        f"'dominant_emotion': '{result['dominant_emotion']}'"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
