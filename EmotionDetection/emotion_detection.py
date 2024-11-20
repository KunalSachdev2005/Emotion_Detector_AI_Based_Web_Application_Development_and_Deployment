import requests
import json

def emotion_detector(text_to_analyze):

    if not text_to_analyze.strip():  # blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_score': None
        }

    # URL & Headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON Payload
    input_json = { 
        "raw_document": { "text": text_to_analyze }
    }
    
    # Sending request to Watson API
    response = requests.post(url, headers = headers, json = input_json)

    if response.status_code == 200:

        response_dict = response.json() # Converting response from json to Python dict

        emotions_dict = response_dict['emotionPredictions'][0]['emotion']

        anger_score = emotions_dict.get("anger", 0)
        disgust_score = emotions_dict.get("disgust", 0)
        fear_score = emotions_dict.get("fear", 0)
        joy_score = emotions_dict.get("joy", 0)
        sadness_score = emotions_dict.get("sadness", 0)

        emotions = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }

        dominant_emotion = max(emotions, key = emotions.get) # find key (emotion) with highest score

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    else:
        # Handle errors if the request fails
        return f"Error: Unable to process text. Status code: {response.status_code}"
        