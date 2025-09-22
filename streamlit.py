import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# sample data
income_df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\SENAPATI SIR FSDS NOTE\SEPTMBER MONTH DS NOTE\10th, 11th - Intro to Stats, Descriptive Stats\10th, 11th - Intro to Stats, Descriptive Stats\PROJECT\Inc_Exp_Data.csv")
income_df
#df = pd.DataFrame(data)

# Fuction to return selected plot
def generate_plot(plot_type):
    fig = plt.figure(figsize=(8,5))

    if plot_type == 'Histogram':
        income_df['Highest_Qualified_Member'].value_counts().plot(kind = 'bar')
    elif plot_type == 'Line Plot':
        income_df.plot(x = 'Mthly_HH_Income', y = 'Mthly_HH_Expense')
        IQR = income_df['Mthly_HH_Expense'].quantile(0.75)-income_df['Mthly_HH_Expense'].quantile(0.25)
    elif plot_type =='Scatter Plot':
        income_df.plot(x='Mthly_HH_Income', y='Mthly_HH_Expense', kind='scatter')
    elif plot_type == 'Bar plot':
        income_df['No_of_Earning_Members'].value_counts().plot(kind = 'bar')
    plt.tight_layout()
    return fig


demo.launch()
    
        

        

        
        

    
