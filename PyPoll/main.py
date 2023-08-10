# Import the os module
import os
# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

# Set following lists:
# List for all votes
vote_list = []
# Votes for Charles Casper Stockham
vote_CC = []
# Votes for Diana DeGette
vote_DD = []
# Votes for Raymon Anthony Doane
vote_RA = []
# Final winner
winner = []

#Using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print("Election Results")
    print("-------------------------")

    # Read the header row first 
    header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # Add all the votes to a list
        vote_list.append((row[2]))

        #Create a vote list of Charles Casper Stockham
        if row[2] == "Charles Casper Stockham":
            vote_CC.append(row[2])

        #Create a vote list of Diana DeGette
        if row[2] == "Diana DeGette":
            vote_DD.append(row[2])

        #Create a vote list of Raymon Anthony Doane
        if row[2] == "Raymon Anthony Doane":
            vote_RA.append(row[2])
        
# Calculate the total number of votes cast
Total_vote = len(vote_list)

# Calculate the percentage of votes each candidate won
# Charles Casper Stockham
percent_CC = round(len(vote_CC)/Total_vote * 100, 3)
# Diana DeGette
percent_DD = round(len(vote_DD)/Total_vote * 100, 3)
# Raymon Anthony Doane
percent_RA = round(len(vote_RA)/Total_vote * 100, 3)

# Print the total number of votes cast
print(f"Total Votes: {Total_vote}")
print(f"-------------------------")

# Print the total number and percentage of votes each candidate won
# Charles Casper Stockham
print(f"Charles Casper Stockham: {percent_CC}% ({len(vote_CC)})")
# Diana DeGette
print(f"Diana DeGette: {percent_DD}% ({len(vote_DD)})")
# Raymon Anthony Doane
print(f"Raymon Anthony Doane: {percent_RA}% ({len(vote_RA)})")

print(f"-------------------------")

# Select the winner by comparing their percentage of votes
# If Charles Casper Stockham has the grestest  percentage of votes
if percent_CC > percent_DD and percent_CC > percent_RA:
    winner = "Charles Casper Stockham"

# If Diana DeGette has the grestest  percentage of votes
if percent_DD > percent_CC and percent_DD > percent_RA:
    winner = "Diana DeGette"

# If Raymon Anthony Doane has the grestest  percentage of votes
if percent_RA > percent_DD and percent_RA > percent_CC:
    winner = "Raymon Anthony Doane"

# Print the final winner
print(f"Winner: {winner}")
print(f"-------------------------")

# Save the txt file path
output_file = os.path.join("Analysis/Election Results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open("Analysis/Election Results.txt", "w") as datafile:
   string_to_write = ("Election Results \n"
                      "------------------------- \n"
                      f"Total Votes: {Total_vote} \n"
                      f"------------------------- \n"
                      f"Charles Casper Stockham: {percent_CC}% ({len(vote_CC)}) \n"
                      f"Diana DeGette: {percent_DD}% ({len(vote_DD)}) \n"
                      f"Raymon Anthony Doane: {percent_RA}% ({len(vote_RA)}) \n"
                      f"------------------------- \n"
                      f"Winner: {winner} \n"
                      f"-------------------------")
# Write results to txt file
   datafile.write(string_to_write)

