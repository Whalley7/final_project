# final_project/emotion_detection.py

import requests

def emotion_detector(text_to_analyze):
    """
    Calls Watson NLP EmotionPredict and returns the original text.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return text_to_analyze
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None