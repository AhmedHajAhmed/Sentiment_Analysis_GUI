from tkinter import *
from patternSentenceBreakdown import *
from typing import Tuple
from find_indices import find_indices


def myClick():
    """
    clicking on the button will print out the sentiment of the text as well as the text again with the important word(s)
    in red or green depending on their sentient
    :return:
    """
    # making it so that the text clears each time you press the button
    text.delete("1.0", END)

    # getting total sentiment of phrase
    total_sentiment = get_total_sentiment(e.get())

    # showing ouput
    text.insert(INSERT, "The sentiment analysis is: " + str(total_sentiment))
    text.insert(INSERT, f"\n{e.get()}")
    text.pack()

    # getting word(s) with most influential sentiment
    partial_sentiment = get_partial_sentiment(e.get(), total_sentiment)

    # get indices of influential words in order to know where to change color
    start_and_end = find_indices(e.get(), partial_sentiment[0])

    # depending on the sentiment the color should be different
    if partial_sentiment[1] > 0.05:
        color = "green"
    elif partial_sentiment[1] < -0.05:
        color = "red"
    else:  # do nothing if the sentiment is neutral
        color = "black"

    # change the color
    text.tag_configure("start", foreground=color)
    text.tag_add("start", f"2.{start_and_end[0]}", f"2.{start_and_end[1]}")

    # delete the placeholder text from the text box
    e.delete(0, END)


if __name__ == "__main__":
    # create the window and specify different features
    root = Tk()
    root.title("Sentiment Analysis GUI")
    root.config(bg="skyblue")
    root.geometry("450x350")
    root.maxsize(900, 600)
    root.geometry("500x300")
    left_frame = Frame(root, width=200, height=400, bg="grey")
    e = Entry(root, width=50, borderwidth=4)
    e.pack()
    text = Text(root)
    e.insert(0, "Enter some text")  # text in text box
    myButton = Button(root, text="Find Sentiment Analysis", command=myClick)  # button
    myButton.pack()
    root.mainloop()

def only_letters(P):
    if P.isdigit():
        return False
    return True



