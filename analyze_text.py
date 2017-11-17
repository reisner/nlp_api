import entities
import keywords
import sentiment

# Given a block of text, return:
#  sentiment:
#  entities:
#  keywords:
def analyze_text_block(text):
    results = {
      'entities': entities.get_entities(text),
      'sentiment': sentiment.get_sentiment(text),
      'keywords': keywords.get_keywords(text)
    }

    return(results)


# Example Run:
result = analyze_text_block("""
Edmonton is the capital city of the Canadian province of Alberta. Edmonton is on the North Saskatchewan River and is the centre of the Edmonton Metropolitan Region, which is surrounded by Alberta's central region. The city anchors the north end of what Statistics Canada defines as the "Calgary–Edmonton Corridor".[12]

The city had a population of 932,546 in 2016, making it Alberta's second-largest city and Canada's fifth-largest municipality.[5] Also in 2016, Edmonton had a metropolitan population of 1,321,426, making it the sixth-largest census metropolitan area (CMA) in Canada.[7] Edmonton is North America's northernmost city with a metropolitan population over one million. A resident of Edmonton is known as an Edmontonian.[13]

Edmonton's historic growth has been facilitated through the absorption of five adjacent urban municipalities (Strathcona, North Edmonton, West Edmonton, Beverly and Jasper Place)[14] and a series of annexations ending in 1982.[15] Known as the "Gateway to the North",[16] the city is a staging point for large-scale oil sands projects occurring in northern Alberta and large-scale diamond mining operations in the Northwest Territories.[17]

Edmonton is a cultural, governmental and educational centre. It hosts a year-round slate of festivals, reflected in the nickname "Canada's Festival City".[1] It is home to North America's largest mall, West Edmonton Mall (the world's largest mall from 1981 until 2004),[18] and Fort Edmonton Park, Canada's largest living history museum
""")

print(result)
