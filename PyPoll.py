#The data we need to retrieve
# To do: perform analysis.

from cgitb import text
import csv
from distutils import text_file
import os

# Add a variable to load a file from a path.
file_to_load= os.path.join("election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize the vote counter
total_votes = 0

with open(file_to_load) as election_data:
    
     print(election_data)

# A complete lists of candidates who received votes
candidate_votes = {}
Candidate_options =[]
 

# The percentage of vote each candidate won
winning_candidate =""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
     file_reader =csv.reader(election_data)
     Headers=next(file_reader)

     # Print each row in the CSV file.
     for row in file_reader:
          # Add to the total vote count.
          total_votes += 1
          # Print the candidate name from each row.
          candidate_name = row[2]
          # If the candidate does not match any existing candidate add it to
          # the candidate list  
          if candidate_name not in Candidate_options:
               # Add it to the list of candidates.
               Candidate_options.append(candidate_name)
               # Begin tracking the candidate's vote count
               candidate_votes[candidate_name] = 0
          # Add a vote to that candidate's count.
          candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
     election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n")
     # Print the final vote count (to terminal)      
     print(election_results, end="")
     # Save the final vote count to the text file.
     txt_file.write(election_results)
     
     with open(file_to_load) as election_data:
          file_reader =csv.reader(election_data)
     for candidate_name in candidate_votes:

          votes = candidate_votes[candidate_name]
          # Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_votes) * 100
     
          # Print each candidate, their voter count, and percentage to the terminal.
          
          candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

          # Print each candidate including their votes count and percentage to the terminal
          print(candidate_results)

          #Save each candidate including their votes count and percentage to the text file
          txt_file.write(candidate_results)
          
          if (votes > winning_count) and (vote_percentage > winning_percentage):
          # If true then set winning_count = votes and winning_percent =
          # vote_percentage.
               winning_count = votes
               winning_candidate = candidate_name  
               winning_percentage = vote_percentage

          #To do: print out the winning candidate, vote count and percentage to
          #   terminal.
               winning_candidate_summary = (
               f"-------------------------\n"
               f"Winner: {winning_candidate}\n"
               f"Winning Vote Count: {winning_count:,}\n"
               f"Winning Percentage: {winning_percentage:.1f}%\n"
               f"-------------------------\n")

     # Print each candidate, their voter count, and percentage to the terminal.
     print(winning_candidate_summary)
     # Save the winning candidate's results to the text file.
     txt_file.write(winning_candidate_summary)
          
       
          
          
               