import tkinter as tk
from controller import Controller
from model import Model

# ---------------- MAIN ------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Padaria VC++")
    root.geometry("600x500")
    root.configure(bg="white")

    model = Model()
    app = Controller(root, model)

    root.mainloop()