#This program opens the input file, opens the output file and writes out the line it decoded from the input file to the output file
# It also keeps track of the line numbers and attaches them to the lines
import sys

args=sys.argv[1:]
inputFile = args[0]
outputFile = args[1]
currentIndexNumber = 0

with open(inputFile, 'rb') as inputFile:
    with open(outputFile,'w') as outputFile:
        for line in inputFile:
            currentIndexNumber = currentIndexNumber + 1
            outputFile.write('{} \t {}'.format(currentIndexNumber, line.decode()))
