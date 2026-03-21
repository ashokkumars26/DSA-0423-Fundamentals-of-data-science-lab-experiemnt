import numpy as np

# Fuel efficiency dataset (mpg)
fuel_efficiency = np.array([25, 30, 28, 35, 40])

# Average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Comparing two models
model1 = fuel_efficiency[0]
model2 = fuel_efficiency[4]

# Percentage improvement
percentage_improvement = ((model2 - model1) / model1) * 100

print("Average Fuel Efficiency:", average_efficiency, "mpg")
print("Percentage Improvement from Model1 to Model2:", percentage_improvement, "%")
