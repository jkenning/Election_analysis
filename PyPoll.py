# The data we need to retrieve
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# declare new list to get candidate names
candidate_options = []
# declare dictionary for votes per candidate
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print candidate names from each row
        candidate_name = row[2]
        # If candidate does not match an existing candidate
        if candidate_name not in candidate_options:
            # Add candidate name to the candidate list
            candidate_options.append(candidate_name)
            # track votes for each candidate
            candidate_votes[candidate_name] = 0
        # count votes for each candidate
        candidate_votes[candidate_name] += 1

# Save results to text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidates list
    for candidate_name in candidate_votes:    
        # Retrieve vote count of as candidate
        votes = candidate_votes[candidate_name]
        # calculate percentage of vote count
        vote_percentage = float(votes) / float(total_votes) * 100
        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
        # define the candidates results
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        #  Save the candidate results to text file
        txt_file.write(candidate_results)
    # print winning candidate summary to terminal
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    # # print winninng candidate summary
    # print(winning_candidate_summary)
    # # print the total votes
    # print(total_votes)
    # # print the candidate list
    # print(candidate_options)
    # # print candidate votes
    # print(candidate_votes)

election_data.close()
