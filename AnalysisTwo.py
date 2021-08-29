import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
from IPython.display import display, HTML

nba_orig_df = pd.read_csv('nbaallelo.csv')
nba_orig_df = nba_orig_df[(nba_orig_df['lg_id']=='NBA') & (nba_orig_df['is_playoffs']==0)]
columns_to_keep = ['game_id','year_id','fran_id','pts','opp_pts','elo_n','opp_elo_n', 'game_location', 'game_result']
nba_orig_df = nba_orig_df[columns_to_keep]

# The dataframe for the assigned team is called assigned_team_df. 
# The assigned team is the Bulls from 1996-1998.
assigned_years_league_df = nba_orig_df[(nba_orig_df['year_id'].between(1996, 1998))]
assigned_team_df = assigned_years_league_df[(assigned_years_league_df['fran_id']=='Bulls')]
assigned_team_df = assigned_team_df.reset_index(drop=True)

display(HTML(assigned_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(assigned_team_df))

your_team_df = your_years_leagues_df[(your_years_leagues_df['fran_id']=="Thunder")]
your_team_df = your_team_df.reset_index(drop=True)

display(HTML(your_team_df.head().to_html()))
print("printed only the first five observations...")
print("Number of rows in the dataset =", len(your_team_df))


import scipy.stats as st

# Mean relative skill level of your team
mean_elo_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of your team in the years 2013 to 2015 =", round(mean_elo_your_team,2))


# Hypothesis Test
# ---- TODO: make your edits here ----
test_statistic, p_value = st.ttest_1samp(your_team_df['elo_n'],  1342)

print("Hypothesis Test for the Population Mean")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", round(p_value,4)) 

import scipy.stats as st

# Mean relative skill level of your team
mean_elo_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of your team in the years 2013 to 2015 =", round(mean_elo_your_team,2))


# Hypothesis Test
test_statistic, p_value = st.ttest_1samp(your_team_df['pts'],  110)

print("Hypothesis Test for the Population Mean")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", round(p_value,4)) 

if p_value < 0.01:
    print("Reject the null hypothesis")
else:
    print("Accept the null hypothesis")


#  

from statsmodels.stats.proportion import proportions_ztest

your_team_gt_80_df = your_team_df[(your_team_df['pts'] > 80)]

# Number of games won when your team scores over 80 points
counts = (your_team_gt_80_df['game_result'] == 'W').sum()

# Total number of games when your team scores over 80 points
nobs = len(your_team_gt_80_df['game_result'])

p = counts*1.0/nobs
print("Proportion of games won by your team when scoring more than 80 points in the years 2013 to 2015 =", round(p,4))


# Hypothesis Test
test_statistic, p_value = proportions_ztest(counts, nobs, p)

print("Hypothesis Test for the Population Proportion")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", round(p_value,4))

import scipy.stats as st

mean_elo_n_project_team = assigned_team_df['elo_n'].mean()
print("Mean Relative Skill of the assigned team in the years 1996 to 1998 =", round(mean_elo_n_project_team,2))

mean_elo_n_your_team = your_team_df['elo_n'].mean()
print("Mean Relative Skill of your team in the years 2013 to 2015  =", round(mean_elo_n_your_team,2))


# Hypothesis Test
# ---- TODO: make your edits here ----
test_statistic, p_value = st.ttest_ind(assigned_team_df['elo_n'],your_team_df['elo_n'])


print("Hypothesis Test for the Difference Between Two Population Means")
print("Test Statistic =", round(test_statistic,2)) 
print("P-value =", round(p_value,4))

