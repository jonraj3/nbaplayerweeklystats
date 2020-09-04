# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:00:21 2020

@author: Jonathan
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import MultiComparison
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import math

#Current Year, 2020
#url = 'https://www.espn.com/nba/player/gamelog/_/id/3012/kyle-lowry'

#2019
url = 'https://www.espn.com/nba/player/gamelog/_/id/3012/type/nba/year/2019'

#2018
#url = 'https://www.espn.com/nba/player/gamelog/_/id/3012/type/nba/year/2018'


soup = BeautifulSoup(requests.get(url).content, 'html.parser')
columns = ['Date','OPP','Result','MIN','FG','FG%','3PT','3P%','FT','FT%','REB','AST','BLK','STL','PF','TO', 'PTS']

all_data = []
for row in soup.select('.Table__TR'):
    tds = [td.get_text(strip=True, separator=' ') for td in row.select('.Table__TD')]
    if len(tds) != 17:
        continue
    all_data.append(tds)

df = pd.DataFrame(all_data, columns=columns)
