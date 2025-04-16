import tkinter as tk
import os

def create_window():
    def calculate_time_ms():
        nonlocal countdown_seconds, countdown_running
        hours = int(hour_spinbox.get())
        minutes = int(minute_spinbox.get())
        total_ms = (hours * 60 * 60 * 1000) + (minutes * 60 * 1000)
        countdown_seconds = total_ms // 1000
        countdown_running = True
        pause_button.config(state="normal", text="Pause")
        stop_button.config(state="normal")
        if total_ms > 0:
            start_countdown()
        else:
            timer_label.config(text="Insert a desired time")

    def start_countdown():
        nonlocal countdown_id, countdown_seconds, countdown_running
        if countdown_running and countdown_seconds >= 0:
            hrs = countdown_seconds // 3600
            mins = (countdown_seconds % 3600) // 60
            secs = countdown_seconds % 60
            timer_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
            countdown_seconds -= 1
            countdown_id = root.after(1000, start_countdown)
        elif countdown_seconds < 0:
            timer_label.config(text="Shutting Down...")
            os.system("shutdown /s /t 0")

    def pause_resume_timer():
        nonlocal countdown_running
        if countdown_running:
            countdown_running = False
            root.after_cancel(countdown_id)
            pause_button.config(text="Resume")
        else:
            countdown_running = True
            pause_button.config(text="Pause")
            start_countdown()

    def stop_timer():
        nonlocal countdown_running, countdown_seconds
        countdown_running = False
        countdown_seconds = 0
        root.after_cancel(countdown_id)
        timer_label.config(text="Cancelled")
        pause_button.config(state="disabled")
        stop_button.config(state="disabled")

    root = tk.Tk()
    root.title("Shutdown Planner")

    # 🌓 Dark theme colors
    bg_color = "#2e2e2e"
    fg_color = "#ffffff"
    a_color = "#00aaff"
    button_bg = "#3c3c3c"
    accent_color = "#00aaff"

    font_style = ("Segoe UI", 12)
    large_font = ("Segoe UI", 20)

    root.configure(bg=bg_color)
    window_width = 360
    window_height = 420

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    title = tk.Label(root, text="Shutdown Planner", font=("Segoe UI", 16, "bold"), bg=bg_color, fg=accent_color)
    title.pack(side="top", pady=(10, 10))

    label2 = tk.Label(root, text="Insert the desired time:", font=font_style, bg=bg_color, fg=fg_color)
    label2.pack(side="top", pady=(10, 10), anchor="w", padx=10)

    hour_minute_frame = tk.Frame(root, bg=bg_color)
    hour_minute_frame.pack(side="top", pady=(10, 10), anchor="w", padx=10)

    hour_label = tk.Label(hour_minute_frame, text="Hours:", font=font_style, bg=bg_color, fg=fg_color)
    hour_label.pack(side="left")

    min_label = tk.Label(hour_minute_frame, text="Minutes:", font=font_style, bg=bg_color, fg=fg_color)
    min_label.pack(side="left", padx=(35, 10))

    time_frame = tk.Frame(root, bg=bg_color)
    time_frame.pack(side="top", pady=(5, 10), anchor="w", padx=10)

    hour_spinbox = tk.Spinbox(time_frame, from_=0, to=24, width=3, font=("Segoe UI", 14), bg=button_bg, fg=a_color, insertbackground=fg_color)
    hour_spinbox.pack(side="left", padx=(0, 10))

    minute_spinbox = tk.Spinbox(time_frame, from_=0, to=60, width=3, font=("Segoe UI", 14), bg=button_bg, fg=a_color, insertbackground=fg_color)
    minute_spinbox.pack(side="left", padx=(30, 10))

    submit_button = tk.Button(root, text="Calculate", font=font_style, bg=accent_color, fg="white", activebackground=button_bg, command=calculate_time_ms)
    submit_button.pack(pady=(5, 10))

    timer_label = tk.Label(root, text="", font=large_font, bg=bg_color, fg=accent_color)
    timer_label.pack(pady=(20, 10))

    button_frame = tk.Frame(root, bg=bg_color)
    button_frame.pack(pady=(5, 10))

    pause_button = tk.Button(button_frame, text="Pause", font=font_style, bg=button_bg, fg=fg_color, activebackground=accent_color, state="disabled", command=pause_resume_timer)
    pause_button.pack(side="left", padx=10)

    stop_button = tk.Button(button_frame, text="Stop", font=font_style, bg=button_bg, fg=fg_color, activebackground=accent_color, state="disabled", command=stop_timer)
    stop_button.pack(side="left", padx=10)

    countdown_id = None
    countdown_seconds = 0
    countdown_running = False

    root.mainloop()

if __name__ == "__main__":
    create_window()
