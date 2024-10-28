import string
from collections import Counter
import matplotlib.pyplot as plt
import sns
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

text = open('read.txt', encoding='utf-8').read()  # reads the read.txt file
lower_case = text.lower()  # puts everything in lower case
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))  # removes punctuation gives spaces

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)

    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

    # Create a figure and axis object
    fig, ax1 = plt.subplots()

    # Plot the bar chart with a different color
    bars = ax1.bar(score.keys(), score.values(), color='lightgreen')  # Adjust color as needed

    # Customize labels and titles
    ax1.set_xlabel('X-axis Label')
    ax1.set_ylabel('Y-axis Label')
    ax1.set_title('Sentiment Analysis of Free Response Questions')

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

sentiment_analyse(cleaned_text)

