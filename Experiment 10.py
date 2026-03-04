import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [20, 22, 25, 30, 35, 33, 31, 30, 28, 26, 23, 21]
rainfall = [10, 15, 20, 25, 40, 120, 200, 180, 100, 50, 20, 15]



# Scatter Plot for Rainfall
plt.figure()
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall Data")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()
