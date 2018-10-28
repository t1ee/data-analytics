# PyBank Question 1
import pandas as pd
pybank = pd.read_csv("/Users/teresalee/Desktop/gitHub/HW/Python-Pandas/PyBank/budget_data.csv")
pybank = pybank["Date"].unique()
pybank.shape
# Answer: 86 months

# Question 2
pybank["Profit/Losses"].sum()
# Answer: 38382578

# Question 3










#PyPoll Question 1
import pandas as pd
pypoll = pd.read_csv("/Users/teresalee/Desktop/gitlab-data-analytics/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")
total_cast = pypoll["Voter ID"].count()
total_cast
# Answer: 3521001

# Question 2
pypoll["Candidate"].unique()
# Answer: ['Khan', 'Correy', 'Li', "O'Tooley"]

# Question 3
pypoll["Candidate"].value_counts()/total_cast*100
# Answer: 
# Khan        63.000011
# Correy      19.999994
# Li          13.999996
# O'Tooley     2.999999

# Question 3
pypoll["Candidate"].value_counts().head()

# Question 4
# Winnter is Khan with 63% of the votes

