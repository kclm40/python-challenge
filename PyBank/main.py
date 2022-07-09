#Financial Analysis
#----------------------------------------
#Import dependencies
import os
import csv

#define PyBank variables
months = []
profit_losses = []

total_months = 0
net_profit_loss = 0
changes_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0

#add budget_data.csv file
csvpath = os.path.join('/Users/kaseymathues/dropbox/Mac/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv')

#open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath) as csvfile:

    #This stores a reference to a file stream
    csvreader = csv.reader(csvfile, delimiter=',')

    # Store all of the text inside a variable called "lines"
    print(csvreader)

    #Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        months.append(row[0])

        #Total Months
        print(f"Total Months: {len(months)}")
