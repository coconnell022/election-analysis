#The data we need to retrieve
#1. The total number of votes cast
#2. The complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on the popular vote.

#Add our dependencies.
import csv
import os

#Assign a variable to the file to load and the path
file_to_load = "/Users/caroline/Documents/Data Boot Camp/Module 3/Canvas/election-analysis/Resources/election_results.csv"
    #DONT USE but indirect path would be... file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to the file to save and the path
file_to_save = "/Users/caroline/Documents/Data Boot Camp/Module 3/Canvas/election-analysis/analysis/election_analysis.txt" 
    #DONT USE but indriect path would be... file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0

#Candidate options
candidate_options = []

#declare candidate vote dictionary
candidate_votes = {}

#declare winning cadidate and winning count
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
       #2. Add to the total vote count.
        total_votes += 1

       #Print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any exisiting candidate...
        if candidate_name not in candidate_options:
           
            #add the candidate name to the list
            candidate_options.append(candidate_name)

            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    #save the results to our txt file
    with open(file_to_save, "w") as txt_file:
        election_results = (f"\nElection Results\n-------------------------\nTotal Votes: {total_votes:,}\n-------------------------\n")
        print(election_results, end="")

        #save the final vote count to the text file
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:

            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]

            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # To do: print out each candidate's name, vote count, and percentage of
            # votes to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage

                # 3. Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)

        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {float(votes) / float(total_votes) * 100:.1f}% of the vote.")

        #print the candidate vote dictionary
        #print(candidate_votes)

        #Print the candidate list
        #print(candidate_options)

        #3. Print the total votes.
        #print(total_votes)

#Close the file.
election_data.close()

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()

