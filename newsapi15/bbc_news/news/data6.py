import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load the data from CSV
df = pd.read_csv('articles.csv')

# Define the keywords to search for
keywords = ['COVID-19', 'vaccine', 'climate change', 'technology', 'politics', 'sports','science','health','entertainment']

# Combine the titles and summaries into a single column
df['text'] = df['title'] + ' ' + df['summary']

# Count the frequency of each keyword in the text column
counts = Counter()
for text in df['text']:
    for keyword in keywords:
        if keyword.lower() in str(text).lower():
            counts[keyword] += 1

# Plot a pie chart of the most popular topics
labels = [topic for topic, count in counts.most_common(5)]
sizes = [count for topic, count in counts.most_common(5)]
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Most Popular Topics in Articles')
plt.axis('equal')

# Display the chart
plt.show()

