import spacy

STOPWORDS = [
    'i',
    'a',
    'about',
    'an',
    'are',
    'as',
    'at',
    'be',
    'by',
    'com',
    'for',
    'from',
    'how',
    'in',
    'is',
    'it',
    'of',
    'on',
    'or',
    'that',
    'the',
    'this',
    'to',
    'was',
    'what',
    'when',
    'where',
    'who',
    'will',
    'with',
    'the',
    "'s",
    '/',
    'do',
    'so',
    'you',
    'say',
    'thank',
    'there',
    'their',
    'do',
    'just',
    'would',
    'can',
    'should'
    'could',
    'can',
    'them',
    'need',
    'and'
]

# Parts of speech to exclude:
EXCLUDE_POS = ['SPACE', 'PUNCT']

def get_lemmas(text):
    nlp = spacy.load('en')
    doc = nlp(str(text))

    lemmas = []
    for word in doc:
        l = word.lemma_ if word.lemma_ != "-PRON-" else word.lower_
        l = l.strip()
        if (len(l) > 0 and
            l not in STOPWORDS and
            word.pos_ not in EXCLUDE_POS):
            lemmas.append(l)

    # Return unique lemmas:
    lemmas = list(set(lemmas))

    lemmas = map((lambda l: {'text': l}), lemmas)
    return(lemmas)
