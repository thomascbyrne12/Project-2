# Import Dependencies
import pandas as pd

# Read in data
cricket_data = pd.read_csv("C://Users//Thomas Byrne//Documents//GitHub//Project-2//icc-test-cricket-runs//ICC Test Batting Figures.csv", encoding="ISO-8859-1")

# Subsets of Table Data
high_scores = cricket_data[['Player', 'HS']]
total_runs = cricket_data[['Player', 'Runs']]
average = cricket_data[['Player', 'Avg']]
hundreds = cricket_data[['Player', '100', '50']]
ducks = cricket_data[['Player', '0']]

# Calculating the Career Length
cricket_data['Span1']=cricket_data['Span'].str[0:4]
cricket_data['Span2']=cricket_data['Span'].str[5:9]
career = year2 - year1
cricket_data['Career Length'] = career

# Creating the Career Length Subset
longest_career = cricket_data[['Player', 'Career Length']]
