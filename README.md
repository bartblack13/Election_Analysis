# Election_Analysis
python and VS coder

## Overview of Election Audit: Explain the purpose of this election audit analysis.
The purpose of this project was to gain familiarity with using Python, an object oriented programming language, to analyze data sets.  For this project, I analyzed a csv file (Election_Results.csv) that contained 369,711 rows of election data, including: ballot ID; county where the vote was cast, and the candidate for whom the vote was cast.  In order to do this, I used VS coder to write and execute my code, to automatically open and analyze my file, and to also automatically save the generated analysis outputs to a text file (election_analysis.txt).  The analysis outputs were also printed to the terminal window in VS Coder, and viewed in the text file window.  Screen shots of both the terminal outputs and the text file windows can be seen below, and the text file is listed in my Election_Analysis repository.

This project is part of my Week 3 DU Coding Bootcamp classwork, and included:
* Running a Python file in the command line or VS Code;
* Performing Calculations;
* Creating and add to a list;
* Creating and add keys and values to a dictionary;
* Using decision statements to check a condition;
* Applying membership and logical operators to decision statements;
* Using repetition statements to iterate through a list or dictionary;
* Writing print statements using f-strings, and format objects, like intergers or floating decimals;
* Opening csv files, and saving outputs to text files

## Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
* How many votes were cast in this congressional election?<br />
    369,711 votes were cast.
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.<br />
     County Votes (county, percentage of total votes, votes by county):<br />
    Jefferson: 10.5% (38,855)<br />
    Denver: 82.8% (306,055)<br />
    Arapahoe: 6.7% (24,801)<br />
* Which county had the largest number of votes?<br />
    Largest County Turnout: Denver
* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.<br />
    (candidate, percentage of total votes, number of votes)<br />
    Charles Casper Stockham: 23.0% (85,213)<br />
    Diana DeGette: 73.8% (272,892)<br />
    Raymon Anthony Doane: 3.1% (11,606)<br />
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?<br />
    Winner: Diana DeGette<br />
    Winning Vote Count: 272,892<br />
    Winning Percentage: 73.8%<br />
    
See below for pictures of outputs.


![This is an image](https://github.com/bartblack13/Election_Analysis/blob/main/analysis/election_analysis%20terminal%20view.png)<br /> 
Figure 1: voting results printed to terminal<br /> <br /> 


![This is an image](https://github.com/bartblack13/Election_Analysis/blob/main/analysis/election_analysis%20txt_file.write%20view.png)<br /> 
Figure 2: voting results saved to text file<br /> <br /> 

## Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

Although the the script used to generate the above results was written for a specific file with specific variables, if the election commission is interested, the code could be modified to run different data set files.  For example, the code could be modified to ask the user which file should be run, by using the input() function.  Since this might require the user to specify the folder path, indirect or direct, an easier method would be to ask the user for the file name, which would automatically update the file path.  Assuming that the data is in the same format in each file (same columns and same info per column), and assuming that the new files are in the same folder as the initial "election_results" file, the input function would create a new file_to_load variable, and then the f-string function nested in the file path scipt would autoload that file name into the script to open the file.  In the picture below, you can see the old code (commented out in green) and the new code, including the new variable and input function.  The modified code, as shown below was 100% functional and successfully genearated the same data outputs as origincal code. 

![This is an image](https://github.com/bartblack13/Election_Analysis/blob/main/analysis/edited%20code%20option1.png)<br /> 
Figure 3:<br /> <br /> 

**old code:**<br /> 
file_to_load = os.path.join("Resources_mod3", "election_results.csv")

**new code:**<br />
desired_file_to_analyze = str(input("Enter the name of the file you wish to analyze.\n"))<br />
file_to_load = os.path.join("Resources_mod3", f"{desired_file_to_analyze}.csv")


Many elections, especially at the local level, have propositions that are being voted on, with a simple yes-no vote, which would be included on the same ballot, and listed in its own column in the data set.  Copying the code with updated column index number and new vairable names would allow the new column of info to be analyzed and used to indicate whether or not the proposition passed or failed, for example.  

This might look like the following:

![This is an image](https://github.com/bartblack13/Election_Analysis/blob/main/analysis/edited%20code%20option2.png)<br /> 
Figure 4:<br /> <br /> 

Another option might be to combine a for loop, an if statement, and the count function to count all values within a column that are "yes" votes, where: yes = true.  This option would require me to experiment with the script, but in theory should work.




