import RAKE #pip install python-rake

def get_keywords(text, score_minimum = None):
    Rake = RAKE.Rake(RAKE.NLTKStopList())
    keywords = Rake.run(text)

    results = []
    for row in keywords:
        score = row[1]
        if (score_minimum is None) or (score >= score_minimum):
            results.append({ 'text': row[0], 'score': score })

    return(results)
