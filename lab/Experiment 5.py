import numpy as np

# Creating NumPy array
student_scores = np.array([
    [85, 78, 92, 88],
    [75, 82, 79, 85],
    [90, 88, 84, 91],
    [70, 74, 80, 72],
    [88, 90, 86, 89],
    [92, 85, 88, 94],
    [76, 80, 75, 78],
    [84, 86, 90, 87],
    [89, 91, 87, 90],
    [73, 77, 72, 74],
    [95, 93, 96, 92],
    [68, 70, 65, 69],
    [82, 84, 81, 83],
    [78, 79, 77, 80],
    [91, 89, 94, 90]
])

subjects = ["Math", "Science", "English", "History"]

average_scores = np.mean(student_scores, axis=0)

highest_avg_index = np.argmax(average_scores)
highest_avg_subject = subjects[highest_avg_index]

print("Average Scores for Each Subject:")
for sub, avg in zip(subjects, average_scores):
    print(sub, ":", round(avg, 2))

print("\nSubject with Highest Average Score:", highest_avg_subject)
