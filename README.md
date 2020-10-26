# election-analysis
Using python to do an analysis on election results

## Overview of Election Audit
A Colorado Board of Elections employees are requesting an election audit of a recent local congressional election. They need a thorough analysis of the election including total number of votes per county, overall percentages, and winning candidate based on popular vote. The purpose of writing an automated code using Python is to create a code that can be used in not only small local elections but also future larger elections. Since multiple different voting methods were used in this election, one centralized election results worksheet with about 370,00 rows was generated. This data source was then used to determine the overall election results pertaining to each candidate and county. 

    Resources
    - Data Source: election_results.csv
    - Software: Python 3.7.6, Visual Studio Code, 1.50.0

## Election-Audit Results

- There were **369,711** congressional votes cast in the election.

- The county results for the precinct were:
  - Jefferson County received 10.5% of the vote and 38,855 votes.
  - Denver County received 82.8% of the vote and 306,055 votes. 
  - Arapahoe County received 6.7% of the vote and 24,801 votes.

-	**The county with the greatest turnout of voters was Denver County**
  
- The candidates results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes. 
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
 

-	**The winner of the election was Diana DeGette, who received 73.8% of the vote and 272,892 votes.**


*See attached image below for a snapshot of the election_results.txt file*

![alt text]( https://github.com/coconnell022/election-analysis/blob/main/Images%20for%20ReadMe/Election%20Results%20Txt%20File.png?raw=true)


## Election-Audit Summary

This code was written with the purpose of being able to be modified and used in future elections. The original code performed an analysis on 3 identifying factors from the dataset: Ballot ID, County, and Candidate. There is room to modify the code if a further analysis were to be requested that included more criteria for each vote. For example, a comparison can be made in the different types of voting methods to decide if more funding needs to be allocated to a certain voting method to allow equal opportunity and poll access in all future elections. Another example would be adding political party for each vote cast to give insight into how people in each political party are voting. 

Another way that this script can be modified is to provide more comprehensive election findings to determine where each candidate received the greatest number of votes depending on county or other specific demographic factors. This type of analysis could help influence future elections by allowing candidates to have a better understanding of how certain areas of the state are voting, which would allow for changes in campaign strategy. 

        Caroline O'Connell
        October 11th, 2020
