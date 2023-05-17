# Education System
# pip install nltk
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')


def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [
        token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens


# Example usage
tokens = ['This', 'is', 'an', 'example', 'sentence', 'with', 'stop', 'words']
filtered_tokens = remove_stopwords(tokens)
print(filtered_tokens)
