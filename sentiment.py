import nlpcloud
def detect_sentiment(text):
    client = nlpcloud.Client("finetuned-llama-3-70b", "8335bc69204251395e3007fd8d49a4d1ca439666", gpu=True)
    response=client.sentiment(text,target="NLP Cloud")
    print(response)
   
    return response['scored_labels'][0]['label'] + " score: " +str(response['scored_labels'][0]['score'])