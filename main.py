import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("500x500")

# Top bar frame thingy
tbar = tk.Frame(root, background="white", height=40,width=500)
tbar.pack_propagate(False) 
tbar.pack()

# Create a label widget in the top bar

label = tk.Label(tbar, text="Pyper v0.3", background="white", font=("Arial", 20))
label.pack(side="left")

# Run the application
root.mainloop()
