# Election Analysis

Analysis of several hundred thousand votes as part of an election audit for a congressional district in Colorado.

## Overview of Project

This analysis scenario involves assisting a board of elections employee named Tom, for an election audit of the results of a U.S. congressional district in Colorado. The task involves calculating and reporting on the following information:

1. The total number of votes cast
2. A list of candidates who recieved votes
3. The total number of votes cast for each candidate
4. The percentage of votes for each candidate
5. Confirm the winner of the election based on the popular vote

### Purpose

While this analysis could be performed in Excel, the goal is to determine if there is a way to automate the process using Python. If successful, this code could therefore be used to audit senatorial races and local elections in addition to other congressional districts. 

## Data Preparation and Analysis

The full analysis performed for this project can be found in [PyPoll_Challenge.py](https://github.com/jkenning/Election_analysis/blob/main/PyPoll_Challenge.py), a text summary of the primary results in [Analysis](https://github.com/jkenning/Election_analysis/tree/main/Analysis), and additional resources (including original data set) in the [Resources](https://github.com/jkenning/Election_analysis/tree/main/Resources) folder. 
Software used: Python 3.9.1, Visual Studio Code 1.52.1

Below is a short summary of the activities performed to prepare the data set and perform analysis of the election results:

1. Imported data and checked if it is readable
2. Created a roadmap for sequential steps in the analysis using psuedocode
3. Looped through the rows of data to determine total number of votes cast and define the unique candidates in the election using a repitition statement
4. Quantified the votes for each candidate, calculated their percentage share of the vote, and determined the winner using repitition and conditional statements
5. Printed the election results and winning candidate summary to a text file
6. Repeated steps 3-5 to modify the code for analysis of counties within the electoral district instead of candidates

## Election-Audit Results

The analysis of the election shows:

* There were 369,711 total votes cast

* There were three candidates in the election:
    1. Charles Casper Stockham
    2. Diana DeGette
    3. Raymon Anthony Doane

* The results for each candidate were:
    1. Charles Casper Stockham: 23.0% (85,213 votes)
    2. Diana DeGette: 73.8% (272,892 votes)
    3. Raymon Anthony Doane: 3.1% (11,606 votes)

* Therefore, the winner of the election was Diana DeGette with a winning percentage of 73.8% from 272,892 votes.

### Voter Turnout by County

Additional data was also requested by election commision to complete the audit:

- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

Results for this analysis:

* There were three counties in the election precinct:
    1. Jefferson
    2. Denver
    3. Arapahoe

* The results for each county:
    1. Jefferson: 10.5% (38,855 votes)
    2. Denver: 82.8% (306,055 votes)
    3. Arapahoe: 6.7% (24,801 votes)

* Denver had the largest vote turnout with 306,055 votes cast, making up 82.8% of the total votes cast in the election.
`
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
        

Figure. 1 - The initial code analyzing votes for candidates was re-purposed to also assess votes by county; this segment writes a decision statement to determine a list of counties and track and add the votes as it loops through the data set rows. 

    `# 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > largest_count):
            largest_count = votes
            largest_county = county_name

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {largest_county}\n"
    f"-------------------------\n")
    print(winning_county_summary)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

Figure. 2 - This section of the script was used to write a repitition statement to determine the votes, percentage votes, and county with the largest vote, while printing the results. 

![Terminal output](https://github.com/jkenning/Election_analysis/tree/main/Resources/printed_results_terminal.png)

Figure. 3 - The script prints the election results to the terminal when run (version also printed to text file can be found [here](https://github.com/jkenning/Election_analysis/blob/main/Analysis/election_results.txt))

## Election-Audit Summary

One of the main purposes for writing this script is to support a business proposal to the election commision for how the script could be used, with some modifications, for any election. Below are two examples of how the script could potentially be modified:

1. For national or presidential level elections on a larger geographic scale, the same script that was used to analyze the number of votes coming from individual counties could be very easily modified to break down the number of votes from each state as well. This could be done by simply creating a new list and dictionary for States, then changing the county variables and referencing the correct data collumn within repetition and conditional statements.

2. If the election is in support of a policy decision instead of a candidate, the script could just as easily be modified to count 'for' or 'against' instead of candidate names in a similar manner as explained above. 