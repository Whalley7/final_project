from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    # get text from the form (Frontend sends it as query parameter 'textToAnalyze')
    text_to_analyze = request.args.get("textToAnalyze", "")

    # call your emotion detector function
    result = emotion_detector(text_to_analyze)

    # if the service returns None (e.g., empty input), handle gracefully
    if result is None:
        return "Invalid input! Please enter a valid text to analyze."

    # format the output exactly as the instructions want
    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
