from textblob import TextBlob

def get_sentiment(text):
    analysis = TextBlob(text)

    return(analysis.sentiment)
