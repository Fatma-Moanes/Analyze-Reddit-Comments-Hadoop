#!/usr/bin/python3
import sys
import json
import re
import nltk
from collections import Counter

nltk.download('stopwords')
nltk.download("wordnet")
from nltk.corpus import stopwords
from nltk.corpus import wordnet

stopwords_dict = Counter(stopwords.words('english'))
regex = r"\(?(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})\)?|[^a-z ]"
nouns = {x.name().split('.', 1)[0] for x in wordnet.all_synsets('n')}

for line in sys.stdin:
    comment = json.loads(line)
    body = comment['body']

    # Lowercase
    body = body.lower()

    body = re.sub(regex, "", body)

    # Remove Stopwords
    for word in body.split(' '):
        if word not in stopwords_dict and word in nouns:
            print(word)
