# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:43:49 2019

@author: Jonathan
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime

 
date = str(input("Input Date in format ((Year-Month-Day): "))
year, month, day = map(int, date.split('-'))
filterdate = datetime.date(year, month, day)
       
url = 'https://www.espn.com/nba/player/gamelog/_/id/3948153/chris-boucher'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


columns=[
 'Date',
 'OPP',
 'Result',
 'MIN',
 'FG',
 'FG%',
 '3PT',
 '3P%',
 'FT',
 'FT%',
 'REB',
 'AST',
 'BLK',
 'STL',
 'PF',
 'TO',
 'PTS',
 ]

# create dataframe
d1 = pd.DataFrame(columns=columns)

months = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december',
]
other_keys = ['Averages', 'Totals']
all_keys = months + other_keys

full = []

for data in soup.find_all('td', attrs = {'class': 'Table__TD'}):
    val = data.get_text()
    full.append(val)
    
    # append None values for missing cols (opp and result)
    # summary of months, averages and totals
    if val in all_keys:
        full += [None, None]  #+= adds blank to full if val returns any of the values in all keys

# seperate full list into sub-lists with 17 elements
rows = [full[i: i+17] for i in range(0, len(full), 17)]

# append list of lists structure to dataframe
d1 = d1.append(pd.DataFrame(rows, columns=d1.columns))

#create new column with proper date
d1['New_Date'] = pd.to_datetime(d1['Date'].str.strip()+'/2019', errors='coerce')

#filter dates
d1 = d1[(d1['New_Date'] > filterdate) & (d1['New_Date'] != 'NaT')]

print(d1)
d1.to_csv('C:\\Users\\Jonathan\\test3.csv')

