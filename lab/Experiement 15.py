import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Clinical trial data
control_group = np.array([45, 50, 48, 52, 47, 49, 51, 46])
treatment_group = np.array([55, 60, 58, 62, 57, 59, 61, 56])

# Perform t-test
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)

# Display p-value
print("P-value:", p_value)

# Calculate means
control_mean = np.mean(control_group)
treatment_mean = np.mean(treatment_group)

# Plot bar chart
groups = ['Control Group', 'Treatment Group']
means = [control_mean, treatment_mean]

plt.bar(groups, means)
plt.title("Clinical Trial Results")
plt.ylabel("Average Improvement Score")
plt.show()

# Interpretation
if p_value < 0.05:
    print("Result: The treatment has a statistically significant effect.")
else:
    print("Result: The treatment does not have a statistically significant effect.")
