# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 06:27:47 2022

@author: Owner
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches


df = pd.read_csv('WHO-COVID-19.csv')
print(df.head())

print('\n')

print(df.dtypes)
df['Cumulative_survival'] = df['New_cases'] - df['New_deaths']
df['Date_reported'] = pd.to_datetime(df['Date_reported'])



def lineplot(data, country_1, country_2) :
    
    """ This function's goal is to produce a line plot that compares two countries 
    that are influenced by COVID 19. Based on new cases, cumulative cases, new deaths, 
    cumulative deaths, and cumulative survival, the comparison is made.
    
    Args: 
        
        data (str) : A dataframe that has all the information required to create 
                    the plot.
        country_1 (str) : selected as the first country for comparison.
        
        country_2 (str) : selected as the second country for comparison. 
        
    Return: 
        
        A subplot of five graphs demonstrates how the pandemic has 
        affected both countries and how they have responded to it.
    """
    
    data_1 = data[data['Country'] == country_1] #
    data_1 = data_1.set_index('Date_reported')
    data_2= data[data['Country'] == country_2]
    data_2 = data_2.set_index('Date_reported')
    cols = []
    for col in data.columns: 
        if 'cases' in col or 'deaths' in col or 'survival' in col: 
            cols.append(col)    
    plt.figure(figsize = (15, 10))
    plt.subplots_adjust(hspace = 0.7, wspace = 0.7)
    country_a = mpatches.Patch(color='blue', label='{}'.format(country_1))
    country_b = mpatches.Patch(color='orange', label='{}'.format(country_2))
    for i in range (5): 
        plt.subplot(2, 3, i +1)
        plt.plot(data_1[cols[i]])
        plt.plot(data_2[cols[i]])
        plt.xlabel('Date')
        plt.ylabel('Covid19  {}'.format(cols[i]))
        plt.xticks(rotation = 90)
        plt.title('{} vs {} COVID19 {}'.format(country_1, country_2, cols[i]))
        plt.legend(handles=[country_a, country_b])
    plt.show()
    
    

def top_10_countries (data, col1, col2) : 
    """ This function's goal is to produce a bar plot of the top 10 countries 
        affected by COVID 19.
    
    Args: 
        
        data (str) : A dataframe that has all the information required to create 
                    the plot.
        col1 (str) : selected as the  country column.
        
        col2 (int) : selected as an interger or float column. 
        
    Return: 
        
        A bar plot that shows the top 10 countries.
    """
        
    country = data.groupby(col1)[col2].sum().reset_index()
    country = country.sort_values(by = col2,  ascending = False)
    country['column'] = country[col2] / 1000000
    print(country.head())
    fig, ax = plt.subplots()
    ax.barh(country['Country'][:10], country['column'][:10])
    plt.ylabel('{}'.format(col2))
    plt.xlabel('Countries')
    plt.title('Top 10 countries with the highest number of {}'.format(col2))
    plt.xticks(rotation = 90)
    plt.show()



def covid19_region (data, col1, col2 ): 
    """ This function's goal is to produce a pie plot of WHO region with respect 
    to the rate COVID 19  
    
    Args: 
        
        data (str) : A dataframe that has all the information required to create 
                    the plot.
        col1 (str) : selected as the first region.
        
        col2 (int) : selected as a column for covid 19 rate.. 
        
    Return: 
        
        A pie plot that shows the area or regions affected.
    """
    
    sizes = []
    label = []
    region = data.groupby(col1)[col2].sum().reset_index()
    for i in region[col1]: 
        label.append(i)
    for j in region[col2]: 
        sizes.append(j)
    explode = (0, 0.1, 0, 0, 0, 0, 0) 
    plt.figure()
    plt.pie(sizes, explode=explode, labels=label)
    plt.axis('equal')  
    plt.title('COVID 19 : {} by  {}'.format(col1, col2))
    plt.show()