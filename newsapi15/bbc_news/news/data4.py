import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
df = pd.read_csv('articles.csv')

# Group articles by source name and count the number of articles per source
counts = df['source_name'].value_counts().head(10)

# Create a pie chart
plt.pie(counts, labels=counts.index)

# Set the title
plt.title('Distribution of Articles Across Sources')

# Display the chart
plt.show()
