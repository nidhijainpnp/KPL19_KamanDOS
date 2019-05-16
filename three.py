import pandas as pd
from operator import itemgetter


def func():
    df = pd.read_csv("data.csv")

    ra= []
    for i in range(274):
        ra.append((df.loc[:, "Column 10"][i], df.loc[:, "Column 1"][i]))
    
    ra = sorted(ra, key=itemgetter(0))

    return ra[-6:]
