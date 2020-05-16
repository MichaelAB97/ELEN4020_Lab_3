from TopKQueryJob import MRTopKWordQuery
import sys
import time

#Sorts the list according to the frequency of each word in descending order
def sort_list(word_count_pairs):
	sortedList = sorted(word_count_pairs, reverse=True)
	return sortedList

# Iterate through the word-frequency pair list and find the top K words
def TopKWords(sortedList, k):
	print("\n----------------K = %i ---------------" % k)
	if len(sortedList) < k:
		k = len(sortedList)
		
	TopK_Words = sortedList[:k]

	for word_count_pair in TopK_Words:
		print(word_count_pair[1], word_count_pair[0])
		
# Stores the word-frequency pair		
word_count_pairs = []

# Starts the timer
startTime = time.process_time()

# Run the program locally
job_args = ['-r', 'local']
job_args.extend(sys.argv[1:])
mr_job = MRTopKWordQuery(args=job_args)

# Run the job class in TopKQuery.py
with mr_job.make_runner() as runner:
	runner.run()
	for key, word_count_list in mr_job.parse_output(runner.cat_output()):
		word_count_pairs.append(word_count_list)
	
	sortedList = sort_list(word_count_pairs)
	
	endTime = time.process_time()
	processTime = endTime - startTime

	TopKWords(sortedList, 10)
	TopKWords(sortedList, 20)
	print("\nProcess Time: ", processTime, 'seconds')