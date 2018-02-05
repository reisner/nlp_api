#!/bin/bash

pip install -r requirements.txt
pip install git+git://github.com/davidadamojr/TextRank.git

python -m spacy download en
python -m nltk.downloader punkt
python -m nltk.downloader averaged_perceptron_tagger

echo "RUNNING TEST:"
python test.py
