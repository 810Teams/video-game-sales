"""
    PSIT Data Analysis Project
    CSV Updating Script
    by Teerapat Kraisrisirikul (810Teams)
"""

import pandas, numpy

def main():
    """ Main Function """
    titles = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher',
              'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales',
              'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Rating']

    db = numpy.array(pandas.read_csv('vgsales.csv')).tolist()
    db = [[i+1] + db[i] for i in range(len(db))]

    df = dict()
    for i in range(len(titles)):
        df[titles[i]] = [db[j][i] for j in range(len(db))]

    df = pandas.DataFrame(df, columns=titles)
    df.to_csv('vgsales_new.csv', index=False)

#main()
