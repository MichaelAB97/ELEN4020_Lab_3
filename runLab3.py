import os
import sys
import time 

print('=========== SMALL.TXT ==========')
start = time.time()
os.system('python3 invertedIndex.py ' + 'small.txt ' + 'invertedIndexSmall')
end = time.time()
duration = end - start
print("Inverting the index of the SMALL text took: ", duration, "s")
print(" ")
print("****************************************")
print(" ")
print('=========== LARGE.TXT ==========')
start = time.time()
os.system('python3 invertedIndex.py ' + 'large.txt ' + 'invertedIndexLarge')
end = time.time()
duration = end - start
print("Inverting the index of the Large text took: ", duration, "s")
print(" ")
print("****************************************")
print(" ")
print('=========== VERY LARGE.TXT ==========')
start = time.time()
os.system('python3 invertedIndex.py ' + 'very_large.txt ' + 'invertedIndexVeryLarge')
end = time.time()
duration = end - start
print("Inverting the index of the Large text took: ", duration, "s")
print(" ")
print("****************************************")


