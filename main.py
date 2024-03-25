from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"
card = {}

try:
    csv = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    csv = pandas.read_csv("data/hindi_words.csv")
finally:
    word_dict = csv.to_dict(orient='records')


def new_word():
    global card, timer
    window.after_cancel(timer)
    card = random.choice(word_dict)
    rand_hindi = card["Hindi"]
    canvas.itemconfig(card_title, text="Hindi", fill=BLACK)
    canvas.itemconfig(word_label, text=rand_hindi, fill=BLACK)
    canvas.itemconfig(front_card, image=front_flashcard_img)
    timer = window.after(3000, func=flip_card)


def is_known():
    word_dict.remove(card)
    new_word()
    df = pandas.DataFrame(word_dict)
    df.to_csv("data/words_to_learn.csv", index=False)


def flip_card():
    canvas.itemconfig(front_card, image=back_card_img)
    canvas.itemconfig(card_title, text="English", fill=WHITE)
    canvas.itemconfig(word_label, text=card["English"], fill=WHITE)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_flashcard_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
front_card = canvas.create_image(400, 263, image=front_flashcard_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="word", font=("Arial", 60, 'bold'), anchor=CENTER)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

new_word()

window.mainloop()
