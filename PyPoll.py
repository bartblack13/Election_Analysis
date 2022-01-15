# output goals
# # find total number of votes
# list of canditdates who received votes
# total number of votes per candidtate
# % of votes per candidate
# winner

# import datetime
# now = datetime.datetime.now()
# print("The time right now is ", now)

#open elctions_result.csv file
# file_to_load = 'Resources_mod3/election_results.csv'
# with open(file_to_load) as election_data:
#     print(election_data)
    
# #indirect path
# import csv
# import os
# file_to_load = os.path.join("Resources_mod3", "election_results.csv")
# with open(file_to_load) as election_data:
#     print(election_data)


# #writing a file
# import csv
# import os
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# outfile= open(file_to_save,"w")
# outfile.write("Hello World")
# outfile.close()

# import csv
# import os
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election")
#     txt_file.write("\nArapahoe, \nDenver, \nJefferson")

#open and read election data
#load dependencies
import csv
import os
#assign variable to load a file
file_to_load=os.path.join("Resources_mod3", "election_results.csv")
#assign variable to save a file    
file_to_save=os.path.join("analysis", "election_analysis.txt")
#open the election results file and read
with open(file_to_load) as election_data:
    #to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    #print each row of csv file using for loop
#     for row in file_reader:
#         print(row)
# #pause and check data output
# #skip the first row or header row
# next(file_reader)
    #read and print header row
    # headers = next(file_reader)
    # print(headers)

