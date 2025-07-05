import tkinter as tk

# Global variables
running = False
counter = 0  # time in milliseconds

def update_time():
    global counter
    if running:
        minutes = counter // 6000
        seconds = (counter // 100) % 60
        milliseconds = counter % 100
        time_display = f"{minutes:02d}:{seconds:02d}:{milliseconds:02d}"
        label.config(text=time_display)
        counter += 1
        root.after(10, update_time)

def start():
    global running
    if not running:
        running = True
        update_time()

def pause():
    global running
    running = False

def reset():
    global counter, running
    running = False
    counter = 0
    label.config(text="00:00:00")

# GUI setup
root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x200")

label = tk.Label(root, text="00:00:00", font=("Arial", 40), pady=20)
label.pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(btn_frame, text="Start", width=8, command=start)
start_btn.grid(row=0, column=0, padx=5)

pause_btn = tk.Button(btn_frame, text="Pause", width=8, command=pause)
pause_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", width=8, command=reset)
reset_btn.grid(row=0, column=2, padx=5)

root.mainloop()
