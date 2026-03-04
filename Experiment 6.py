import numpy as np

# Creating NumPy arrays
time = np.array([0, 1, 2, 3, 4, 5])
position = np.array([0, 15, 25, 30, 20, 5])

# Calculating total displacement
displacement = position[-1] - position[0]

# Calculating total time
total_time = time[-1] - time[0]

# Calculating average velocity
average_velocity = displacement / total_time

print("Average Velocity of the Projectile:", average_velocity, "m/s")
