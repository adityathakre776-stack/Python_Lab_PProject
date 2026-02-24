# Countdown Clock and Timer (CS24066)
# Requirements: Python installed (Tkinter comes pre-installed)

import tkinter as tk
from tkinter import messagebox
import time
import threading

# For sound (Windows)
try:
    import winsound
    SOUND = True
except:
    SOUND = False


# ---- Countdown Logic ----
def start_timer():
    try:
        total_seconds = int(entry.get())
        if total_seconds <= 0:
            raise ValueError
    except:
        messagebox.showerror("Invalid Input", "Enter time in seconds")
        return

    # Run timer in separate thread so GUI doesn't freeze
    threading.Thread(target=countdown, args=(total_seconds,), daemon=True).start()


def countdown(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        label.config(text=time_format)
        time.sleep(1)
        seconds -= 1

    # Timer finished
    label.config(text="00:00")
    messagebox.showinfo("Time Up", "Countdown Finished!")

    if SOUND:
        winsound.Beep(1000, 1000)  # frequency, duration


# ---- GUI ----
root = tk.Tk()
root.title("Countdown Timer - CS24066")
root.geometry("300x200")
root.resizable(False, False)

title = tk.Label(root, text="Countdown Timer", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(root, justify="center", font=("Arial", 12))
entry.pack(pady=5)
entry.insert(0, "Enter seconds")

start_btn = tk.Button(root, text="Start Timer", command=start_timer)
start_btn.pack(pady=10)

label = tk.Label(root, text="00:00", font=("Arial", 24))
label.pack(pady=10)

root.mainloop()