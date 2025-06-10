import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 배열
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['휘발유', '경유', '=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == '휘발유':
            self.calculate_fuel_cost('gasoline')
        elif char == '경유':
            self.calculate_fuel_cost('diesel')
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate_fuel_cost(self, fuel_type):
        try:
            distance = float(self.expression)
            if fuel_type == 'gasoline':
                efficiency = 12   
                price_per_liter = 1547  
            else: 
                efficiency = 15   
                price_per_liter = 1397 

            liters_needed = distance / efficiency
            cost = round(liters_needed * price_per_liter)
            self.expression = str(cost)
        except:
            self.expression = "에러"
