from textblob import TextBlob

def get_sentiment(text):
    analysis = TextBlob(text)
    # from textblob.sentiments import NaiveBayesAnalyzer
    # blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())

    return(analysis.sentiment)
