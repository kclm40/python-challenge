#Financial Analysis
#----------------------------------------
#Import dependencies
from cgitb import text
import os
import csv

#add budget_data.csv file
csvpath = os.path.join('/Users/kaseymathues/dropbox/Mac/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv')

#define PyBank variables



total_months = 0
net_profit_loss = 0
average_change = 0
previous_month = 0
greatest_increase = 0
greatest_decrease = 0
increase_month = ""
decrease_month = ""


#open the file in "read" mode ('r') and store the contents in the variable "text"
with open(csvpath) as csvfile:

    #This stores a reference to a file stream
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Read the header row first
    csv_header = next(csvreader)
    
    
    # Read each row of data after the header
    
    for row in csvreader:
        
        current_month = float(row[1])
    
        if total_months == 0:
            greatest_increase = 0
            greatest_decrease = 0
            increase_month = row[0]
            decrease_month = row[0]
        else:
            #calculate greatest increase & decrease
            change = current_month-previous_month
            average_change += change
            if change > greatest_increase:
                greatest_increase = change
                increase_month = row[0]
            elif change < greatest_decrease:
                greatest_decrease = change
                decrease_month = row[0]
        
        previous_month = current_month
        
    


    
    #calculate the # of months
        total_months +=1
    
    #calculate the net total amount of "Profit/Losses" over the entire period
        net_profit_loss += int(row[1])
       
       
        
    #calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
        
average_change = average_change/(total_months-1)   
        
#Summary
print("Financial Analysis")
print("-" * 50)
print(f"Total Months: {total_months}")
print(f"Net Total P/L: ${net_profit_loss}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Great Increase in Profits: {increase_month} (${round(greatest_increase)})")
print(f"Great Decrease in Profits: {decrease_month} (${round(greatest_decrease)})")

#print to text file
textfile_summary = []
textfile_summary.append("Financial Analysis")
textfile_summary.append("-" * 50)
textfile_summary.append(f"Total Months: {total_months}")
textfile_summary.append(f"Net Total P/L: ${net_profit_loss}")
textfile_summary.append(f"Average Change: ${round(average_change,2)}")
textfile_summary.append(f"Great Increase in Profits: {increase_month} (${round(greatest_increase)})")
textfile_summary.append(f"Great Decrease in Profits: {decrease_month} (${round(greatest_decrease)})")

filename = 'PyBank.txt'

with open(filename,'w') as file:
    for PyBank in textfile_summary:
        print(textfile_summary)
        file.write(PyBank + '\n')


