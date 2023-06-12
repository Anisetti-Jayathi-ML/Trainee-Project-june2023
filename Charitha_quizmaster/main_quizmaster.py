# Name :P Charitha
# emplo no: 10419
# We can also do this using dataframes I used dictionaries for accessing 

import excel_data
import storing_in_dictionaries
import generate_questions
# URL of the raw Excel file on GitHub
github_excel_url = "https://raw.githubusercontent.com/Anisetti-Jayathi-ML/git_master/main/test.xlsx"
excel_data.access_and_convert_to_textfile(github_excel_url)
quesansdict = storing_in_dictionaries.To_dictionay()

# show the concepts that are exist using the dictionaries that is having the data in the excel sheet
print('select one concept?')
for i in quesansdict:
    print(i)
concept=input()

# check whether the concept exist in excel or not 
if concept in quesansdict:
    # calling to the questions function by giving the concept
    generate_questions.random_questions(quesansdict,concept)
else:
    print('Enter the existing concept')