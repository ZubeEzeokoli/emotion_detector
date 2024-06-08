'''
My code
'''
from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_predictor

app = Flask(__name__)

@app.route("/emotionDetector", methods=['GET'])
def emotion_detector():
    """
    Analyze the emotion of the given text and return the result as JSON.

    Returns:
        str: JSON response containing the emotion analysis result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_predictor(text_to_analyze)

    response_text = "For the given statement, the system response is "
    for emotion, value in result.items():
        response_text += f"'{emotion}': {value}, "

    dom_emo = result['dominant_emotion']
    if result['dominant_emotion'] is None:
        dom_emo = "Invalid text! Please try again!"

    response_text += f"and the dominant emotion is {dom_emo}."

    return jsonify(response_text=response_text)

@app.route("/")
def render_index_page():
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5500)
