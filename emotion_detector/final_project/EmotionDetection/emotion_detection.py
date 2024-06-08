import requests
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json =  {"raw_document": { "text": text_to_analyze } }
    response = requests.post(url = url, headers=headers, json=input_json)
    if response.status_code == 400:
        return None
    return response.json()["emotionPredictions"][0]

def emotion_predictor(text_to_analyze):
    emotions = emotion_detector(text_to_analyze)
    if emotions is None:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    emotions = dict(emotions)
    d = {"anger": emotions['emotion']['anger'],
    "disgust": emotions['emotion']['disgust'],
    "fear": emotions['emotion']['fear'],
    "joy": emotions['emotion']['joy'],
    "sadness": emotions['emotion']['sadness']}
    mx = ("none", 0)
    for k,v in d.items():
        if v > mx[1]:
            mx = (k,v)
    d['dominant_emotion'] = mx[0]
    return d