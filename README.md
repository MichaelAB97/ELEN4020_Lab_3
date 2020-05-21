# ELEN4020 - Lab 3
## Word Index
This was implemented using the mrs MapReduce framework
This can be run by running the runWordIndex.py file in terminal, which automatically searches through all three files - small.txt, large.txt and very_large.txt.
It also makes use of the stopWords.txt file.
The results are stored in their respective output folders.

## Top-K Query & Word Count
These algorithms were implemented using the MrJob Framework

## Build Instructions
The algorithms for this lab is written in Python 3
The requirements for the virtual environment can be found in requirements.txt

Please ensure that the following are installed:
- `Python 3.6+`
- `pip3`
- `virtualenv`

1. Create a virtual environment
`virtualenv venv`

2. Activate the virtual environment:
`source venv/bin/activate`

3. Install the requirements for the virtual environment:
`pip3 install -r requirements.txt`

4. To deactive the virtual environment:
`deactivate`


## Commands to run the following algorithms:
- Word Count: `python3 runWordFiles`
- Top-K Query: `python3 runTopKFiles`
- Inverted Index: `python3 runWordIndex.py`