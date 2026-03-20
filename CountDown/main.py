import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
from plyer import notification

class TopTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("TopTimer")
        self.root.geometry("400x500")
        self.root.configure(bg="#F8FAFC")
        self.root.resizable(False, False)

        # --- State ---
        self.running = False
        self.remaining_seconds = 0

        self.setup_ui()

    def setup_ui(self):
        """Builds a modern, light-mode timer interface."""
        # Header
        header = tk.Frame(self.root, bg="#F8FAFC", pady=20)
        header.pack(fill="x")
        tk.Label(header, text="TopTimer", font=("Helvetica", 24, "bold"), 
                 bg="#F8FAFC", fg="#1E293B").pack()

        # Display Area
        self.display_lbl = tk.Label(self.root, text="00:00:00", font=("Courier", 48, "bold"), 
                                    bg="#F8FAFC", fg="#3B82F6")
        self.display_lbl.pack(pady=30)

        # Input Card
        card = tk.Frame(self.root, bg="white", bd=1, relief="solid", padx=20, pady=20)
        card.pack(fill="x", padx=40)

        # Entry Grid
        input_frame = tk.Frame(card, bg="white")
        input_frame.pack()

        self.h_var = tk.StringVar(value="0")
        self.m_var = tk.StringVar(value="0")
        self.s_var = tk.StringVar(value="0")

        def create_spin(var, label):
            f = tk.Frame(input_frame, bg="white")
            f.pack(side="left", padx=5)
            tk.Label(f, text=label, font=("Helvetica", 8), bg="white").pack()
            tk.Spinbox(f, from_=0, to=59, width=3, textvariable=var, 
                       font=("Helvetica", 14), bd=0, bg="#F1F5F9").pack()

        create_spin(self.h_var, "HH")
        create_spin(self.m_var, "MM")
        create_spin(self.s_var, "SS")

        tk.Label(card, text="Message:", bg="white", font=("Helvetica", 9)).pack(pady=(15, 0), anchor="w")
        self.msg_var = tk.StringVar(value="Timer Done!")
        tk.Entry(card, textvariable=self.msg_var, bg="#F1F5F9", bd=0, font=("Helvetica", 10)).pack(fill="x", pady=5)

        # Controls
        self.btn_start = tk.Button(self.root, text="START TIMER", bg="#10B981", fg="white", 
                                   font=("Helvetica", 12, "bold"), relief="flat", height=2,
                                   command=self.start_timer_thread)
        self.btn_start.pack(fill="x", padx=40, pady=20)

    def start_timer_thread(self):
        if self.running:
            self.stop_timer()
            return

        try:
            h = int(self.h_var.get())
            m = int(self.m_var.get())
            s = int(self.s_var.get())
            self.remaining_seconds = h * 3600 + m * 60 + s

            if self.remaining_seconds <= 0:
                return

            self.running = True
            self.btn_start.config(text="STOP", bg="#EF4444")
            
            # Use threading so the UI doesn't freeze during time.sleep()
            threading.Thread(target=self.countdown, daemon=True).start()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers.")

    def countdown(self):
        while self.remaining_seconds > 0 and self.running:
            # Efficiently calculate H:M:S from total seconds
            # 
            mins, secs = divmod(self.remaining_seconds, 60)
            hours, mins = divmod(mins, 60)
            time_str = f"{hours:02d}:{mins:02d}:{secs:02d}"
            
            self.display_lbl.config(text=time_str)
            time.sleep(1)
            self.remaining_seconds -= 1

        if self.remaining_seconds == 0 and self.running:
            self.notify_user()
            
        self.stop_timer()

    def notify_user(self):
        self.display_lbl.config(text="00:00:00")
        notification.notify(
            title="TopAlert",
            message=self.msg_var.get(),
            app_name="TopTimer",
            timeout=10
        )
        messagebox.showinfo("Time's Up", self.msg_var.get())

    def stop_timer(self):
        self.running = False
        self.btn_start.config(text="START TIMER", bg="#10B981")
        self.display_lbl.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = TopTimer(root)
    root.mainloop()