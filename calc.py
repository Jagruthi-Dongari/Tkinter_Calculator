import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.resizable(False, True)

entry = tk.Entry(
    root,
    font=("Segoe UI", 20),
    bg="black",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=15)


def press(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calc():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

r = 1
c = 0

for btn in buttons:
    if btn == "=":
        action = calc
        btn_color = "red"
    elif btn in "+-*/.":
        action = lambda x=btn: press(x)
        btn_color = "red"
    else:  # Numbers
        action = lambda x=btn: press(x)
        btn_color = "light grey"

    tk.Button(
        root,
        text=btn,
        font=("Segoe UI", 14),
        width=5,
        height=2,
        bg=btn_color,
        fg="black",
        command=action
    ).grid(row=r, column=c, padx=5, pady=5)

    c += 1
    if c == 4:
        c = 0
        r += 1

tk.Button(
    root,
    text="C",
    font=("Segoe UI", 14),
    width=22,
    height=2,
    bg="yellow",
    fg="black",
    command=clear
).grid(row=r, column=0, columnspan=4, padx=5, pady=5)
root.mainloop()
