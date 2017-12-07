# NLP API #

This project provides an API to a variety of NLP libraries, in a standard format. Returns document sentiment, keywords, and entities. Can return sentiment per keyword and per entity.

Also can be used to set up your own text analysis API server.

### Usage ###

Some input:

    text = """
    Edmonton is the capital city of the Canadian province of Alberta. Edmonton is on the North Saskatchewan River and
    is the centre of the Edmonton Metropolitan Region, which is surrounded by Alberta's central region. The city anchors
    the north end of what Statistics Canada defines as the "Calgary–Edmonton Corridor".

    The city had a population of 932,546 in 2016, making it Alberta's second-largest city and Canada's fifth-largest
    municipality. Also in 2016, Edmonton had a metropolitan population of 1,321,426, making it the sixth-largest census
    metropolitan area (CMA) in Canada. Edmonton is North America's northernmost city with a metropolitan population over
    one million. A resident of Edmonton is known as an Edmontonian.

    Edmonton's historic growth has been facilitated through the absorption of five adjacent urban municipalities
    (Strathcona, North Edmonton, West Edmonton, Beverly and Jasper Place) and a series of annexations ending in 1982.
    Known as the "Gateway to the North", the city is a staging point for large-scale oil sands projects occurring in
    northern Alberta and large-scale diamond mining operations in the Northwest Territories.

    Edmonton is a cultural, governmental and educational centre. It hosts a year-round slate of festivals, reflected in
    the nickname "Canada's Festival City". It is home to North America's largest mall, West Edmonton Mall (the world's
    largest mall from 1981 until 2004), and Fort Edmonton Park, Canada's largest living history museum
    """

Using the code:

    import analyze_text as at
    result = at.analyze_text_block(text)
    import pprint
    pprint.pprint(result)

You can also specify which libraries to use:

    result = at.analyze_text_block(text, sentiment_library = "vader", entity_library = "textblob")

### Flask REST Server ###

Run the flask server:

    nohup python rest_server.py >/dev/null 2>&1 &

Query the server (from python):

    from requests import put
    host_url = 'host.url.com/analyze_text'
    put(host_url, data={'text': text}).json()

Query the server (from the command line):

    curl -X PUT -d text="hello there i am some text to analyze in Canada. Boy oh boy am I angry." host.url.com/analyze_text
