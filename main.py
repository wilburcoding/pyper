import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("500x500")

# Top bar frame thingy
tbar = tk.Frame(root, background="white", height=40,width=500)
tbar.pack_propagate(False) 
tbar.pack()
name = tk.StringVar()

label = tk.Label(tbar, text="Pyper v0.3", background="white", font=("Arial", 20))
label.pack(side="left")
name_bar = tk.Frame(root, background="lightgray", height=40, width=500)
name_bar.pack_propagate(False)
name_bar.pack()
dnamelabel = tk.Label(name_bar, text="Display Name: ",
                 background="lightgray", font=("Arial", 12))
dnamelabel.pack(side="left")
name_entry = tk.Entry(name_bar, textvariable=name,
                      font=('Arial', 12))
name_entry.place(relx=0.7, rely=0.5, anchor="center")
# Run the application
root.mainloop()