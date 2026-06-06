import subprocess
import sys
import os

# 1. Automatische Installation
def setup():
    packages = ["customtkinter", "screen-brightness-control"]
    for pkg in packages:
        try:
            __import__(pkg.replace("-", "_") if pkg != "customtkinter" else "customtkinter")
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
setup()

import customtkinter as ctk
import screen_brightness_control as sbc
import json

CONFIG_FILE = "settings.json"

class MonitorHUD(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Display Pro")
        self.geometry("280x160")
        self.resizable(False, False)
        
        # Lade alten Wert
        self.brightness = self.load_settings()

        self.label = ctk.CTkLabel(self, text=f"Helligkeit: {int(self.brightness)}%", font=("Arial", 14, "bold"))
        self.label.pack(pady=(15, 5))

        self.slider = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.slider.set(self.brightness)
        self.slider.pack(pady=10, padx=20)
        
        # Regler-Logik
        self.slider.bind("<ButtonRelease-1>", self.update_brightness)
        
        # Button für "Display aus" (nur Hintergrundbeleuchtung)
        self.btn_off = ctk.CTkButton(self, text="Bildschirm Standby", command=self.turn_off, height=25)
        self.btn_off.pack(pady=10)

    def load_settings(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                return json.load(f).get("brightness", 50)
        return 50

    def update_brightness(self, event):
        val = int(self.slider.get())
        sbc.set_brightness(val) # Steuert alle erkannten Monitore
        self.label.configure(text=f"Helligkeit: {val}%")
        with open(CONFIG_FILE, "w") as f:
            json.dump({"brightness": val}, f)

    def turn_off(self):
        sbc.set_brightness(0)

if __name__ == "__main__":
    app = MonitorHUD()
    app.mainloop()import subprocess
import sys
import os

# 1. Automatische Installation
def setup():
    packages = ["customtkinter", "screen-brightness-control"]
    for pkg in packages:
        try:
            __import__(pkg.replace("-", "_") if pkg != "customtkinter" else "customtkinter")
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
setup()

import customtkinter as ctk
import screen_brightness_control as sbc
import json

CONFIG_FILE = "settings.json"

class MonitorHUD(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Display Pro")
        self.geometry("280x160")
        self.resizable(False, False)
        
        # Lade alten Wert
        self.brightness = self.load_settings()

        self.label = ctk.CTkLabel(self, text=f"Helligkeit: {int(self.brightness)}%", font=("Arial", 14, "bold"))
        self.label.pack(pady=(15, 5))

        self.slider = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.slider.set(self.brightness)
        self.slider.pack(pady=10, padx=20)
        
        # Regler-Logik
        self.slider.bind("<ButtonRelease-1>", self.update_brightness)
        
        # Button für "Display aus" (nur Hintergrundbeleuchtung)
        self.btn_off = ctk.CTkButton(self, text="Bildschirm Standby", command=self.turn_off, height=25)
        self.btn_off.pack(pady=10)

    def load_settings(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                return json.load(f).get("brightness", 50)
        return 50

    def update_brightness(self, event):
        val = int(self.slider.get())
        sbc.set_brightness(val) # Steuert alle erkannten Monitore
        self.label.configure(text=f"Helligkeit: {val}%")
        with open(CONFIG_FILE, "w") as f:
            json.dump({"brightness": val}, f)

    def turn_off(self):
        sbc.set_brightness(0)

if __name__ == "__main__":
    app = MonitorHUD()
    app.mainloop()