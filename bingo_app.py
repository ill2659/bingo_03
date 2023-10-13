import random
import tkinter as tk
from tkinter import scrolledtext

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo Game")
        self.root.geometry("800x600") #ウインドウサイズ
        
        self.used_numbers = set()
        self.remaining_numbers = set(range(1, 76))
        self.past_numbers = []
        
        self.label = tk.Label(root, text="", font=("Arial", 50))
        self.label.pack(pady=20)
        
        self.past_label = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=30, height=10, font=("Arial", 20))
        self.past_label.pack()
        
        self.start_button = tk.Button(root, text="Next", command=self.pick_next_number, width=10, height=2,  bg="light sky blue", font=("Arial", 14, "bold"))
        self.start_button.pack(pady=10)
        
        self.check_bingo()
    
    def pick_next_number(self):
        if len(self.remaining_numbers) > 0:
            num = random.choice(list(self.remaining_numbers))
            self.remaining_numbers.remove(num)
            self.used_numbers.add(num)
            self.past_numbers.append(num)
            self.label.config(text=str(num))
            self.update_past_numbers()
            self.check_bingo()
        else:
            self.label.config(text="ビンゴは終了です")
            self.start_button.config(state=tk.DISABLED)
    
    def update_past_numbers(self):
        past_str = ",  ".join(map(str, self.past_numbers))
        self.past_label.delete(1.0, tk.END)  # 既存のテキストをクリア
        self.past_label.insert(tk.INSERT, f" {past_str}")
    
    def check_bingo(self):
        if len(self.used_numbers) == 75:
            self.label.config(text="ビンゴは終了です")
            self.start_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()
