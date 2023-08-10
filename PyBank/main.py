# import the os module
import os
# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Set following varibles:
# Profit/Loss of previous month
Pre_month = 0
# Difference of profit/loss between previous month and current month 
change = 0
# Total diffences 
total_changes = 0
# Set list for date
Months = []
# Set list for every change 
change_list = []
# Set list for profit/loss
profit = []
# Set list for greatest increase in profit/loss
greatest_increase = ["", 0]
# Set list for greatest decrease in profit/loss
greatest_decrease = ["", 0]

#Using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print("Financial Analysis")
    print("----------------------------")

    # Read the header row first 
    header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:

        # Set the value for profit/loss current month
        profitloss = int(row[1])

        # When calculate the change, we skip the first month because it will minus 0
        if Pre_month != 0:

            # For change of profit/loss, using profit/loss of curent month minus that of previous month
            change = profitloss-Pre_month

            # Save the change to a list
            change_list.append(change)

        # Reset previous month 
        Pre_month = profitloss
        
        # Selecting the greatest increase
        if change > greatest_increase[1]:
            greatest_increase[1] = change

            # Save the date of that increase
            greatest_increase[0] = row[0]

        # Selecting the greatest decrease
        if change < greatest_decrease[1]:
            greatest_decrease[1] = change

            # Save the date of that decrease
            greatest_decrease[0] = row[0]

        # Insert the date to the list
        Months.append(row[0])

        # Insert the profit/loss to the list
        profit.append(profitloss)

    # Calculate how many changes
    total_changes = len(change_list) 

    # Calculate total month
    Totalmonth = len(Months) 

    # Print otal month
    print(f"Total Months: {Totalmonth}")

    # Print total profit/loss
    print(f"Total: ${sum(profit)}")

    # Print average of changes
    print(f"Average Change: ${round((sum(change_list))/total_changes,2)}")

    # Print the date and value of the greatest increase 
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${(max(change_list))})")

    # Print the date and value of the greatest increase 
    print(f"Greatest decrease in Profits: {greatest_decrease[0]} (${(min(change_list))})")

# Save the txt file path
output_file = os.path.join("Analysis/Financial Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open("Analysis/Financial Analysis.txt", "w") as datafile:
   string_to_write = ("Financial Analysis \n"
                      "---------------------------- \n"
                      f"Total Months: {Totalmonth} \n"
                      f"Total: ${sum(profit)} \n"
                      f"Average Change: ${round((sum(change_list))/total_changes,2)} \n"
                      f"Greatest Increase in Profits: {greatest_increase[0]} (${(max(change_list))}) \n"
                      f"Greatest decrease in Profits: {greatest_decrease[0]} (${(min(change_list))})")

# Write results to txt file
   datafile.write(string_to_write)


   
    
    

   
    
    



    