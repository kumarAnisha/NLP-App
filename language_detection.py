import nlpcloud
def detect_language(text):
    client = nlpcloud.Client("python-langdetect", "8335bc69204251395e3007fd8d49a4d1ca439666", gpu=False)
    response=client.langdetection(text)
    print(response)
    result=""
    for i in response['languages']:
        for key,value in i.items():
           
         result+=key + " score: " + str(value) + '\n'
    return result