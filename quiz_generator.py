import re
from collections import Counter
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# クイズ生成関数
def kantan_quiz(input_text, entry):
    re_hiragana = re.compile("[ぁ-ゞ]+")
    if not re_hiragana.fullmatch(input_text):
        messagebox.showerror("エラー", "ひらがなで入力してください")
        return

    symbols = ["○", "▽", "□", "△", "◇", "☆", "●", "▼", "■", "▲", "◆", "★"]
    counts = Counter(input_text)
    mapping = {}
    result = ""
    symbol_index = 0

    for ch in input_text:
        if counts[ch] == 1:
            result += ch
        else:
            if ch not in mapping:
                mapping[ch] = symbols[symbol_index]
                symbol_index += 1
            result += mapping[ch]

    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
    return

# GUI部分
root = tk.Tk()
root.title("かんたんクイズ生成")

window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root)
frame.pack(expand=True)

label1 = ttk.Label(frame, text="答えとなる言葉をひらがなで入力")
label1.grid(row=0, column=0)

entry1 = ttk.Entry(frame, width=40)
entry1.grid(row=1, column=0)

label2 = ttk.Label(frame, text="↓")
label2.grid(row=3, column=0)

entry2 = ttk.Entry(frame, width=40)
entry2.grid(row=4, column=0)

button = ttk.Button(frame, text="生成", command=lambda: kantan_quiz(entry1.get(), entry2))
button.grid(row=2, column=0)

root.mainloop()
