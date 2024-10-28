import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

text = open('read.txt', encoding='utf-8').read()  # reads the read.txt file
lower_case = text.lower()  # puts everything in lower case
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))  # removes punctuation gives spaces

# Using word_tokenize because it's faster than split()
tokenized_words = word_tokenize(cleaned_text, "english")

# Enhanced token list to account for negation
enhanced_tokens = []
negations = {"not", "no"}
negate = False

for word in tokenized_words:
    if word in negations:
        negate = True
    else:
        if negate:
            enhanced_tokens.append("not " + word)
            negate = False
        else:
            enhanced_tokens.append(word)
print(enhanced_tokens)
# Removing Stop Words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

final_words = []
for word in enhanced_tokens:
    if word == "no" or word == "not":
        final_words.append(word)
    if word not in stopwords.words('english'):
        final_words.append(word)

# Lemmatization - From plural to single + Base form of a word (example better-> good)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)

emotion_ref = {}
with open("emotions.txt") as f:
    for line in f:
       curr_emotion = line.replace("\n", '').replace(",", '').replace("'", '').strip()
       key, val = curr_emotion.split(':')
       emotion_ref[key] = val

emotion_list = []
keys_list = list(emotion_ref.keys())
for word in lemma_words:
    if word in keys_list:
        emotion = emotion_ref[word]
        print(emotion)
        emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

# Create a figure and axis object
fig, ax1 = plt.subplots(figsize=(10, 6))  # Adjust figsize as needed

# Plot the bar chart
bars = ax1.bar(w.keys(), w.values(), color='skyblue')  # Adjust color as needed

# Customize labels and titles
ax1.set_xlabel('X-axis Label')
ax1.set_ylabel('Y-axis Label')
ax1.set_title('Emotion Analysis of Free Response Questions')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add grid lines
ax1.grid(True)

# Optionally add some padding to the plot
plt.tight_layout()

# Save the plot to a file named 'graph.png'
plt.savefig('graph.png')

# Show the plot
plt.show()
