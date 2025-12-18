import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Variable to store the current calculation
        self.current = "0"
        self.total = 0
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
    
    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="black")
        display_frame.pack(expand=True, fill="both")
        
        # Display label
        self.display = tk.Label(
            display_frame,
            text=self.current,
            anchor="e",
            bg="black",
            fg="white",
            font=("Arial", 20, "bold"),
            padx=10
        )
        self.display.pack(expand=True, fill="both")
    
    def create_buttons(self):
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")
        
        # Button layout
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']
        ]
        
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                if button_text == '':
                    continue
                
                # Special styling for different button types
                if button_text in ['C', '±', '%']:
                    bg_color = "#A6A6A6"
                    fg_color = "black"
                elif button_text in ['÷', '×', '-', '+', '=']:
                    bg_color = "#FF9500"
                    fg_color = "white"
                else:
                    bg_color = "#333333"
                    fg_color = "white"
                
                # Make 0 button span two columns
                if button_text == '0':
                    btn = tk.Button(
                        button_frame,
                        text=button_text,
                        bg=bg_color,
                        fg=fg_color,
                        font=("Arial", 18),
                        border=0,
                        command=lambda x=button_text: self.button_click(x)
                    )
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=1, pady=1)
                else:
                    btn = tk.Button(
                        button_frame,
                        text=button_text,
                        bg=bg_color,
                        fg=fg_color,
                        font=("Arial", 18),
                        border=0,
                        command=lambda x=button_text: self.button_click(x)
                    )
                    btn.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
        
        # Configure grid weights for responsive design
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def button_click(self, value):
        if self.result == True:
            self.current = "0"
            self.result = False
        
        if value in "0123456789":
            self.number_press(value)
        elif value == ".":
            self.decimal_press()
        elif value in "+-×÷":
            self.operation_press(value)
        elif value == "=":
            self.equals_press()
        elif value == "C":
            self.clear_press()
        elif value == "±":
            self.sign_press()
        elif value == "%":
            self.percent_press()
    
    def number_press(self, num):
        if self.input_value:
            self.current = num
            self.input_value = False
        else:
            if self.current == "0":
                self.current = num
            else:
                self.current += num
        self.display.config(text=self.current)
    
    def decimal_press(self):
        if self.input_value:
            self.current = "0."
            self.input_value = False
        elif "." not in self.current:
            self.current += "."
        self.display.config(text=self.current)
    
    def operation_press(self, op):
        if not self.check_sum:
            self.total = float(self.current)
            self.check_sum = True
        else:
            if not self.input_value:
                self.equals_press()
        
        self.op = op
        self.input_value = True
    
    def equals_press(self):
        if self.check_sum:
            try:
                if self.op == "+":
                    self.total += float(self.current)
                elif self.op == "-":
                    self.total -= float(self.current)
                elif self.op == "×":
                    self.total *= float(self.current)
                elif self.op == "÷":
                    if float(self.current) == 0:
                        messagebox.showerror("Error", "Cannot divide by zero!")
                        return
                    self.total /= float(self.current)
                
                # Format the result
                if self.total == int(self.total):
                    self.current = str(int(self.total))
                else:
                    self.current = str(self.total)
                
                self.display.config(text=self.current)
                self.check_sum = False
                self.input_value = True
                self.result = True
            except:
                messagebox.showerror("Error", "Invalid operation!")
    
    def clear_press(self):
        self.current = "0"
        self.total = 0
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        self.display.config(text=self.current)
    
    def sign_press(self):
        if self.current != "0":
            if self.current[0] == "-":
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
            self.display.config(text=self.current)
    
    def percent_press(self):
        try:
            self.current = str(float(self.current) / 100)
            self.display.config(text=self.current)
        except:
            messagebox.showerror("Error", "Invalid operation!")

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()