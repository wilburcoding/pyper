import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("500x500")


name = tk.StringVar()
typeval = tk.StringVar()

def raise_frame(frame):
    frame.tkraise()

def open_practice():
    raise_frame(practicecontent)
    



practicecontent = tk.Frame(root, background="white", height=500, width=500)
practicecontent.pack_propagate(False)
practicecontent.pack()
practicecontent.place(x=0, y=0)
title = tk.Label(practicecontent, text="among us something here long words here something long here",
                 background="white", font=("Arial", 20), wraplength=300)
title.place(relx=0.5, rely=0.24, anchor="center", width=300)
typeentry = tk.Text(practicecontent,
                      font=('Arial', 15), borderwidth=2)
typeentry.place(relx=0.5, rely=0.51, anchor="center", width=300,height=100)
typeentry.config(state="disabled")


maincontent = tk.Frame(root, background="white", height=500, width=500)
maincontent.pack_propagate(False)
maincontent.pack()
maincontent.place(x=0,y=0)
maincontent.tkraise()

title = tk.Label(maincontent, text="Pyper v0.3",
                 background="white", font=("Arial", 35))
title.place(relx=0.5, rely=0.13, anchor="center")
name_entry = tk.Entry(maincontent, textvariable=name,
                      font=('Arial', 15), borderwidth=2)
name_entry.insert(0, 'Guest')

name_entry.place(relx=0.5, rely=0.23, anchor="center")


# somehow we gotta use tkraise  -> DONe

practice = tk.Button(maincontent, text="Practice",
                     background="lightgray", font=("Arial", 16), command=open_practice)
practice.place(relx=0.5, rely=0.32, anchor="center", width=180, height=40)
compete = tk.Button(maincontent, text="Compete",
                     background="lightgray", font=("Arial", 16))
compete.place(relx=0.5, rely=0.41, anchor="center", width=180, height=40)
leaderboard = tk.Button(maincontent, text="Leaderboard",
                    background="lightgray", font=("Arial", 16))
leaderboard.place(relx=0.5, rely=0.50, anchor="center", width=180, height=40)
# Run the application
root.mainloop()







