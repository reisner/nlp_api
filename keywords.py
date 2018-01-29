import RAKE #pip install python-rake
import textrank #pip install git+git://github.com/davidadamojr/TextRank.git

def get_keywords(text, library = "textrank"):
    if library == 'RAKE':
        return(get_rake_keywords(text))
    elif library == 'textrank':
        return(get_textrank_keywords(text))
    else:
        return({'keywords error': 'Invalid keywords library'})

def get_rake_keywords(text, score_minimum = None):
    results = []
    Rake = RAKE.Rake(RAKE.NLTKStopList())
    keywords = Rake.run(text)

    results = []
    for row in keywords:
        score = row[1]
        if (score_minimum is None) or (score >= score_minimum):
            results.append({ 'text': row[0], 'score': score })

    return(results)

def get_textrank_keywords(text):
    results = []
    keywords = textrank.extract_key_phrases(text)

    for word in keywords:
        results.append({ 'text': word, 'score': 0 })

    return(results)
