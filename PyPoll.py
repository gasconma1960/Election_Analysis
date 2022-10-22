#The data we need to retrieve
# To do: perform analysis.
import csv
import os

file_to_load= os.path.join("election_results.csv")

with open(file_to_load) as election_data:
    
     print(election_data)
# Close the file.
# Open the election results and read the file
     # To do: perform analysis.

#1. The total number of votes cast
total_votes = 0
#2. A complete lists of candidates who received votes
Candidate_options =[]
candidate_votes = {}

total_votes = 0

#3. The percentage of vote each candidate won
winning_percentage = 0

#4. the total number of votes each canditate won
winning_candidate =""
winning_count = 0
#5. The winner of the election base on popular vote.

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.

    txt_file.write("Counties en the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
    

# Read the file object with the reader function.
with open(file_to_load) as election_data:
     file_reader =csv.reader(election_data)
     header =next(file_reader)
# Print each row in the CSV file.
     for row in file_reader:
          print(row)

# Close the file
election_data.close()

     