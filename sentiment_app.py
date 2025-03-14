import streamlit as st
import nltk
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from newspaper import Article
from deep_translator import GoogleTranslator
from langdetect import detect,DetectorFactory
from textblob import TextBlob

# Ensure consistent language detection results
DetectorFactory.seed = 0

# Download required resources
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()


# Function to analyze sentiment
def analyze_sentiment(text):
    # Detecting language and translate if needed
    translator = GoogleTranslator(source="auto", target="en")
    detected_lang = translator.translate(text, target="en")  # GoogleTranslator auto-detects the language
    
    if detected_lang != text:  # If text is translated, show the translation
        st.write(f"**Translated from {text.upper()} to English:**","\n")
        st.write(f"{detected_lang}")

    # Performing sentiment analysis using TextBlob
    blob = TextBlob(detected_lang)  
    sentiment_score = blob.sentiment.polarity  # Sentiment polarity from -1 to 1



    if sentiment_score > 0:
        sentiment_label = "Positive "
    elif sentiment_score < 0:
        sentiment_label = "Negative "
    else:
        sentiment_label = "Neutral "

    return sentiment_score, sentiment_label



# Function to plot sentiment visualization
def plot_sentiment(sentiment_score):
    labels = ['Negative', 'Neutral', 'Positive']
    values = [max(0, -sentiment_score), 1-abs(sentiment_score), max(0, sentiment_score)]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['red', 'gray', 'green'])
    ax.set_title('Sentiment Analysis Results')
    ax.set_xlabel('Sentiments')
    ax.set_ylabel('Score')
    st.pyplot(fig)



# Streamlit Web App UI
st.title("Sentiment Analysis Web App")
st.subheader("Analyze Sentiment of Text or News Articles")



# Sidebar for selecting analysis type
option = st.sidebar.radio("Choose Analysis Type:", ["Analyzing Text", "Analyzing News Article"])

if option == "Analyzing Text":
    user_input = st.text_area("Enter text for sentiment analysis:")
    if st.button("Analyze"):
        if user_input.strip():
            score, sentiment = analyze_sentiment(user_input)
            st.success(f"**Sentiment Score:** {score:.2f}")
            st.info(f"**Overall Sentiment:** {sentiment}")
            plot_sentiment(score)
        else:
            st.warning("Please enter some text!")




elif option == "Analyzing News Article":
    url = st.text_input("Enter News Article URL:")
    if st.button("Analyze"):
        if url.strip():
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            text = article.summary

            st.subheader("Extracted Summary:")
            st.write(text)

            score, sentiment = analyze_sentiment(text)
            st.success(f"**Sentiment Score:** {score:.2f}")
            st.info(f"**Overall Sentiment:** {sentiment}")
            plot_sentiment(score)
        else:
            st.warning("Please enter a valid URL!")
