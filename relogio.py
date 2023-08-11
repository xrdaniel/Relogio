import tkinter as tk
import time
from datetime import datetime, timezone, timedelta

def update_time():
    brt = timezone(timedelta(hours=-3))  # Fuso horário de Brasília (UTC-3)
    current_time = datetime.now(brt).strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)  # Atualiza a cada 1000ms (1 segundo)

root = tk.Tk()
root.title("Relógio Digital - Horário de Brasília")

label = tk.Label(root, font=("Helvetica", 48))
label.pack(padx=20, pady=20)

update_time()  # Inicia a atualização do relógio

root.mainloop()
