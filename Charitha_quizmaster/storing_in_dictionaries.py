def To_dictionay():
    quesansdict={}
    # in this by reading txt file the data will be stored in dictionaries 
    # as keys as concepts names  
    # And values are tuple of list of ques and answers
    with open('Test.txt') as f:
        f.readline()
        for row in list(f.readlines()):
            oneques=row.split(',')
            if oneques[0] not in quesansdict.keys():
                quesansdict[oneques[0]]=[(oneques[1],oneques[2][:-1])]
            else:
                quesansdict[oneques[0]].append((oneques[1],oneques[2][:-1]))
    return quesansdict