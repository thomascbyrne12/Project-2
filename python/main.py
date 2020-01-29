# Import Dependencies
import pandas as pd

# Read in data
cricket_data = pd.read_csv("C://Users//Thomas Byrne//Documents//GitHub//Project-2//data//ICC Test Batting Figures.csv", encoding="ISO-8859-1")

# Subsets of Table Data
high_scores = cricket_data[['Player', 'HS']]
total_runs = cricket_data[['Player', 'Runs']]
average = cricket_data[['Player', 'Avg']]
hundreds = cricket_data[['Player', '100', '50']]
ducks = cricket_data[['Player', '0']]
longest_career = cricket_data[['Player', 'CareerLength']]
