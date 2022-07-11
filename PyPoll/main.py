#Election Results
#Import dependencies

import os
import csv
#add budget_data.csv file
csvpath = os.path.join('/Users/kaseymathues/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv')

#define variables
total_votes = 0
votes_won = 0
candidates = []
unique_candidates = []
#open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath) as csvfile:
    #This stores a reference to a file stream
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first
    csv_header = next(csvreader)
    # Read each row of data after the header
    
    for row in csvreader:
        #Total number of votes cast
        total_votes += 1
        candidates.append(row[2])
    
   

print('Election Results')
print('-'*50)
print(f'Total Votes: {total_votes}')
print('-'*50)
print(f'{unique_candidates}')