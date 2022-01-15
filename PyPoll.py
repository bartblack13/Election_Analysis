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

# open and read election data
# load dependencies
import csv
import os

# variables and objects
# assign variable to load a file
file_to_load=os.path.join("Resources_mod3", "election_results.csv")
# assign variable to save a file    
file_to_save=os.path.join("analysis", "election_analysis.txt")
# 1. initialize a total vote counter
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results file and read
with open(file_to_load) as election_data:
    #to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    
    # #skip the first row or header row
    # next(file_reader)
    
    #read and print header row
    headers = next(file_reader)
    # print(headers)
    
    #print each row of csv file using for loop
    for row in file_reader:
        # print(row)
        # 2. Add to the total vote count
        total_votes += 1

        # 3. print the total votes
        ## print(total_votes)
        ## print(type(total_votes))
        ## print(f'The total votes are {total_votes:,}')
        # #pause and check data output

# count votes using accumulator with for loop and 
# new variable (total_votes) see above code to open file

# iterate through all rows and [make] list of candidate names see above
# use indexing with for loop with row variable (column 3 = index 2)
        
        # print the candidate name from each row
        candidate_name = row[2]
        # # add candidate name to candidate list
        # candidate_options.append(candidate_name)

        # print the candidate list
        # if the candidate name does not match any 
        # existing candidate on the output list...
        if candidate_name not in candidate_options:
            # ...add to list
            candidate_options.append(candidate_name)
            # ...count each candidate votes
            # begin tracking vote count at 0
            candidate_votes[candidate_name] = 0
            # incrementally add all the votes
        candidate_votes[candidate_name] += 1

        
# # determine the vote percentages for each candidate using a for loop
# for candidate_name in candidate_votes:
#     votes = candidate_votes[candidate_name]
#     vote_percentage = float(votes) / float(total_votes) * 100

# print the candidate list
print(f'\nThe candidates are as follows: \n{candidate_options}')
print(f'\nThe total votes are: \n{total_votes:,}')
print(f'\nThe votes for each candidate are as follows: \n{candidate_votes}\n')

# determine the vote percentages for each candidate using a for loop
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # print(f'{candidate_name}: received {vote_percentage:.2f}% of the vote.')
    # determine winner, winner votes, and winner %
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    print(f'{candidate_name}: received {vote_percentage:.1f}% of the total votes ({votes})')
print()

winning_candidate_summary = (
    f'-----------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'-----------------\n'
)
print(winning_candidate_summary)
# determine winner, winner vote counts, and winner percentage
# with for loop and if statement, see above (with code) for variables







    

