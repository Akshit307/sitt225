import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df_cleaned = pd.read_csv('read.csv')

# Ensure 'Timestamp' is treated as a string and then convert it to a proper datetime format
df_cleaned['Timestamp'] = pd.to_datetime(df_cleaned['Timestamp'], format='%I:%M:%S %p.%f', errors='coerce')

# Drop any rows where the 'Timestamp' conversion failed
df_cleaned = df_cleaned.dropna(subset=['Timestamp'])

# Plot the X, Y, Z values over time
plt.figure(figsize=(10, 6))
plt.plot(df_cleaned['Timestamp'], df_cleaned['X'], label='X-axis', color='r')
plt.plot(df_cleaned['Timestamp'], df_cleaned['Y'], label='Y-axis', color='g')
plt.plot(df_cleaned['Timestamp'], df_cleaned['Z'], label='Z-axis', color='b')

# Add labels and title
plt.xlabel('Timestamp')
plt.ylabel('Acceleration')
plt.title('Acceleration in X, Y, Z over Time')
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
