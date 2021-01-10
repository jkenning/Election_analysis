# Election Analysis

Analysis of several hundred thousand votes as part of a congressional election audit for a district in Colorado

## Overview of Project

This analysis scenario involves assisting a board of elections employee named Tom, for an election audit of the results of a U.S. congressional district in Colorado. The task involves calculating and reporting on the following information:

1. The total number of votes cast
2. A list of candidates who recieved votes
3. The total number of votes cast for each candidate
4. The percentage of votes for each candidate
5. Confirm the winner of the election based on the popular vote

Three main voting methods will be taken into account which will determine the outcome of the results:

- Mail-in ballots
- Punch cards
- Direct Recording Electronic voting machines

### Purpose

While this analysis could be performed in Excel, the goal is to determine if there is a way to automate the process using Python. If successful, this code could therefore be used to audit senatorial races and local elections in addition to other congressional districts. 

## Data Preparation and Initial Analysis Performed

The full analysis performed for this project can be found at !(), and additional resources in !(). 
Software used: Python 3.9.1, Visual Studio Code 1.52.1

Below is a short summary of the activities performed to prepare the data set and perform initial analysis of the election results:

1. Imported data and checked if it is readable
2. Created a roadmap for sequential steps in the analysis using psuedocode
3. Used a 'for' loop through the rows of data to determine total number of votes cast and define the unique candidates in the election
4. Quantified the votes for each candidate, calculated their percentage share of the vote, and determined the winner using a 'for' loop and 'if' statement
5. Printed the election results and winning candidate summary to a text file

## Election Results

The analysis of the election shows:

- There were 369,711 total votes cast

- There were three candidates in the election:
    1. Charles Casper Stockham
    2. Diana DeGette
    3. Raymon Anthony Doane

- The results for each candidate were:
    1. Charles Casper Stockham: 23.0% (85,213 votes)
    2. Diana DeGette: 73.8% (272,892 votes)
    3. Raymon Anthony Doane: 3.1% (11,606 votes)

- Therefore the winner of the election was Diana DeGette with a winning percentage of 73.8% and 272,892 votes.

## Additional analyses

Some additional data has also been requested by election commision to complete the audit:

- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout




## Summary

