from pattern.text.en import sentiment

thing = "I dislike coffee"

print(sentiment(thing))
for word in thing.split():
    print(f"{word}: {sentiment(word)}")

print(sentiment("very grey"))