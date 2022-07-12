#Election Results
#Import dependencies

from enum import unique
import os
import csv
#add budget_data.csv file
csvpath = os.path.join("Resources","election_data.csv")
PyPoll_output = os.path.join("PyPoll.txt")

#define variables
total_votes = 0
candidate_votes = []
candidates_list = {}
winner = 0
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

        candidate = row[2]
        if candidate in candidates_list:
            candidates_list[candidate] += 1
        else:
            candidates_list[candidate] = 1

print("Election Results")

print('-'*50)

print(f"Total Votes: {total_votes}")

print('-'*50)
            
for candidate in candidates_list:
                    
    percentage_votes = (candidates_list[candidate]/total_votes)
        
    print(f"{candidate}: {percentage_votes:.3%} ({candidates_list[candidate]})")     

    if candidates_list[candidate]>winner:
        winner = candidates_list[candidate]
        winner_name = candidate


print('-'*50)

print(f"Winner: {winner_name}")

print('-'*50)

#print to text file


with open(PyPoll_output,'w') as file:
    file.write("Election Results\n")
    file.write("=" *50+"\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("=" *50+"\n")
    for candidate in candidates_list:
        file.write(f"{candidate}: {percentage_votes:.3%} ({candidates_list[candidate]})\n")
    file.write("=" *50+"\n")
    file.write(f"Winner: {winner_name}\n")
    
