import entities
import keywords
import pprint
import sentiment

# Given a block of text, return:
#  sentiment:
#  entities:
#  keywords:
def analyze_text_block(text, sentiment_library="textblob", entity_library="spacy"):
    results = {
      'entities': entities.get_entities(text, library = entity_library),
      'sentiment': sentiment.get_sentiment(text, library = sentiment_library),
      'keywords': keywords.get_keywords(text)
    }

    return(results)

    # TODO: sentiment per keyword, and sentiment per entity.
