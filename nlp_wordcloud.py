# nlp_wordcloud.py

# Importing libraries
from wordcloud import WordCloud
from PIL import Image
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np
import re

# Ensure you have the necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('vader_lexicon')


# Function to read and clean movie lines
def read_movie_lines(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    # Extract dialogues
    dialogues = [line.split(' +++$+++ ')[-1].strip() for line in lines]
    return ' '.join(dialogues)


# Clean text by removing special characters and digits
def clean_text(text):
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text


# Read and clean the movie lines
text_data = read_movie_lines('movie_lines.txt')
cleaned_text = clean_text(text_data)

# Tokenize text
tokens = word_tokenize(cleaned_text)

# Remove stopwords
stopwords_set = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stopwords_set]

# Recombine text for word cloud
filtered_text = ' '.join(filtered_tokens)


# Function to generate word cloud
def generate_wordcloud(mask_image_path, title):
    mask_img = np.array(Image.open(mask_image_path))
    word_cloud = WordCloud(width=1000, height=500, background_color='white', stopwords=stopwords_set, mask=mask_img,
                           contour_color='black', contour_width=0.1).generate(filtered_text)

    # Display word cloud
    plt.figure(figsize=(10, 10))
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()


# Generate word clouds with different masks
generate_wordcloud('assets\\butterfly.webp', 'Word cloud in butterfly')
generate_wordcloud('assets\\car.webp', 'Word cloud in car')
generate_wordcloud('assets\\dog.webp', 'Word cloud in dog')
generate_wordcloud('assets\\tower.jpg', 'Word cloud in eiffel tower')
generate_wordcloud('assets\\tree.jpg', 'Word cloud in tree')

# Part of Speech Tagging
tagged_tokens = nltk.pos_tag(filtered_tokens)
print("Part of Speech Tagging:")
print(tagged_tokens[:10])  # Print the first 10 tagged tokens for inspection

# Named Entity Recognition
ner_chunks = nltk.ne_chunk(tagged_tokens)
print("\nNamed Entity Recognition:")
print(ner_chunks)

# Sentiment Analysis
sid = SentimentIntensityAnalyzer()
sentiment_scores = sid.polarity_scores(filtered_text)
print("\nSentiment Analysis:")
print(sentiment_scores)
