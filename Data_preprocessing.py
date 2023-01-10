import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def import_data():
    df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

    # delete space and dot for continent
    df['continent'] = df['continent'].str.strip('. ')

    return df


