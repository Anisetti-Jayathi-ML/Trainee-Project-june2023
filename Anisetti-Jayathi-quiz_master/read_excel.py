import pandas as pd

def importFromGithub(url):
    df = pd.read_excel(url)
    return df