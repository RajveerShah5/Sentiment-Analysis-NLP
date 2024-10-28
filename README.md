# Sentiment-Emotion-Analysis-NLP

This repository contains a Python script for performing sentiment and emotion analysis on text data. The code reads text from a file, processes it to remove punctuation and stop words, performs tokenization, and then analyzes the sentiment and emotions within the text using the NLTK library. The results are visualized through bar charts for better interpretation.

## Features
- **Sentiment Analysis**: Determines if the text has positive, negative, or neutral sentiment.
- **Emotion Analysis**: Identifies the presence of specific emotions using a reference dictionary.
- **Data Visualization**: Creates bar charts to display sentiment and emotion distributions, saving them as images.

## Prerequisites
Make sure you have the following Python packages installed:
- `nltk`: Natural Language Toolkit for text processing and sentiment analysis.
- `matplotlib`: Used for plotting and visualizing the data.
- `collections`: Used for counting and processing emotion words.

How to Use
Prepare the Input Files:

Save the text you want to analyze in read.txt.
The emotions.txt file should contain emotion-word mappings in the format word:emotion.
The script generates two bar charts, one for sentiment analysis and one for emotion analysis. These are saved as graph.png.
Example Output
Sentiment Analysis: Shows the positive, negative, and neutral sentiment distribution in the text.
Emotion Analysis: Displays the frequencies of different emotions found in the text.
Issues & Contributing
Feel free to open an issue if you encounter any bugs or have suggestions for improvement. Contributions are welcome!
