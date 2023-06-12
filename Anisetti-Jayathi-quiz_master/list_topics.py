def listTopics(df):

    # to get list of topics

    topics = list(set(df["Topic"]))

    # to list out all topics

    print("select a topic")
    for i in range(0,len(topics)):
        print(i+1,". ",topics[i])