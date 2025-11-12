import tkinter as tk
import math

mode = "DEGREE"  # Default mode

def toggle_mode():
    global mode
    mode = "RADIAN" if mode == "DEGREE" else "DEGREE"
    mode_button.config(text=f"Mode: {mode}")

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            result = math.sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "log":
        try:
            result = math.log10(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text in ("sin", "cos", "tan"):
        try:
            angle = float(entry.get())
            if mode == "DEGREE":
                angle = math.radians(angle)
            func = getattr(math, text)
            result = func(angle)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("420x520")
root.title("Scientific Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

mode_button = tk.Button(root, text="Mode: DEGREE", font="Arial 12", command=toggle_mode)
mode_button.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "log"],
    ["1", "2", "3", "-", "sin"],
    ["0", ".", "=", "+", "cos"],
    ["C", "(", ")", "**", "tan"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 16", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()