#news reader


import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak =Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("news for today....")
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']

    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("moving on to the next news....")
speak("thanks for listing....")
