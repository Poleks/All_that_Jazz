from tkinter import *
import random

keys = ["C", "G", "D", "A", "E", "B", "F#/Gb", "Db", "Ab", "Eb", "Bb", "F"]
step = [1, 2, 3, 4, 5, 6, 7]
cKey = ["Cmaj7", "Dm7", "Em7", "Fmaj7", "G7", "Am7", "Bm7b5"]
gKey = ["Gmaj7", "Am7", "Bm7", "Cmaj7", "D7", "Em7", "F#m7b5"]
dKey = ["Dmaj7", "Em7", "F#m7", "Gmaj7", "A7", "Bm7", "C#m7b5"]
aKey = ["Amaj7", "Bm7", "C#m7", "Dmaj7", "E7", "F#m7", "G#m7b5"]
eKey = ["Emaj7", "F#m7", "G#m7", "Amaj7", "B7", "C#m7", "D#m7b5"]
bKey = ["Bmaj7", "C#m7", "D#m7", "Emaj7", "F#7", "G#m7", "A#m7b5"]
fisKey = ["F#maj7", "G#m7", "A#m7", "Bmaj7", "C#7", "D#m7", "E#m7b5"]
dbKey = ["Dbmaj7", "Ebm7", "Fm7", "Gbmaj7", "Ab7", "Bbm7", "Cm7b5"]
abKey = ["Abmaj7", "Bbm7", "Cm7", "Dbmaj7", "Eb7", "Fm7", "Gm7b5"]
ebKey = ["Ebmaj7", "Fm7", "Gm7", "Abmaj7", "Bb7", "Cm7", "Dm7b5"]
bbKey = ["Bbmaj7", "Cm7", "Dm7", "Ebmaj7", "F7", "Gm7", "Am7b5"]
fKey = ["Fmaj7", "Gm7", "Am7", "Bbmaj7", "C7", "Dm7", "Em7b5"]

def answerx():
    chord = random.choice(step)
    chosenKey = random.choice(keys)
    label_question = Label(window, text=str(chosenKey) + " " + str(chord)).grid(row=2, column=0)

    answer = answer1.get()

    if answer == cKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == gKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == dKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == aKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == eKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == bKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == fisKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == dbKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == abKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == ebKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == bbKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer == fKey[chord - 1]:
        label_answer.config(text = "Right!")
    elif answer is None:
        label_answer.config(text = "Wrong!")
    else:
        label_answer.config(text = "Wrong!")

window = Tk()
window.title("XD")
window.geometry("300x300")

answer1 = Entry(window, width = 40)

label_answer = Label(window, text = "Your answer is:")
label_basicQuestion = Label(window, text = "Which chord is it?", padx = 3, pady = 10).grid(row = 0, column = 0)

exit_button = Button(window, text = "Exit", command = window.quit, padx = 3, pady = 10).grid(row = 1, column = 1)
check_button = Button(window, text = "Check", padx = 3, pady = 10, command = answerx())

label_answer.grid(row = 2, column = 1)
answer1.grid(row = 0, column = 1)
check_button.grid(row = 1, column = 0)

window.mainloop()
