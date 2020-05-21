from mrjob.job  import MRJob
from mrjob.step import MRStep
import string
import time
import re

word_re    = re.compile(r"[\w']+") #looks for words such as "word", word's "word's", word

def getStopWords():
	return [ "a", "about", "above", "after", "again", 
	"against", "all", "am", "an", "and", "any", "are", 
	"as", "at", "be", "because", "been", "before", "being", 
	"below", "between", "both", "but", "by", "could", "did", 
	"do", "does", "doing", "down", "during", "each", "few", 
	"for", "from", "further", "had", "has", "have", "having", 
	"he", "he'd", "he'll", "he's", "her", "here", "here's", 
	"hers", "herself", "him", "himself", "his", "how", "how's", 
	"i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", 
	"it", "it's", "its", "itself", "let's", "me", "more", "most", 
	"my", "myself", "nor", "of", "on", "once", "only", "or", 
	"other", "ought", "our", "ours", "ourselves", "out", "over", 
	"own", "same", "she", "she'd", "she'll", "she's", "should", 
	"so", "some", "such", "than", "that", "that's", "the", 
	"their", "theirs", "them", "themselves", "then", "there", 
	"there's", "these", "they", "they'd", "they'll", "they're", 
	"they've", "this", "those", "through", "to", "too", "under", 
	"until", "up", "very", "was", "we", "we'd", "we'll", "we're", 
	"we've", "were", "what", "what's", "when", "when's", "where", 
	"where's", "which", "while", "who", "who's", "whom", "why", 
	"why's", "with", "would", "you", "you'd", "you'll", "you're", 
	"you've", "your", "yours", "yourself", "yourselves" ]


stop_words = getStopWords()

#creating a class and importing the framework MRJob. In heriting from the MRJob
class FrequencyCount(MRJob):                               
    #overiding the MRJob functions. MRStep is a constructor
	def steps(self):                                                            
		return [  MRStep(mapper   = self.map_get_word,         
						 combiner = self.comb_count_word,
						 reducer  = self.red_count_word)]
		
    #getting the lines from the text
	def map_get_word(self, _, line):   
        #yield each word in the line
		for word in word_re.findall(line):                      #geting the words from the line
			word = word.strip(string.punctuation).lower()       #remove punctuations and change to lower case
			if word.lower() not in stop_words:                  #exclude stop words
				if not word.isdigit():                          #make sure there are no numbers
					yield (word.lower(), 1)                     #return the word that passed all the checks and the 1 means that it is only counted once
			
	def comb_count_word(self, word, counts):
		# optimization: sum the words we've seen so far
		yield (word, sum(counts))
		
	def red_count_word(self, word, counts):
		# sum the rest of the words we've seen so far
		yield (word, sum(counts))
		
if __name__ == '__main__':
	FrequencyCount.run()