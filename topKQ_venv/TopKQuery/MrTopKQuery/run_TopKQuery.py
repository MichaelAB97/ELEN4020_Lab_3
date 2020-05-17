# Run this file only: python3 run_TopKQuery.py small.txt
from TopKQueryJob import MRTopKWordQuery
import sys
import time

#Sorts the list according to the frequency of each word in descending order
# Iterate through the word-frequency pair list and find the top K words
def TopKWordsAlg(word_count_pairs, k):
	sortedList = sorted(word_count_pairs, reverse=True)		
	TopK_Words = sortedList[:k]

	print("\n----------------K = %i ---------------" % k)
	for word_count_pair in TopK_Words:
		print(word_count_pair[1], word_count_pair[0])
		

# Stores the word-frequency pair		
word_count_pairs = []

# Starts the process timer
startTime = time.time()

# Run the program locally
job_args = ['-r', 'local']
job_args.extend(sys.argv[1:])
mr_job = MRTopKWordQuery(args=job_args)

# Run the job class in TopKQuery.py
with mr_job.make_runner() as runner:
	runner.run()
	for key, word_count_list in mr_job.parse_output(runner.cat_output()):
		word_count_pairs.append(word_count_list)
	
	TopKWordsAlg(word_count_pairs, 10)
	TopKWordsAlg(word_count_pairs, 20)

	# Stops the process timer
	endTime = time.time()
	processTime = endTime - startTime

	
	print("\nProcess Time: ", processTime, 'seconds')