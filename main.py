import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Data_preprocessing

# Import DataFrame
df_data = Data_preprocessing.import_data()
print(df_data)

st.title("Cars' Comparison")

# SelectBox to choose Continent
select_continent = st.multiselect("Please, select a continent :",
                                  df_data['continent'].unique(),
                                  df_data['continent'].iloc[0])
# Filter DataFrame with selected continent
if len(select_continent) == 0:
    st.write("Please, choose at least one continent")
else:
    df_filter = df_data[df_data['continent'].isin(select_continent)]

    # Graph with HeatMap
    st.subheader('HeatMap')
    heat_map = sns.heatmap(df_filter.corr(), cmap='PiYG', center=0, annot=True)
    st.pyplot(heat_map.figure, clear_figure=True)

    # Find parameters with high correlation
    dict_corr = {}
    list_columns = df_filter.select_dtypes(include=np.number).columns.to_list()

    for column in list_columns:
        column_corr = df_filter.corr()[column].abs()
        best_corr = column_corr[column_corr >= 0.7]
        dict_corr[column] = best_corr.index.to_list()
        dict_corr[column].remove(column)
    print(dict_corr)

    # Comments
    for column in list_columns:
        st.markdown(f'The parameter **{column}** is high correlated to {dict_corr[column]}')

    # Graph with distribution
    for column in list_columns:
        st.subheader(f'Distribution of {column}')
        violin_plot = sns.violinplot(data=df_filter, x=column, inner='box')
        st.pyplot(violin_plot.figure,
                  clear_figure=True)
