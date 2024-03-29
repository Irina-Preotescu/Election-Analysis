# The Data We Need to Retrieve:
# 1. The total number of votes cats
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#import datetime
#now = datetime.datetime.now()
#print("The time right now is ", now)


# Assign a variable for the file to load and the path
file_to_load = '/Users/irinapreotescu/Desktop/Election-Analysis/Resources/election_results.csv'



#election_data= open(file_to_load, 'r')

#election_data.close()

#with open(file_to_load) as election_data:
    #print(election_data)

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    print(election_data)

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#open(file_to_save, "w")

# Using the with statement open the file as a text file
#outfile = open(file_to_save, "w")

# Write some data to the file.
#outfile.write("Hello World")

#Close the file
#outfile.close()

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Hello World! \nCounties in the Election\n--------------------")
    #Add 3 counties to the file
    txt_file.write("\nArapahoe\nDenver\nJefferson")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson.")


# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Extracting the candidate options
  #Create a new list
candidate_options = []

# Determine how many votes each candidate received
 # Create a new dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #for row in file_reader:
     #print(row)

#Read and print the header row.
    headers = next(file_reader)

# Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2] 

        # If the candidate name does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0 
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

#Save the results to a text file
with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end= "")
    #Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #And set the winning_candidate equal to the candidate's name
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
   

        
    




