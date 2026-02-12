import tkinter as tk
from tkinter import messagebox
import requests


# Constants for styling
BG_COLOR = "#212121"      # Dark Charcoal
ACCENT_COLOR = "#00E5FF"  # Cyan
TEXT_COLOR = "#FFFFFF"    # White
CARD_COLOR = "#2D2D2D"    # Lighter Grey for contrast

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickWeather")
        self.root.geometry("450x550")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)
        self.root.wm_iconbitmap("./images/icon.ico")

        self.setup_ui()

    def setup_ui(self):
        # Header
        tk.Label(self.root, text="QuickWeather", font=("Inter", 24, "bold"), 
                 bg=BG_COLOR, fg=ACCENT_COLOR).pack(pady=20)

        # Input Area
        input_frame = tk.Frame(self.root, bg=BG_COLOR)
        input_frame.pack(pady=10)

        self.place_name = tk.StringVar()
        self.entry = tk.Entry(input_frame, textvariable=self.place_name, font=("Inter", 14),
                              bg=CARD_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR,
                              border=0, justify="center", width=20)
        self.entry.pack(side=tk.LEFT, ipady=8, padx=5)
        self.entry.bind('<Return>', lambda e: self.fetch_weather())

        # Action Buttons
        btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Search", command=self.fetch_weather, bg=ACCENT_COLOR, 
                  fg=BG_COLOR, font=("Inter", 10, "bold"), width=10, relief="flat", cursor="hand2").pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="Reset", command=self.reset_fields, bg="#FF5252", 
                  fg=TEXT_COLOR, font=("Inter", 10, "bold"), width=10, relief="flat", cursor="hand2").pack(side=tk.LEFT, padx=5)

        # Results Display Area
        self.results_frame = tk.LabelFrame(self.root, text=" Weather Forecast ", bg=BG_COLOR, 
                                          fg=ACCENT_COLOR, font=("Inter", 10), padx=20, pady=20)
        self.results_frame.pack(padx=20, fill="both", expand=True, pady=10)

        self.metrics = {
            "Current": tk.StringVar(value="--"),
            "High": tk.StringVar(value="--"),
            "Low": tk.StringVar(value="--"),
            "Precipitation": tk.StringVar(value="--"),
            "Clouds": tk.StringVar(value="--")
        }

        for label, var in self.metrics.items():
            f = tk.Frame(self.results_frame, bg=BG_COLOR)
            f.pack(fill="x", pady=5)
            tk.Label(f, text=label, bg=BG_COLOR, fg="#AAAAAA", font=("Inter", 11)).pack(side=tk.LEFT)
            tk.Label(f, textvariable=var, bg=BG_COLOR, fg=TEXT_COLOR, font=("Inter", 11, "bold")).pack(side=tk.RIGHT)

    def f_to_c(self, f):
        return int((f - 32) * 5/9)

    def fetch_weather(self):
        query = self.place_name.get().strip()
        if not query: return

        # Quick fix for Delhi
        if query.lower() == "delhi": query = "New Delhi"

        api_key = "H5976K629HDQX4BGJFTVZQRCN"
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{query}?unitGroup=us&key={api_key}&contentType=json"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()["days"][0]

            # Calculation & Update
            temp_f = data["temp"]
            self.metrics["Current"].set(f"{temp_f}°F | {self.f_to_c(temp_f)}°C")
            self.metrics["High"].set(f"{data['tempmax']}°F | {self.f_to_c(data['tempmax'])}°C")
            self.metrics["Low"].set(f"{data['tempmin']}°F | {self.f_to_c(data['tempmin'])}°C")
            self.metrics["Precipitation"].set(f"{data['precipprob']}%")
            self.metrics["Clouds"].set(f"{data['cloudcover']}%")

        except Exception:
            messagebox.showerror("Error", f"Could not find weather for '{query}'")

    def reset_fields(self):
        self.place_name.set("")
        for var in self.metrics.values(): var.set("--")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()