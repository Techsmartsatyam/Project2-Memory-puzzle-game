import tkinter as tk
import random

root = tk.Tk()
root.title("Memory Puzzle Game")
root.geometry("520x650")

# Dummy card data (emoji based)
card_values = ["🐱","🚀","🍕","🐼","⚽","🐧","🦆","🏖️"] * 2
random.shuffle(card_values)

buttons = []
first = None
second = None
moves = 0
matches = 0
best_score = None

def on_click(btn, index):
    global first, second, moves
    
    if btn["state"] == "disabled" or second is not None:
        return

    btn.config(text=card_values[index], bg="white", fg="black")

    if first is None:
        first = (btn, index)
    else:
        second = (btn, index)
        moves += 1
        move_label.config(text=f"Moves: {moves}")
        root.after(600, check_match)

def check_match():
    global first, second, matches, best_score

    btn1, idx1 = first
    btn2, idx2 = second

    if card_values[idx1] == card_values[idx2]:
        btn1.config(state="disabled", bg="lightgreen")
        btn2.config(state="disabled", bg="lightgreen")
        matches += 1

        if matches == 8:
            result_label.config(text="🎉 You Won Bro Keep it up!")
            if best_score is None or moves < best_score:
                best_score = moves
                best_label.config(text=f" Wow Nice Best Score: {best_score}")
    else:
        btn1.config(text="?", bg="#1f4e79", fg="white")
        btn2.config(text="?", bg="#1f4e79", fg="white")

    first = None
    second = None

def restart_game():
    global card_values, moves, matches, first, second

    card_values = ["🐱","🚀","🍕","🐼","⚽","🐧","🦆","🏖️"] * 2
    random.shuffle(card_values)

    moves = 0
    matches = 0
    first = None
    second = None

    move_label.config(text="Moves: 0")
    result_label.config(text="")

    for btn in buttons:
        btn.config(text="?", bg="gray", fg="green", state="normal")

# Create grid
frame = tk.Frame(root)
frame.pack(pady=20)

for i in range(16):
    btn = tk.Button(frame, text="?", font=("Arial", 24),
                    width=4, height=2,
                    bg="#1f4e79", fg="white")
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    btn.config(command=lambda b=btn, i=i: on_click(b, i))
    buttons.append(btn)

move_label = tk.Label(root, text="Moves: 0", font=("Arial", 14))
move_label.pack()

best_label = tk.Label(root, text="Best Score: -", font=("Arial", 14))
best_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=10)

restart_btn = tk.Button(root, text="Restart Game", command=restart_game)
restart_btn.pack(pady=10)

root.mainloop()