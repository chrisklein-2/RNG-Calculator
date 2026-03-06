import tkinter as tk
from generate_rng import perform_calculation, print_results


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("RNG Calculator")
        self.root.geometry("400x200")


        self.drop_rate = None
        self.kill_count = None
        self.result = None

        self.project_label = tk.Label(root, text="Assess how lucky you are with RNG drops!")
        self.project_label.pack(pady=10)
        
        self.instruction_label = tk.Label(root, text="Enter an RNG value")
        self.instruction_label.pack(pady=10)

        self.entry = tk.Entry(root, width = 30)
        self.entry.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.button = tk.Button(root, text="Enter", command=self.on_button_click)
        self.button.pack(padx=100, pady=1)
        self.root.bind('<Return>', lambda event: self.on_button_click())

        
    def on_button_click(self):

        if self.instruction_label.cget("text") == "Enter an RNG value":
            self.drop_rate = int(self.entry.get())
            self.result = perform_calculation(self.drop_rate)
            self.entry.delete(0, tk.END)
            self.instruction_label.config(text="Enter your current kill count.")

        elif self.instruction_label.cget("text") == "Enter your current kill count.":
            self.kill_count = int(self.entry.get())
            final_result = print_results(self.drop_rate, self.kill_count, self.result)
            self.result_label.config(text=f"At {self.kill_count}/{self.drop_rate}\n{final_result:.2f}% of players received the drop")
            self.entry.delete(0, tk.END)
            self.instruction_label.config(text="Enter an RNG value")