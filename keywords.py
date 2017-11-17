import RAKE #pip install python-rake

def get_keywords(text, score_minimum = 2.0):
    Rake = RAKE.Rake(RAKE.NLTKStopList())
    keywords = Rake.run(text)

    keywords = [row for row in keywords if row[1] >= score_minimum]

    return(keywords)
