import RAKE #pip install python-rake

def get_keywords(text, score_minimum = 2.0):
    Rake = RAKE.Rake(RAKE.NLTKStopList())
    keywords = Rake.run(text)

    results = []
    for row in keywords:
        score = row[1]
        if score >= score_minimum:
            results.append({ 'text': row[0], 'score': score })

    return(results)
