# Import mrjob, mrstep and regular expressions modules
from mrjob.job import MRJOb
from mrstep.step import MRStep
import re

# Compiles regular expression pattern into a reusable regular expression object
WORD_RE     = re.compile(r"[\w']+")

class invertedIndex(MRJOb):
    def steps(self):
        return [MRStep(mapper = self.map_word_index, reducer = self.reduce_word_index_list)]
    
    # Mapper takes in a key, which in this case is NONE, and a value, which is a line of words
    def map_word_index(self, _, line):
        key, line = line.split(" ", 1) # Splits line into words and attaches an index (line) number next to the word
        for word in WORD_RE.findall(line):
            if word.lower() and not word.isdigit(): # ONly proceeds once lowercase word has been validated that it is not a number
               yield(word.lower(), key)  # Returns lowercase word and the index (line) number

    # Reducer takes in the key, which is a word, and a value, which is the index (line) number
    def reduce_word_index_list(self, word, indexNumbers):
        indexNumbersList = list(indexNumbers) # Creates a list of the index numbers
        yield(word.lower(), indexNumbersList)

if __name__ == '__main__':
    invertedIndex.run()

