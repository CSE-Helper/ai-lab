import nltk
from nltk.tokenize import TweetTokenizer


def tokenize_twitter_text(text):
    tokenizer = TweetTokenizer(
        preserve_case=False, strip_handles=True, reduce_len=True)
    tokens = tokenizer.tokenize(text)
    return tokens


# Example usage
twitter_text = "Feeling down today :( #depression"
tokens = tokenize_twitter_text(twitter_text)
print(tokens)
