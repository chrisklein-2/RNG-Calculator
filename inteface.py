import tkinter as tk

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Interface Example")
        
        self.label = tk.Label(master, text="Hello, World!")
        self.label.pack(pady=10)
        
        self.button = tk.Button(master, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)
    
    def on_button_click(self):
        self.label.config(text="Button Clicked!")