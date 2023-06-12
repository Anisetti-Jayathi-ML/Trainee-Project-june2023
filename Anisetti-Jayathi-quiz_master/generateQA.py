import random

def generate_ques(s,e,df):
 # to get random number in given range

    num = random.randint(s,e)

    # solution of question

    sol = (str(df["Answer"][num])).strip().lower()

    # to print question
    print(df["Question"][num])

    # to get answer from user

    ans = input().strip().lower()
   

    # to check if user input matches with given solution

    if(ans == sol):
        print("correct")
        print()
        return 1
        
    else:
        print("incorrect!")
        print("correct solution :",sol)
        print()
        return 0

    

