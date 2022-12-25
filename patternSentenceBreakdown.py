"""
Doctests for get_partial_sentiment
the correct answers were obtained by checking each word and combination in get_total_sentiment

>>> thing = "the sun is shining very brightly"
>>> get_partial_sentiment(thing, get_total_sentiment(thing))
('very brightly', 0.91)

>>> thing1 = "I wish the whether was sunny, but it's actually pretty awful"
>>> get_partial_sentiment(thing1, get_total_sentiment(thing1))
('awful', -1.0)

>>> thing2 = "the weather today is not bad"
>>> get_partial_sentiment(thing2, get_total_sentiment(thing2))
('not bad', 0.35)

>>> thing3 = "I wish the weather was better than it is"
>>> get_partial_sentiment(thing3, get_total_sentiment(thing3))
('better', 0.5)

"""

from pattern.text.en import sentiment
from typing import List
from typing import Tuple
from typing import List


def get_total_sentiment(text: str) -> float:
    """
    returns the total sentiment of inputted text using pattern sentiment analysis
    :param text: strings of text with words
    :return: sentiment of text to three decimal places, can be between -1 and 1
    """
    compound = sentiment(text) # returns the sentiment and subjectivity as a tuple
    return round(compound[0], 3) # so we take compound[0] in order to get the sentiment

def get_partial_sentiment(text: str, total_sentiment: float) -> Tuple[str, float]:
    """
    takes in a string of text and its total sentiment and returns a tuple of
    if the total sentiment is negative: the one or two consecutive words with most negative sentiment and their sentiment value
    if the total sentiment is positive: the one or two consecutive words with most positive sentiment and their sentiment value
    if the total sentiment is neutral: an empty string and 0
    :param text: string of text with words
    :param total_sentiment: sentiment of text
    :return: tuple of 1-2 consecutive words contributing most to overall sentiment and the sentiment of those words
    """
    assert -1 <= total_sentiment <= 1, "invalid total sentiment value"
    # this is commented out to make the code run faster
    # assert total_sentiment == get_total_sentiment(text)

    # if the total sentiment is neutral
    if .05 > total_sentiment > -.05:
        return "", 0
    else:
        components = text.split() # split into words
        most_influential = components[0] # most influential starts as the first word
        most_influential_score = sentiment(components[0])[0] # most influential score starts as the sentiment of the first word

        # loop through each word
        for i in range(1, len(components)):
            score = sentiment(components[i])[0]

            # if the sentiment of that word is more positive or more negative (depending on the total sentiment
            # of the text), then make it the most_influential
            if abs(score) > abs(most_influential_score) and score * total_sentiment > 0:
                most_influential = components[i]
                most_influential_score = score

            # now score becomes the sentiment of that word and the one before it together
            score = sentiment(components[i-1: i+1])[0]

            # do the same checking process again
            if abs(score) > abs(most_influential_score) and score * total_sentiment > 0:
                most_influential = " ".join(components[i-1: i+1])
                most_influential_score = score

        return most_influential, round(most_influential_score, 3) # return most influential and its score

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Congratulations! You have passed all "+str(result[1])+" tests"))
    else:
        print("Rats!")



