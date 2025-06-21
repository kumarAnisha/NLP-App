import nlpcloud
def perform_ner_final(text):
    client = nlpcloud.Client("t5-base-en-generate-headline", "8335bc69204251395e3007fd8d49a4d1ca439666", gpu=False)
    result=client.summarization(text)

    
   
    return result['summary_text']