# XYZ company
# pip install nltk

from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')


def tokenize_comments(comment_text):
    words = word_tokenize(comment_text)
    return words


# Example usage
comment = "This new phone model is amazing!"
tokenized_words = tokenize_comments(comment)
print(tokenized_words)
['This', 'new', 'phone', 'model', 'is', 'amazing', '!']
