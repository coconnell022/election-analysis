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

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To Do: Read and analyze the data.
    #print(election_data)

    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #print the header row.
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
       print(row)

#Close the file.
election_data.close()

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()
