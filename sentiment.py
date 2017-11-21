from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer #pip install vaderSentiment

# Returns a hash, that differs based on the library, but is guaranteed to return
# a value for the key "polarity". This ranges from -1 (negative) to 1 (positive).
def get_sentiment(text, library = "textblob"):
    if library == 'textblob':
        return(get_textblob_sentiment(text))
    elif library == 'vader':
        return(get_vader_sentiment(text))
    else:
        return({'sentiment error': 'Invalid sentiment library'})

def get_textblob_sentiment(text):
    analysis = TextBlob(text)
    # from textblob.sentiments import NaiveBayesAnalyzer
    # blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())
    sentiment = analysis.sentiment
    return({ 'polarity': sentiment.polarity, 'subjectivity': sentiment.subjectivity })

# The compound score is computed by summing the valence scores of each word in
# the lexicon, adjusted according to the rules, and then normalized to be between
# -1 (most extreme negative) and +1 (most extreme positive).
def get_vader_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(text)
    result['polarity'] = result['compound']

    return(result)
