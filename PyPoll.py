# The data we need to retrieve
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
# Close the file.
election_data.close()









# 1. Total number of votes cast

# 2. complete list of candidates wgo recieved votes

# 3. Percentage of votes for each candidate won

# 4. total number of votes for each candidate won

# 5. winner of the election based on popular vote