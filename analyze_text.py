import entities
import keywords
import pprint
import sentiment

# Given a block of text, return:
#  sentiment:
#  entities:
#  keywords:
def analyze_text_block(text):
    results = {
      'entities': entities.get_entities(text),
      'sentiment': sentiment.get_sentiment(text),
      'keywords': keywords.get_keywords(text)
    }

    return(results)

    # TODO: sentiment per keyword, and sentiment per entity.
