# Import string, mrs and regular expressions modules
import re
import mrs
import string

# Extract stop words from textfile and store in a list
stopWords = open('stopWords.txt','r').read().split()

class invertedIndexing(mrs.MapReduce):
    
    # Mapper takes in a key, which is the indexNumber and a value, which is a line 
    def map(self, indexNumber, line):
        # Reads a line and creates list of the words in the line
        line = line.split() 
        for word in line:
            # Converts all letters to lowercase
            word = word.lower()
            # Converts every instance of punctuation to a space
            word = word.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
            #Only maps word once it has been validated that it only contains the alphabet, it's larger than 3 letters and is not a stopword
            if word.isalpha() and len(word) > 3 and word not in stopWords: 
               yield(word, indexNumber + 1)  # Returns lowercase word, stripped of all punstuation and the index number

    # Reducer takes in the key, which is a word, and a value, which is the index number and returns the list of indexNumbers
    def reduce(self, word, indexNumber):
        indexNumbers = []

        for currentIndex in indexNumber:
            # If statements to ensure only the first 50 lines are recorded and that if a word appears twice on one line, its only recorded once
            if len(indexNumbers) >= 50:
                break
            if currentIndex not in indexNumbers:
                indexNumbers.append(currentIndex)       
        yield(indexNumbers)

if __name__ == '__main__':
	mrs.main(invertedIndexing)

