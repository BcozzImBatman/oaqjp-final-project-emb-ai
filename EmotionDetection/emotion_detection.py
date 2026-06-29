import requests
import json

def emotion_detector(text_to_analyse):
    emotions = {'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None}
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputs = { "raw_document": { "text": text_to_analyse }}

    response = requests.post(url, headers=headers, json=inputs)
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
    
        emotions["anger"] = formatted_response['emotionPredictions'][0]['emotion']['anger']
        emotions["disgust"] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        emotions["fear"] = formatted_response['emotionPredictions'][0]['emotion']['fear']
        emotions["joy"] = formatted_response['emotionPredictions'][0]['emotion']['joy']
        emotions["sadness"] = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        emotions["dominant_emotion"] = dominant_emotion = max(formatted_response['emotionPredictions'][0]\
                            ['emotion'], key=formatted_response['emotionPredictions'][0]['emotion'].get)
    
    elif response.status_code == 400:
        return emotions
    
    return emotions
