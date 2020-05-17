#!/usr/bin/python
# Run this code first, then run MrsTopKQuery.py
# To run this code: python3 MrsWordCount.py small.txt output
import mrs
import string
import re
import os

PATH 	   = os.path.dirname(os.path.abspath(__file__))
STOP_WORDS = os.path.join(PATH, 'stopWords.txt')
WORD_RE    = re.compile(r"[\w']+")

class WordCount(mrs.MapReduce):
    def map(self, line_num, line_text):
        for word in WORD_RE.findall(line_text):
            word = word.strip(string.punctuation).lower()
            if word.lower() not in STOP_WORDS:
                if word:
                    yield (word, 1)

    def reduce(self, word, counts):
        yield sum(counts)

if __name__ == '__main__':
    mrs.main(WordCount)

# vim: et sw=4 sts=4