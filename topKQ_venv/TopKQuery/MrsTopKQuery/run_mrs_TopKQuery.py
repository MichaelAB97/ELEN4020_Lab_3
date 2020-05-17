import sys
import shutil, os
import time

def key_(word_count_pair):
	return word_count_pair[1]

#Sorts the list according to the frequency of each word in descending order
# Iterate through the word-frequency pair list and find the top K words
def TopKWordsAlg(word_count_pairs, k):
	sortedList = sorted(word_count_pairs, key=key_ ,reverse=True)		
	TopK_Words = sortedList[:k]

	print("\n----------------K = %i ---------------" % k)
	for word_count_pair in TopK_Words:
		print(word_count_pair[0], word_count_pair[1])
		
# Stores the word-frequency pair	
word_count_pairs = []
	
def main():	
	filename = sys.argv[1]
	startTime = time.process_time()	
	os.system('python3 word_count.py ' + filename + ' output')

	f = open("output/source_0_split_0_.mtxt", "r")
	words = f.readlines()
	for lines in words:
		key,frequency = lines.split()
		word_count_pairs.append([key, frequency])
	
	TopKWordsAlg(word_count_pairs, 10)
	TopKWordsAlg(word_count_pairs, 20)
	
	# Stops the process timer
	endTime = time.process_time()
	processTime = (endTime - startTime)
	print("Proccess Time: ", processTime, "seconds" )


if __name__ == '__main__':
        main()








