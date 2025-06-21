import tkinter as tk
from controller import Controller
from model import Model

# ---------------- MAIN ------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Padaria VC++")
    root.geometry("700x600")
    root.configure(bg="white")


    model = Model()
    init = Controller(root, model)
    root.mainloop()
    