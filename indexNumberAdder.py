#This program adds index numbers to each line in a file
import sys

# Command line system arguments allowing us to open and write to two files
args=sys.argv[1:]
inputFile = args[0]
outputFile = args[1]
currentIndexNumber = 0

# Opening input and output files
with open(inputFile, 'rb') as inputFile:
    with open(outputFile,'w') as outputFile:
        # Reads line, creates it's indexNumber, writes the indexNumber and line out to outputFile
        for line in inputFile:
            currentIndexNumber = currentIndexNumber + 1
            outputFile.write('{} \t {}'.format(currentIndexNumber, line.decode()))
