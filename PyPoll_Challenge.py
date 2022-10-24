# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load= os.path.join("election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Create a county list and county votes dictionary.
county_options= []
county_votes = {}

#Track the largest county and county voter turnout.
Largest_turnout_county = ''

# Track the winning candidate, vote count and percentage
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Write an if statement that checks that the

        # county does not match any existing county in the county list.

        if county_name not in county_options:

        # Add the county name to the county list.
            county_options.append(county_name)

        # And begin tracking that county's voter count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file: 
    
    election_results = (
         f"\nElection Results\n"
         f"-------------------------\n"
         f"Total Votes: {total_votes:,}\n"
         f"-------------------------\n\n"
         f"County Votes:\n")

    # Print the final vote count (to terminal) 
    print(election_results, end="")
    
    # Save the results to the text file
    txt_file.write(election_results)

# Write a for loop to get the county from the county dictionary.
    for county in county_votes:
        # Retrieve the county vote count.
        votes= county_votes[county]

        # Calculate the percentage of votes for the county.
        vote_percentage = float(votes)/float(total_votes) *100 
         
        county_results = ( 
            f"{county}: {vote_percentage: .1f}% ({votes})\n")

        # Print the county results to the terminal.
        print(county_results)
        # Save the county votes to a text file.
        txt_file.write(county_results)

        if (votes > winning_count) or (county == ''):
            winning_count = votes
            Largest_turnout_county= county

    winning_county_summary = (             
        f"-------------------------\n" 
        f"Largest County Trunout : {Largest_turnout_county}\n"
        f"-------------------------\n")
    # Print the largest turnout to the terminal
    print(winning_county_summary)
    # Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)
    winning_count = 0

    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
       
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage) :
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    winning_candidate_summary = (
        f"-------------------------\n\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
# Print the winning candidate (to terminal)
    print(winning_candidate_summary)
# Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

# Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
      
       


        
