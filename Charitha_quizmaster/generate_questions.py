import random
# In this the random questions are generated accessing from the ques and ans dict
def random_questions(quesansdict,concept):
    concept_ques_list=quesansdict[concept]
    l=[]
    for i in range(len(concept_ques_list)):
        l.append(i)
    random_ques = random.sample(l,5)
    score = 0
    quesnum = 1
    index= 0
    for question, correct_answer in concept_ques_list:
        if index in random_ques:
            print(quesnum, end = '.')
            answer = input(f"{question}? ")
            if answer.strip() == correct_answer.strip():
                print("Correct!")
                score+=1
            else:
                print(f"The answer is {correct_answer!r}, not {answer!r}")
            quesnum+=1
        index+=1
    print('your total score is:', score)