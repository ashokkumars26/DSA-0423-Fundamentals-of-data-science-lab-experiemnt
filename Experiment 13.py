# Customer reviews dataset
reviews = [
    "this product is very good",
    "this product is good and useful",
    "very useful and good quality",
    "good product and good service"
]

# Combine all reviews
text = " ".join(reviews)

# Convert to lowercase
text = text.lower()

# Split into words
words = text.split()

# Dictionary to store frequency
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Display frequency distribution
print("Word Frequency Distribution:")
for word, count in word_freq.items():
    print(word, ":", count)
