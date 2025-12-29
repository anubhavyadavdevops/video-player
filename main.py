import customtkinter as ctk
from app.gui.main_window import MainWindow

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = MainWindow()
    app.mainloop()
