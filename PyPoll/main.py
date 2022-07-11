#Election Results
#Import dependencies

from enum import unique
import os
import csv
#add budget_data.csv file
csvpath = os.path.join("Resources","election_data.csv")
    #correct file path
    # csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#define variables
total_votes = 0
votes_won = 0
candidates = {}
winner = []
#open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath) as csvfile:
    #This stores a reference to a file stream
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row first
    csv_header = next(csvreader)
    # Read each row of data after the header
    
    for row in csvreader:
        #Total number of votes cast
        
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1
        
        total_votes += 1

        if votes_won < total_votes:
            winner = candidates
    
    #find candidate names:
    
    
   

print("Election Results")
print('-'*50)
print(f"Total Votes: {total_votes}")
print('-'*50)
print(f"{candidates}")
print(f"{winner}")