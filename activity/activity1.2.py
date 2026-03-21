import pandas as pd
import matplotlib.pyplot as plt

# Sample sleep data (hours slept by students)
sleep_data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Avg_Sleep_Hours": [7, 6.5, 8, 5.5, 7.5]
}

df = pd.DataFrame(sleep_data)

# -------------------------------
# BAR CHART (Comparison)
# -------------------------------
plt.figure()
plt.bar(df["Student"], df["Avg_Sleep_Hours"])
plt.xlabel("Students")
plt.ylabel("Average Sleep Hours")
plt.title("Average Sleep Hours of Students")
plt.show()


# -------------------------------
# LINE CHART (7-day sleep pattern)
# -------------------------------

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
sleep_hours = [6, 7, 5.5, 6.5, 7, 8, 7.5]

plt.figure()
plt.plot(days, sleep_hours, marker='o')
plt.xlabel("Days")
plt.ylabel("Sleep Hours")
plt.title("Student A Sleep Pattern (7 Days)")
plt.show()
