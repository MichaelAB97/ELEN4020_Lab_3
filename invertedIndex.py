# Import mrjob, mrstep and regular expressions modules
from mrjob.job  import MRJob
from mrjob.step import MRStep
import re

# Compiles regular expression pattern into a reusable regular expression object
WORD_RE = re.compile(r"[\w']+")

class invertedIndexing(MRJob):
    def steps(self):
        return [MRStep(mapper = self.mapper_word_index, 
                        reducer = self.reducer_word_index_list)]
    
    # Mapper takes in a key, which in this case is NONE, and a value, which is a line 
    def mapper_word_index(self, _, line):
        indexNumber, line = line.split(" ", 1) # Reads a line, extracts the indexNumber and creates list of the words in the line
        for word in WORD_RE.findall(line):
            if not word.isdigit(): # Only proceeds once word has been validated that it is not a number
               yield(word.lower(), indexNumber)  # Returns lowercase word and the index (line) number

    # Reducer takes in the key, which is a word, and a value, which is the index (line) number
    def reducer_word_index_list(self, word, indexNumbers):
        indexNumbersList = list(indexNumbers) # Creates a list of the index numbers
        yield(word.lower(), indexNumbersList)

if __name__ == '__main__':
	invertedIndexing.run()

