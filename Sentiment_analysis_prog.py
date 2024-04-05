import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK's VADER lexicon for sentiment analysis
# nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis on a given text
def analyze_sentiment(text):
    # Get sentiment scores
    sentiment_scores = sid.polarity_scores(text)
   
    # Classify sentiment based on compound score
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Get input from the user
text = input("Enter the text you want to analyze: ")

# Perform sentiment analysis
sentiment = analyze_sentiment(text)
print("Sentiment:", sentiment)

# Get input from the user
text2 = input("\nEnter the text you want to analyze: ")

# Perform sentiment analysis
sentiment2 = analyze_sentiment(text2)
print("Sentiment:", sentiment2)
