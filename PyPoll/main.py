#Election Results

#Import dependencies
from cgitb import text
import os
import csv

#add budget_data.csv file
csvpath = os.path.join('/Users/kaseymathues/dropbox/Mac/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv')


#define variables

total_votes = 0
votes_won = 0

candidates = []

#open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath) as csvfile:

    #This stores a reference to a file stream
    csvreader = csv.reader(csvfile, delimiter=',')
    print([csvreader])
    
    #Read the header row first
    csv_header = next(csvreader)