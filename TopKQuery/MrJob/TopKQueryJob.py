from mrjob.job  import MRJob
from mrjob.step import MRStep
import re
import os

PATH 	   = os.path.dirname(os.path.abspath(__file__))
STOP_WORDS = os.path.join(PATH, 'stopWords.txt')
WORD_RE    = re.compile(r"[\w']+")

class MRTopKWordQuery(MRJob):

	def steps(self):
		return [ MRStep(mapper = self.mapper_get_words, 
						combiner = self.combiner_count_words, 
						reducer  = self.reducer_count_words)]
		
	# Yeilds the lowercase word, when the word 
	# in each line is not a stop word or an integer
	def mapper_get_words(self, _, line):
		# yield each word in the line
		for word in WORD_RE.findall(line):
			if word.lower() not in STOP_WORDS:
				if not word.isdigit():
					yield (word.lower(), 1)
			
	# Sums the words that have already been read
	def combiner_count_words(self, word, counts):
		yield word, sum(counts)
	
	# Send word-frequency pairs to the same reducer
	def reducer_count_words(self, word, counts):
		yield None, (sum(counts), word)
			
			
if __name__ == '__main__':
	MRTopKWordQuery.run()