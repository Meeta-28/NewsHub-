import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('articles.csv')

# Convert the `created_at` column to a pandas datetime object
df['created_at'] = pd.to_datetime(df['created_at']).dt.tz_localize(None)

# Extract the hour from the `created_at` column
df['hour'] = df['created_at'].dt.hour

# Group articles by hour and count the number of articles per hour
counts = df['hour'].value_counts()

# Sort the counts by hour
counts = counts.sort_index()

# Create a bar chart
counts.plot(kind='bar')

# Set the title and axis labels
plt.title('Number of Articles Published by Hour')
plt.xlabel('Hour')
plt.ylabel('Number of Articles')

# Print the most popular publishing times
print('The most popular publishing times are:')
for hour, count in counts.nlargest(3).items():
    print(f'{hour}:00 - {hour+1}:00 ({count} articles)')
    
# Display the chart
plt.show()


