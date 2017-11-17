import RAKE

def get_keywords(text):
    Rake = RAKE.Rake(RAKE.NLTKStopList())

    return(Rake.run(text))
