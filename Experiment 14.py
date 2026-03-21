import pandas as pd
import matplotlib.pyplot as plt
import string
from collections import Counter

# Load dataset
data = pd.read_csv("data.csv")

# Combine all feedback
text = " ".join(data['feedback'])

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Stop words list
stop_words = ['the', 'and', 'is', 'in', 'to', 'of', 'a', 'for', 'on', 'with', 'this']

# Split words
words = text.split()

# Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# Calculate frequency
word_freq = Counter(filtered_words)

# User input for top N words
N = int(input("Enter number of top frequent words: "))

# Get top N words
top_words = word_freq.most_common(N)

# Display results
print("Top", N, "Frequent Words:")
for word, freq in top_words:
    print(word, ":", freq)

# Plot bar graph
words = [w[0] for w in top_words]
freqs = [w[1] for w in top_words]

plt.bar(words, freqs)
plt.title("Top Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
