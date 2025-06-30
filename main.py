import tkinter as tk
import random
from datetime import datetime
wlist = []
with open('words.txt', 'r') as file:
    for line in file:
        processed_line = line.strip()
        if (len(processed_line) > 2 and "'" not in processed_line):
            wlist.append(processed_line)
root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("500x500")

pressed= []
name = tk.StringVar()
typeval = tk.StringVar()

def raise_frame(frame):
    frame.tkraise()
counter = 5
start = datetime.now()
def handle_enter(e):
    print(pressed)
    typeentry.config(state=tk.DISABLED)
    typeentry.config(bg="lightgray")


def handle_change(e):
    global pressed
    pressed = list(" ".join(str(typeentry.get("1.0", "end")).split())) # prob not the most efficient solution but ok

def open_practice():
    global counter
    typeentry.config(bg="lightgray")
    counter = 5
    ranwords = [random.choice(wlist) for i in range(int(wlselected.get()[0:2]))]
    words.config(text=" ".join(ranwords))
    raise_frame(practicecontent)


    def count():
        global counter

        if counter >= 0:
            typeentry.config(state=tk.NORMAL)
            typeentry.delete('1.0', tk.END)
            typeentry.insert('1.0', "Starting in " + str(counter))
            typeentry.config(state=tk.DISABLED)
            counter -= 1
        if (counter == -1):
            typeentry.config(bg="white")
            typeentry.config(state=tk.NORMAL)
            typeentry.delete('1.0', tk.END)
        else:
            typeentry.after(1000, count)

    count()



practicecontent = tk.Frame(root, background="white", height=500, width=500)
practicecontent.pack_propagate(False)
practicecontent.pack()
practicecontent.place(x=0, y=0)
words = tk.Label(practicecontent, text="among us something here long words here something long here",
                 background="white", font=("Arial", 20), wraplength=300)
words.place(relx=0.5, rely=0.24, anchor="center", width=300)
typeentry = tk.Text(practicecontent,
                      font=('Arial', 15), borderwidth=2)
typeentry.place(relx=0.5, rely=0.51, anchor="center", width=300,height=100)
typeentry.config(state="disabled", wrap="word")
typeentry.bind('<Control-v>', lambda _: 'break')
typeentry.bind('<Control-c>', lambda _: 'break')
typeentry.bind('<BackSpace>', lambda _: 'break')
typeentry.bind("<Return>", handle_enter)
typeentry.bind('<KeyRelease>', handle_change)

maincontent = tk.Frame(root, background="white", height=500, width=500)
maincontent.pack_propagate(False)
maincontent.pack()
maincontent.place(x=0,y=0)
maincontent.tkraise()

wlselected = tk.StringVar()


title = tk.Label(maincontent, text="Pyper v0.3",
                 background="white", font=("Arial", 35))
title.place(relx=0.5, rely=0.13, anchor="center")
name_entry = tk.Entry(maincontent, textvariable=name,
                      font=('Arial', 15), borderwidth=2)
name_entry.insert(0, 'Guest')

name_entry.place(relx=0.5, rely=0.23, anchor="center")

wordlengths = tk.OptionMenu(maincontent, wlselected, 
                            *["10 words", "15 words", "25 words", "50 words"])
wordlengths.place(relx=0.5, rely=0.35, anchor="center", width=180)
wlselected.set("10 words")
# somehow we gotta use tkraise  -> DONe

practice = tk.Button(maincontent, text="Practice",
                     background="lightgray", font=("Arial", 16), command=open_practice)
practice.place(relx=0.5, rely=0.44, anchor="center", width=180, height=40)
compete = tk.Button(maincontent, text="Compete",
                     background="lightgray", font=("Arial", 16))
compete.place(relx=0.5, rely=0.53, anchor="center", width=180, height=40)
leaderboard = tk.Button(maincontent, text="Leaderboard",
                    background="lightgray", font=("Arial", 16))
leaderboard.place(relx=0.5, rely=0.62, anchor="center", width=180, height=40)
# Run the application
root.mainloop()







