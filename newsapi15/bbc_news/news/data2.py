'''import pandas as pd
import matplotlib.pyplot as plt

# Load the article data from the CSV file
article_data = pd.read_csv('articles.csv', parse_dates=['created_at'])

# Group the articles by date and count the number of articles for each day
article_counts = article_data.groupby(article_data['created_at'].dt.date)['id'].count()

# Calculate the rolling average of article counts over a 7-day window
rolling_avg = article_counts.rolling(window=7).mean()

# Plot the article counts and rolling average
plt.plot(article_counts.index, article_counts.values, label='Article Count')
plt.plot(rolling_avg.index, rolling_avg.values, label='7-Day Rolling Average')
plt.title('Daily Article Count')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.legend()
plt.show()'''
'''import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('articles.csv')

# Group articles by source name and count the number of articles per source
counts = df.groupby('source_name').size().reset_index(name='counts')

# Sort by count in descending order and keep only top 10 sources
counts = counts.sort_values(by='counts', ascending=False).iloc[:10]

# Create a bar chart
plt.bar(counts['source_name'], counts['counts'])

# Set the title and axis labels
plt.title('Number of Articles per Source')
plt.xlabel('Source Name')
plt.ylabel('Number of Articles')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the chart
plt.show()'''
'''import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('articles.csv')

# Convert the `created_at` column to a pandas datetime object
df['created_at'] = pd.to_datetime(df['created_at']).dt.tz_localize(None)

# Group articles by date and source name and count the number of articles per date-source combination
counts = df.groupby([df['created_at'].dt.date, 'source_name']).size().reset_index(name='counts')

# Pivot the data to create a matrix with dates as rows and sources as columns
pivot = counts.pivot(index='created_at', columns='source_name', values='counts').fillna(0)

# Keep only the top 10 sources by article count
top_sources = pivot.sum().sort_values(ascending=False).head(10).index
pivot = pivot[top_sources]

# Create a bar chart
pivot.plot(kind='bar')

# Set the title and axis labels
plt.title('Number of Articles by Source over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')

# Display the chart
plt.show()'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('articles.csv')

# Convert the `created_at` column to a pandas datetime object
df['created_at'] = pd.to_datetime(df['created_at']).dt.tz_localize(None)

# Group articles by date and source name and count the number of articles per date-source combination
counts = df.groupby([df['created_at'].dt.date, 'source_name']).size().reset_index(name='counts')

# Pivot the data to create a matrix with dates as rows and sources as columns
pivot = counts.pivot(index='created_at', columns='source_name', values='counts').fillna(0)

# Keep only the top 10 sources by article count
top_sources = pivot.sum().sort_values(ascending=False).head(10).index
pivot = pivot[top_sources]

# Limit to the last 7 dates
last_7_dates = pivot.tail(7).index
pivot = pivot.loc[last_7_dates]

# Create a bar chart with a larger bottom length
ax = pivot.plot(kind='bar')

# Set the title and axis labels
ax.set_title('Number of Articles by Source over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Articles')

# Adjust the margins to avoid the dates getting cut off
plt.subplots_adjust(bottom=0.2)

# Display the chart
plt.show()








