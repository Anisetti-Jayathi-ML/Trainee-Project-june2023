import pandas as pd
import random

url = "https://raw.githubusercontent.com/Anisetti-Jayathi-ML/git_master/main/test.xlsx"


import read_excel
import list_topics
import generateQA

## to read excel sheet from github

df = read_excel.importFromGithub(url)

# to get list of topics

list_topics.listTopics(df)

# to get topic as input from user

n = int(input("Enter ur choice(number) : "))

# s = start , e = end
#range of question numbers for given topic

s = (n-1)*10
e = n*10-1

# to get no-of questions as input

q = int(input("no of questions : "))
marks = 0


for i in range(q):

    # to generate random questions

    marks += generateQA.generate_ques(s,e,df)

   
# to print solution

print("score = ",marks)









