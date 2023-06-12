import pandas as pd
def access_and_convert_to_textfile(github_excel_url):
    df = pd.read_excel(github_excel_url)
    # the excel data accessed and converted to text file and 
    # it is saved as Test.txt in the location
    df.to_csv ("Test.txt",
                    index = None,
                    header=True)