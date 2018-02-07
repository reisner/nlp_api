import entities
import keywords
import lemmas
import numpy as np
import pprint
import sentiment
from textblob import TextBlob

# Given a block of text, return:
#  sentiment:
#  entities:
#  keywords:
#  lemmas:
def analyze_text_block(text,
                       sentiment_library = "textblob",
                       entity_library = "spacy",
                       get_sentiment_per_topic = True):
    entities_res = entities.get_entities(text, library = entity_library)
    keywords_res = keywords.get_keywords(text)
    sentiment_res = sentiment.get_sentiment(text, library = sentiment_library)
    lemmas_dict = {}

    # Calculate sentiment per lemmas, keywords and entities, by averaging
    # the sentiment for all the sentences that they appear in:
    if get_sentiment_per_topic:
        blob = TextBlob(text)
        for sentence in blob.sentences:
            sentence_score = sentiment.get_sentiment(str(sentence), library = sentiment_library)['sentiment.score']

            sentence_lemmas = lemmas.get_lemmas(sentence)

            sentence = sentence.lower().replace("\n", ' ')
            for lemma in sentence_lemmas:
                lemmatxt = lemma['text']
                if lemmatxt in lemmas_dict.keys():
                    lemmas_dict[lemmatxt]['sentiment.score'].append(sentence_score)
                else:
                    lemmas_dict[lemmatxt] = { 'sentiment.score': [sentence_score] }

            for keyword in keywords_res:
                word = keyword['text']
                if word.lower() in sentence:
                    if 'sentiment.score' not in keyword.keys(): keyword['sentiment.score'] = []
                    keyword['sentiment.score'].append(sentence_score)

            for entity in entities_res:
                word = entity['text']
                if word.lower() in sentence:
                    if 'sentiment.score' not in entity.keys(): entity['sentiment.score'] = []
                    entity['sentiment.score'].append(sentence_score)

        for keyword in keywords_res:
            keyword['num.sentences'] = len(keyword['sentiment.score'])
            keyword['sentiment.score'] = np.mean(keyword['sentiment.score'])

        for entity in entities_res:
            entity['num.sentences'] = len(entity['sentiment.score'])
            entity['sentiment.score'] = np.mean(entity['sentiment.score'])

        lemmas_res = []
        for lemma in lemmas_dict.keys():
            scores = lemmas_dict[lemma]['sentiment.score']
            lemmas_res.append({ 'text': lemma,
                                'num.sentences': len(scores),
                                'sentiment.score': np.mean(scores) })
    else:
        lemmas_res = lemmas.get_lemmas(text)

    results = {
      'entities': entities_res,
      'sentiment': sentiment_res,
      'keywords': keywords_res,
      'lemmas': lemmas_res
    }

    return(results)
