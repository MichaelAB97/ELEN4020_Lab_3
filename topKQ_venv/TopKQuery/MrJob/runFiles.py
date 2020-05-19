import os
import sys
import time 

print('=========== SMALL.TXT ==========')
os.system('python3 run_TopKQuery.py ' + 'small.txt ')
print(" ")
print("****************************************")
print(" ")
print('=========== LARGE.TXT ==========')
os.system('python3 run_TopKQuery.py ' + 'large.txt ')
print(" ")
print("****************************************")
print(" ")
print('=========== VERY LARGE.TXT ==========')
#os.system('python3 run_TopKQuery.py ' + 'very_large.txt ')
print(" ")
print("****************************************")