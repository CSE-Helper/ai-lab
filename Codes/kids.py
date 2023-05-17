# School Kids
# pip install nltk

from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')


def get_word_definition(word):
    synsets = wordnet.synsets(word)

    if synsets:
        # Retrieve the first synset
        synset = synsets[0]

        # Retrieve the definition and examples
        definition = synset.definition()
        examples = synset.examples()

        return definition, examples
    else:
        return None, None


# Example usage
word = "cat"
definition, examples = get_word_definition(word)
if definition and examples:
    print(f"Definition of '{word}': {definition}")
    print(f"Examples of '{word}':")
    for example in examples:
        print(f"- {example}")
else:
    print(f"No definition found for '{word}'")
