import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("500x500")


name = tk.StringVar()




maincontent = tk.Frame(root, background="white", height=500, width=500)
maincontent.pack_propagate(False)
maincontent.pack()
title = tk.Label(maincontent, text="Pyper v0.3",
                 background="white", font=("Arial", 35))
title.place(relx=0.5, rely=0.13, anchor="center")
name_entry = tk.Entry(maincontent, textvariable=name,
                      font=('Arial', 15), borderwidth=2)
name_entry.insert(0, 'Guest')

name_entry.place(relx=0.5, rely=0.23, anchor="center")

practice = tk.Button(maincontent, text="Practice",
                     background="lightgray", font=("Arial", 16))
practice.place(relx=0.5, rely=0.32, anchor="center", width=180, height=40)
compete = tk.Button(maincontent, text="Compete",
                     background="lightgray", font=("Arial", 16))
compete.place(relx=0.5, rely=0.41, anchor="center", width=180, height=40)
leaderboard = tk.Button(maincontent, text="Leaderboard",
                    background="lightgray", font=("Arial", 16))
leaderboard.place(relx=0.5, rely=0.50, anchor="center", width=180, height=40)
# Run the application
root.mainloop()