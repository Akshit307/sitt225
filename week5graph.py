import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('gyroscope_data.csv')

# Plot x, y, z individually
plt.figure(figsize=(10, 6))

# Plot x-axis
plt.subplot(3, 1, 1)
plt.plot(df['timestamp'], df['x'], label='x-axis')
plt.legend()

# Plot y-axis
plt.subplot(3, 1, 2)
plt.plot(df['timestamp'], df['y'], label='y-axis')
plt.legend()

# Plot z-axis
plt.subplot(3, 1, 3)
plt.plot(df['timestamp'], df['z'], label='z-axis')
plt.legend()

plt.show()

# Plot all axes together
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['x'], label='x-axis')
plt.plot(df['timestamp'], df['y'], label='y-axis')
plt.plot(df['timestamp'], df['z'], label='z-axis')
plt.legend()
plt.show()
