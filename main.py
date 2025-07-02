import tkinter as tk
import random
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
wlist = []
with open('words.txt', 'r') as file:
    for line in file:
        processed_line = line.strip()
        if (len(processed_line) > 2 and "'" not in processed_line):
            wlist.append(processed_line)
root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("500x500")
ranlets = []
pressed = []
name = tk.StringVar()
typeval = tk.StringVar()


def raise_frame(frame):
    frame.tkraise()
slist = []
def return_home_from_practice(): # coming from practice ONLY -> may have to adjust to accept returning events from other places idk 
    global pressed
    global grouping
    global cgroup
    global cgcount
    global counter

    practicecontent.config(height=500, width=500)
    root.geometry("500x500")
    raise_frame(maincontent)
    words.place(relx=0.5, rely=0.24, anchor="center", width=300)
    typeentry.place(relx=0.5, rely=0.51, anchor="center", width=300, height=100)
    slist[0].get_tk_widget().destroy()
    for i in range(1, len(slist)):
        slist[i].destroy()
    pressed = [] #i think i needt his idk tho
    grouping = {}
    counter = 5
    cgroup = ""
    cgcount = 0
counter = 5
start = datetime.now()
grouping = {}
cgroup = ""
cgcount = 0
ltime = datetime.now()


def handle_enter(e):
    global pressed
    global slist
    print(pressed)
    print(grouping)
    typeentry.config(state=tk.DISABLED)
    typeentry.config(bg="lightgray")
    # list of amoutns of characters type (changed) for every group
    wpms = [60/((int(x.microseconds) + int(x.seconds) * 1000000) /
                1000000) * (2/5) for x in grouping.values()]
    print(wpms)
    practicecontent.config(height=500, width=1000)
    root.geometry("1000x500")
    words.config(text="Practice Results")
    words.config(font=('Arial', 26))
    words.place(relx=0.25, rely=0.05, anchor="center", width=300)
    typeentry.place(relx=0.25, rely=0.20, anchor="center",
                    width=300, height=100)
    fig = Figure(figsize=(4, 3),
                 dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.plot(wpms)
    canvas = FigureCanvasTkAgg(fig,
                               master=practicecontent)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.25, rely=0.62, anchor="center",
                                 width=450, height=250)
    slist.append(canvas)
    diff = datetime.now() - start
    wpmfull = (60/((int(diff.microseconds) + int(diff.seconds) * 1000000) /
                   1000000)) * (len(pressed)/5)
    print(wpmfull)
    wpmlabel = tk.Label(practicecontent, text=str(round(wpmfull, 2)) + " wpm",
                        background="white", font=("Arial", 25), wraplength=300)
    wpmlabel.place(relx=0.25, rely=0.35, anchor="center")
    practicecontent.config(height=500, width=1000)
    root.geometry("1000x500")
    bursts = [x for x in wpms if x >= (1.25 * (sum(wpms)/len(wpms)))]
    addinfo = tk.Label(practicecontent, text=f"Max burst wpm:{round(max(wpms),2)}\nAverage burst wpm:{round(sum(bursts)/len(bursts),2)}",
                       background="white", font=("Arial", 18), wraplength=500, justify="left")
    addinfo.place(relx=0.75, rely=0.15, anchor="center", width=400)
    btitle = tk.Label(practicecontent, text="Worst Letters",
                      background="white", font=("Arial", 18, "bold"), wraplength=500, justify="left")
    btitle.place(relx=0.75, rely=0.23, anchor="n", width=400)


    bestletters = {}
    for k, v in grouping.items():
        for let in list(k):
            if (let not in bestletters):
                bestletters[let] = [(int(v.microseconds) + int(v.seconds) * 1000000) /
                                    1000000]
            else:
                bestletters[let].append((int(v.microseconds) + int(v.seconds) * 1000000) /
                                        1000000)
    # sort bestletters
    bestletters = {k: v for k, v in sorted(bestletters.items(
    ), key=lambda item: (sum(item[1])/len(item[1])), reverse=True)}
    t = ""
    for i in range(4):
        avg = sum(list(bestletters.values())[i])/len(list(bestletters.values())[i])
        t += list(bestletters.keys())[i] + " - " + str(round(60 /
                                                 (avg) * (2/5),2)) + " wpm avg\n"
    blets = tk.Label(practicecontent, text=t,
                          background="white", font=("Arial", 16), wraplength=500, justify="left")
    blets.place(relx=0.75, rely=0.30, anchor="n", width=400)
    wtitle = tk.Label(practicecontent, text="Best Letters",
                      background="white", font=("Arial", 18, "bold"), wraplength=500, justify="left")
    wtitle.place(relx=0.75, rely=0.51, anchor="n", width=400)
    bestletters["\" \""] = bestletters[" "]
    del bestletters[" "]
    worstletters = {k: v for k, v in sorted(bestletters.items(
    ), key=lambda item: (sum(item[1])/len(item[1])))}
    t = ""
    for i in range(4):
        avg = sum(list(worstletters.values())[
                  i])/len(list(worstletters.values())[i])
        t += list(worstletters.keys())[i] + " - " + str(round(60 / (avg) * (2/5), 2)) + " wpm avg\n"
    wlets = tk.Label(practicecontent, text=t,
                     background="white", font=("Arial", 16), wraplength=500, justify="left")
    wlets.place(relx=0.75, rely=0.58, anchor="n", width=400)
    returnh = tk.Button(practicecontent, text="Return",
                         background="lightgray", font=("Arial", 16), command=return_home_from_practice)

    returnh.place(relx=0.75, rely=0.89, anchor="center", width=180, height=40)
    slist.append(btitle)
    slist.append(addinfo)
    slist.append(wpmlabel)
    slist.append(blets)
    slist.append(wtitle)
    slist.append(wlets)
    slist.append(returnh)

def handle_change(e):

    global cgcount
    global cgroup
    global grouping
    global pressed
    global typeentry
    global typeval
    global ltime
    if (str(typeentry.get("end-1c")) != "".join(pressed)):
        typeentry.delete('1.0', tk.END)
        typeentry.insert('1.0', "".join(pressed))
    val = str(e.keysym)  # get the last character typed
    if (val == "space"):
        val = " "
    if (len(pressed) >= len(ranlets)):
        return
    if (val == ranlets[len(pressed)]):
        typeentry.config(fg="black")
        pressed.append(val)
        cgcount += 1
        cgroup += val
        if (cgcount == 2):
            grouping[cgroup] = datetime.now() - ltime
            ltime = datetime.now()
            cgroup = ""
            cgcount = 0
        if (len(pressed) == len(ranlets)):
            typeentry.delete('1.0', tk.END)
            typeentry.insert('1.0', "".join(pressed))
            handle_enter(None)
    else:
        typeentry.config(fg="red")


def open_practice():
    global ranlets
    global counter
    global start
    global ltime

    typeentry.config(bg="lightgray")
    counter = 5
    ranwords = [random.choice(wlist)
                for i in range(int(wlselected.get()[0:2]))]
    if (wlselected.get()[0:2] == "50"):
        words.config(font=('Arial', 12))
    elif (wlselected.get()[0:2] == "25"):
        words.config(font=('Arial', 14))
    elif (wlselected.get()[0:2] == "15"):
        words.config(font=('Arial', 16))
    else:
        words.config(font=('Arial', 20))
    ranlets = list(" ".join(ranwords))
    words.config(text=" ".join(ranwords))
    print(ranlets)
    raise_frame(practicecontent)

    def count():
        global counter
        global start
        global ltime
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
            start = datetime.now()
            ltime = start
        else:
            typeentry.after(1000, count)
    count()


def start_practice():
    # Record new value of text widget every 100 milliseconds and save to grouping
    def record():
        global grouping
        grouping.append(str(typeentry.get("1.0", "end"))[:-2])
        typeentry.after(1000, record)
    record()


practicecontent = tk.Frame(root, background="white", height=500, width=500)
root.resizable(False, False)
practicecontent.pack_propagate(False)
practicecontent.pack()
practicecontent.place(x=0, y=0)
words = tk.Label(practicecontent, text="among us something here long words here something long here",
                 background="white", font=("Arial", 20), wraplength=300)
words.place(relx=0.5, rely=0.24, anchor="center", width=300)
typeentry = tk.Text(practicecontent,
                    font=('Arial', 15), borderwidth=2)
typeentry.place(relx=0.5, rely=0.51, anchor="center", width=300, height=100)
typeentry.config(state="disabled", wrap="word")
typeentry.bind('<Control-v>', lambda _: 'break')
typeentry.bind('<Control-c>', lambda _: 'break')
typeentry.bind('<BackSpace>', lambda _: 'break')
# typeentry.bind("<Return>", handle_enter)
typeentry.bind('<KeyPress>', handle_change)

maincontent = tk.Frame(root, background="white", height=500, width=500)
maincontent.pack_propagate(False)
maincontent.pack()
maincontent.place(x=0, y=0)
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
