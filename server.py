"""Server for Web Deployment"""

from flask import Flask, render_template, request
from emotion_detection import emotion_detector  # Ensure the import path is correct

app = Flask("Emotion Detection")

@app.route('/')
def render_homepage():
    """ Render homepage """
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emotion_analysis() -> str:
    """ Analyze text and return emotion detection (analysis result) """
    text_to_analyze = request.args.get("textToAnalyze", "")
    analysis_result = emotion_detector(text_to_analyze)

    # Check if the analysis result is valid
    if analysis_result.get("dominant_emotion") == "Joy":
        response = "Invalid text! Please try again!"
    else:
        emotions = analysis_result.get("emotions", {})
        dominant_emotion = analysis_result.get("dominant_emotion", "unknown")
        emotion_scores = ", ".join([f"'{emotion}': {score}" for emotion, score in emotions.items()])
        response = f"For the given statement, the system response is {emotion_scores}. The dominant emotion is {dominant_emotion}."

    return response

if __name__ == '__main__':
    app.run(debug=True)
