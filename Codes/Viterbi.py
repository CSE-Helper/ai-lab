import re

# Language model (unigram probabilities)
language_model = {
    "the": 0.2,
    "longest": 0.1,
    "list": 0.05,
    "of": 0.07,
    "stuff": 0.03,
    "at": 0.08,
    "domain": 0.06,
    "name": 0.09,
    "last": 0.04,
    "com": 0.1
}


def segment_words(input_string):
    # Preprocess input string
    input_string = input_string.lower()
    # Remove non-alphabetic characters
    input_string = re.sub(r"[^a-z]+", "", input_string)

    # Viterbi algorithm for word segmentation
    n = len(input_string)
    best_scores = [0] * (n + 1)
    best_segments = [""] * (n + 1)

    for i in range(1, n + 1):
        best_score = float("-inf")
        best_segment = ""
        for j in range(i):
            current_word = input_string[j:i]
            current_score = best_scores[j] + \
                language_model.get(current_word, 0)
            if current_score > best_score:
                best_score = current_score
                best_segment = current_word

        best_scores[i] = best_score
        best_segments[i] = best_segments[i -
                                         len(best_segment)] + " " + best_segment

    segmented_words = best_segments[n].strip().split()
    return segmented_words


# Test the word segmentation
input_string = "thelongestlistofthelongeststuffatthelongestdomainnameatlonglastcom"
segmented_words = segment_words(input_string)
print(segmented_words)
