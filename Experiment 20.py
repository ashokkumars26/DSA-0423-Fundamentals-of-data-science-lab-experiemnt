import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("players.csv")

# Top 5 goal scorers
top_goals = df.sort_values(by='Goals', ascending=False).head(5)

# Top 5 highest salaries
top_salary = df.sort_values(by='Salary', ascending=False).head(5)

# Average age
avg_age = df['Age'].mean()

# Players above average age
above_avg = df[df['Age'] > avg_age]

# Count by position
position_count = df['Position'].value_counts()

# Display results
print("Top 5 Goal Scorers:\n", top_goals[['Name','Goals']])
print("\nTop 5 Highest Paid Players:\n", top_salary[['Name','Salary']])
print("\nAverage Age:", avg_age)
print("\nPlayers Above Average Age:\n", above_avg[['Name','Age']])

# Plot bar chart
position_count.plot(kind='bar')
plt.title("Player Distribution by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()
