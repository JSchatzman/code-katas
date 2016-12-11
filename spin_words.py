"""Spin Words."""


def spin_words(sentence):
    """Return input string with reversed words with length >= 5."""
    split_words = sentence.split(' ')
    reverse_words = [word[::-1] if len(word) >= 5 else word for word in split_words]
    return ' '.join(reverse_words)
