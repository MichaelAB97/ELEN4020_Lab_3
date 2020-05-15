# Imports job class, invertedIndexing
from invertedIndex import invertedIndexing
import sys
import time

# Tuple to store the word and index number pair
wordIndexNumber = []
start = time.process_time()

# To ensure parallelisation
runtimeArguments = ['-r', 'local']
runtimeArguments.extend(sys.argv[1:])
runningJob = invertedIndexing(args=runtimeArguments)

with runningJob.make_runner() as runner: # Run invertedIndex from another script 
    runner.run()
    for word, indexNumbers in runningJob.parse_output(runner.cat_output()):
        wordIndexNumber.append([word, indexNumbers])
        duration = time.process_time() - start

        for oneWord in wordIndexNumber[:50]:
            print(oneWord[0], ' ', oneWord[1])
        print('This process took: ', duration, 's')


