# The Data We Need to Retrieve:
# 1. The total number of votes cats
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#import datetime
#now = datetime.datetime.now()
#print("The time right now is ", now)


# Assign a variable for the file to load and the path.
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

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#open(file_to_save, "w")

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")

# Write some data to the file.
#outfile.write("Hello World")

#Close the file
#outfile.close()

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Hello World! \nCounties in the Election\n--------------------")
    #Add 3 counties to the file
    txt_file.write("\nArapahoe\nDenver\nJefferson")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson.")


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #for row in file_reader:
     #print(row)

#Read and print the header row
    headers = next(file_reader)
    print(headers)

# Print each row in the CSV file
#file_reader = csv.reader(election_data)
#for row in file_reader:
    #print(row)
