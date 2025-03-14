from textblob import TextBlob   #used for sentiment analysis, spelling correction, part-of-speech tagging, and translation.
import nltk
from newspaper import Article  #used to extract and analyze the article


print(''' CHOOSE FROM THE MENU:
1. Analyze the sentiment of the text file
2. Analyze the sentiment of a news article from a URL     
''')

option_choosen = int(input("Enter the option: "))
if option_choosen == 1:
    print("You have choosen to Analyze the sentiment of the text file")
elif option_choosen == 2:
    print("You have choosen to Analyze the sentiment of a news article from a URL")
else:
    print("Invalid option choosen")
    exit()



def sentiment_analysis_from_text_file():
    #checking sentiment for text files

    #writing the text in the file

    with open("myfile.txt" , 'w+') as f:
        data = input("enter the text: ")
        f.write(data)

    #reading the text from the file

    with open("myfile.txt" , 'r') as f:
        text = f.read()
        if(text == ""):
            print("The file is empty","\n")
            exit()
        print("The text in the file is: ", text,"\n")

    blob = TextBlob(text)  #TextBlob allows easy text processing, including sentiment analysis.

    sentiment = blob.sentiment.polarity #-1 to 1 (negative to positive)
    print("The sentiment score is ", sentiment,"\n")


    if(sentiment>0):
        print("The sentiments in the file are Positive","\n")
    elif(sentiment<0):
        print("The sentiments in the file are Negative", "\n")
    else:
        print("The sentiments in the file are Neutral", "\n")


def sentiment_analysis_from_article():
    url = input("Enter the url of the article: ")
    if(url== ""):
        print("The url is not provided","\n")
        exit()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    text = article.summary
    print("The text in the file is ", text,"\n")
    blob = TextBlob(text)  #TextBlob allows easy text processing, including sentiment analysis.

    sentiment = blob.sentiment.polarity #-1 to 1 (negative to positive)
    print("The sentiment score is ", sentiment,"\n")


    if(sentiment>0):
        print("The sentiments in the article are Positive","\n")
    elif(sentiment<0):
        print("The sentiments in the article are Negative", "\n")
    else:
        print("The sentiments in the article are Neutral", "\n")


if(option_choosen == 1):
    sentiment_analysis_from_text_file()

elif(option_choosen == 2):
    sentiment_analysis_from_article()

