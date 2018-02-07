import entities
import keywords
import numpy as np
import pprint
import sentiment
from textblob import TextBlob

# Given a block of text, return:
#  sentiment:
#  entities:
#  keywords:
def analyze_text_block(text,
                       sentiment_library = "textblob",
                       entity_library = "spacy",
                       get_sentiment_per_topic = True):
    entities_res = entities.get_entities(text, library = entity_library)
    keywords_res = keywords.get_keywords(text)
    sentiment_res = sentiment.get_sentiment(text, library = sentiment_library)

    # Calculate sentiment per keywords and entities, by averaging the sentiment
    # for all the sentences that they appear in:
    if get_sentiment_per_topic:
        blob = TextBlob(text)
        for sentence in blob.sentences:
            polarity = sentiment.get_sentiment(str(sentence), library = sentiment_library)['sentiment.score']
            for keyword in keywords_res:
                word = keyword['text']
                if word.lower() in sentence.lower().replace("\n", ' '):
                    if 'sentiment.score' not in keyword.keys():
                        keyword['sentiment.score'] = []
                    keyword['sentiment.score'].append(polarity)

            for entity in entities_res:
                word = entity['text']
                if word.lower() in sentence.lower():
                    if 'sentiment.score' not in entity.keys():
                        entity['sentiment.score'] = []
                    entity['sentiment.score'].append(polarity)

        for keyword in keywords_res:
            keyword['num.sentences'] = len(keyword['sentiment.score'])
            keyword['sentiment.score'] = np.mean(keyword['sentiment.score'])

        for entity in entities_res:
            entity['num.sentences'] = len(entity['sentiment.score'])
            entity['sentiment.score'] = np.mean(entity['sentiment.score'])

    results = {
      'entities': entities_res,
      'sentiment': sentiment_res,
      'keywords': keywords_res
    }

    return(results)
