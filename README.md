# README #

Basic NLP analysis using a variety of libraries. Returns Document sentiment, keywords, and entities.

### Usage ###

    text = """
    Edmonton is the capital city of the Canadian province of Alberta. Edmonton is on the North Saskatchewan River and is the centre of the Edmonton Metropolitan Region, which is surrounded by Alberta's central region. The city anchors the north end of what Statistics Canada defines as the "Calgary–Edmonton Corridor".

    The city had a population of 932,546 in 2016, making it Alberta's second-largest city and Canada's fifth-largest municipality. Also in 2016, Edmonton had a metropolitan population of 1,321,426, making it the sixth-largest census metropolitan area (CMA) in Canada. Edmonton is North America's northernmost city with a metropolitan population over one million. A resident of Edmonton is known as an Edmontonian.

    Edmonton's historic growth has been facilitated through the absorption of five adjacent urban municipalities (Strathcona, North Edmonton, West Edmonton, Beverly and Jasper Place) and a series of annexations ending in 1982. Known as the "Gateway to the North", the city is a staging point for large-scale oil sands projects occurring in northern Alberta and large-scale diamond mining operations in the Northwest Territories.

    Edmonton is a cultural, governmental and educational centre. It hosts a year-round slate of festivals, reflected in the nickname "Canada's Festival City". It is home to North America's largest mall, West Edmonton Mall (the world's largest mall from 1981 until 2004), and Fort Edmonton Park, Canada's largest living history museum
    """

    result = analyze_text_block(text)
    pprint.pprint(result)
