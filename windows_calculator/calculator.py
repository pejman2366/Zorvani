import tkinter as tk
from functools import partial

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Windows Calculator")
        self.resizable(False, False)
        self.geometry("300x400")
        self.configure(bg="#f0f0f0")

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.display_var = tk.StringVar()
        display = tk.Entry(self, textvariable=self.display_var, font=("Segoe UI", 16), bd=10, insertwidth=2,
                            width=14, borderwidth=4, relief="ridge", justify="right")
        display.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            action = partial(self.on_button_click, text)
            tk.Button(self, text=text, width=6, height=2, font=("Segoe UI", 14), command=action).grid(row=row, column=col, padx=5, pady=5)

        tk.Button(self, text="C", width=6, height=2, font=("Segoe UI", 14), command=self.clear).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self, text="⌫", width=6, height=2, font=("Segoe UI", 14), command=self.backspace).grid(row=5, column=1, padx=5, pady=5)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except Exception:
            self.display_var.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
