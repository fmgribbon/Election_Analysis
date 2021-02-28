#        *************
#        retrieve Data
#        *************
#  Add dependencies
#
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
 # Assign a  variable to save the from a path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")
                #open election results  using with statement
with open(file_to_load) as election_data:
                # To do: perform analysis.
                # Read the file object using the reader function.
    file_reader = csv.reader(election_data)
        #Read and print the header row
    headers = next(file_reader)
    print(headers)
#        *************
#         Close Data
#        *************
# election_data.close()