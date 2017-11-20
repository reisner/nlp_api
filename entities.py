import spacy
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

# Returns a list of hashes. The hashes may differ, but are guaranteed to contain
# the key "text" for each entity.
def get_entities(text, library = "spacy"):
    if library == 'spacy':
        return(get_spacy_entities(text))
    elif library == 'textblob':
        return(get_textblob_entities(text))
    else:
        return({'entities error': 'Invalid entities library'})

# REQUIRES:
# python3 -m spacy download en
def get_spacy_entities(text):
    nlp = spacy.load('en')

    doc = nlp(text)

    # Find named entities, phrases and concepts
    entities = []
    for entity in doc.ents:
        if entity.text.strip() != '':
            entities.append({
                "text": entity.text,
                "label": entity.label_,
                "start_char": entity.start_char,
                "end_char": entity.end_char
            })

    return(entities)

# REQUIRES:
# import nltk
# nltk.download('punkt')
# nltk.download('conll2000')
def get_textblob_entities(text):
    extractor = ConllExtractor()
    blob = TextBlob(text, np_extractor=extractor)
    entities = []
    for entity in blob.noun_phrases:
        entities.append({'text': entity})
    return(entities)


#TODO: Using NLTK:
# import nltk
# nltk.download('maxent_ne_chunker')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('words')
# nltk.download('maxent_ne_chunker')
# res = nltk.chunk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text)))
