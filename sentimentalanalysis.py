from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity (range: -1 to 1)
    polarity = blob.sentiment.polarity
    
    # Determine the sentiment label
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example text for sentiment analysis
text = "I love this product. It's amazing!"

# Analyze the sentiment of the text
result = analyze_sentiment(text)

# Display the result
print(f"Sentiment: {result}")
