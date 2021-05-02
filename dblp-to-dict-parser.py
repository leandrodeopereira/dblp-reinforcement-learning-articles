import collections
import xmltodict
import re
import codecs
import numpy as np
import time
start_time = time.time()

xmlfile = codecs.open('dblp-2021-01-02.xml', 'r', 'ISO-8859-1').read()

doc = xmltodict.parse(xmlfile)

dic = dict()
for article in doc['dblp']['article']:
    try:
        # In some cases the title can be a dictionary, just convert to string.
        title = str(article['title'])
        if (re.search('reinforcement learning', title, re.IGNORECASE) 
            or re.search('reinforcement-learning', title, re.IGNORECASE)):
            authors = []
            if isinstance(article['author'], str):
                authors.append(article['author'])
            elif isinstance(article['author'], dict):
                authors.append(article['author']["#text"])
            elif isinstance(article['author'], list):
                for author in article['author']:
                    if isinstance(author, str):
                        authors.append(author)
                    elif isinstance(author, dict):
                        authors.append(author["#text"])
            else:
                authors.append(article['author'])

            if not article['year'] in dic:
                dic[article['year']] = []
            dic[article['year']] = [{ 'title': title, 'authors': authors  }] + dic[article['year']]
    except KeyError:
        print('Error on article:')
        print(article)
print("--- %s seconds ---" % (time.time() - start_time))

read_dict_sorted = collections.OrderedDict(sorted(dic.items()))
np.save('result-correct-title.npy', read_dict_sorted)
