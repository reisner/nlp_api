import spacy

# Requires: "python3 -m spacy download en"
def get_entities(text):
    return(spacy_entities(text))

def spacy_entities(text):
    nlp = spacy.load('en')

    doc = nlp(text)

    # Find named entities, phrases and concepts
    entities = []
    for entity in doc.ents:
        entities.append({
            "text": entity.text,
            "label": entity.label_,
            "start_char": entity.start_char,
            "end_char": entity.end_char
        })

    return(entities)


#TODO: Using NLTK:
#>>> entities = nltk.chunk.ne_chunk(tagged)
