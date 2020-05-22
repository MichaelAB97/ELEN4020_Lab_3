from wordCount import FrequencyCount                                   #impoting the class
import sys
import time

result_pairs = []                                                   #the array that stores the word and the frequency
t_start = time.time()                                         		#starting the timer
task_args = ['-r', 'local']                                           #(basically saying run it in local mode) -r is the type of a runner
task_args.extend(sys.argv[1:])
mr_job = FrequencyCount(args=task_args)                              
with mr_job.make_runner() as runner:                                  #giving mr_job.make_runner a simpler name - runner (an alias)
	runner.run()
	for word, frequency in mr_job.parse_output(runner.cat_output()):   
		result_pairs.append([word, frequency])     					   #combining the outputs
	
	t_end = time.time() - t_start                             			#checking how long MRJob took
	
	for distinct_word in result_pairs:
		distinct_word
		print(distinct_word[0], " ", distinct_word[1])               #Limit output to 50 as stated in lab brief.
	
	print("Time taken to process: ", t_end)