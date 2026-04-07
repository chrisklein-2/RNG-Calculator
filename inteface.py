import tkinter as tk
from generate_rng import perform_calculation, print_results


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("RNG Calculator")
        self.root.geometry("600x260")

        # variables to store user input and results
        self.drop_rate = None
        self.kill_count = None
        self.result = None

        self.rng_text = "Enter an RNG value."
        self.kc_text = "Enter your current kill count."

        self.project_label = tk.Label(root, text="Assess how lucky you are with RNG drops.", font=("Helvetica", 12))
        self.project_label.pack(pady=10)
        
        # instruction label to guide user through input process
        self.instruction_label = tk.Label(root, text=self.rng_text, font=("Helvetica", 20))
        self.instruction_label.pack(pady=10)

        # entry field for RNG value input, with "1/" prefix to indicate the format of the input
        self.input_rng_frame = tk.Frame(root)
        self.input_rng_frame.pack(pady=5)
        prefix_label = tk.Label(self.input_rng_frame, text ="1/", font=("Helvetica", 12))
        prefix_label.pack(side=tk.LEFT)

        self.rng_entry = tk.Entry(self.input_rng_frame, width = 30)
        self.rng_entry.pack(pady=10)
        self.rng_entry.focus_set()

        # entry field for kill count input
        self.drop_rate_frame = tk.Frame(root)
        self.drop_rate_entry = tk.Entry(self.drop_rate_frame, width = 30)
        self.drop_rate_entry.pack()
        self.drop_rate_frame.pack(pady=5)

        # label to display results
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        # button for user to submit input, also binds the Enter key to the same function for convenience
        self.enter_button = tk.Button(root, text="Simulate", command=self.on_enter_button_click, width = 10)
        self.enter_button.pack(padx=100, pady=1)
        self.root.bind('<Return>', lambda event: self.on_enter_button_click())


    def on_enter_button_click(self):

        # gets focus of rng entry field 
        if self.root.focus_get() == self.rng_entry:
            try:
                self.drop_rate = int(self.rng_entry.get())
                self.result = perform_calculation(self.drop_rate)
                self.instruction_label.config(text=self.kc_text)
                self.drop_rate_entry.focus_set()
            except ValueError:
                self.result_label.config(text="Please enter a valid integer for the RNG value.")
                self.rng_entry.delete(0, tk.END)
        
        # gets focus of kc entry or button
        elif self.root.focus_get() == self.drop_rate_entry or self.root.focus_get() == self.enter_button:
            try:
                self.kill_count = int(self.drop_rate_entry.get())
                if self.drop_rate is None:
                    if self.rng_entry.get() == "":
                        self.result_label.config(text="Please enter the RNG value first.")
                        self.rng_entry.focus_set()
                        return
                    else:
                        self.drop_rate = int(self.rng_entry.get())
                        self.result = perform_calculation(self.drop_rate)
                
                # prints final result and resets variables for next calculation
                final_result = print_results(self.drop_rate, self.kill_count, self.result)
                self.result_label.config(text=final_result)                
                self.instruction_label.config(text=self.rng_text)
                self.rng_entry.focus_set()
                self.reset_variables()

            except ValueError:
                self.result_label.config(text="Please enter a valid integer for the kill count.")
                self.drop_rate_entry.delete(0, tk.END)
                self.drop_rate_entry.focus_set()
        
            
# resets variables and clears entry fields for next calculation
    def reset_variables(self):
        self.drop_rate = None
        self.kill_count = None
        self.result = None
        self.rng_entry.delete(0, tk.END)
        self.drop_rate_entry.delete(0, tk.END)