import tkinter as tk
from tkinter import messagebox

scalingFactor = 1.60934

def m_to_k():
    try:
        miles = float(entry.get())
        km = miles * scalingFactor
        result_label.config(text=f"{miles:.2f} miles is approx. {km:.2f} km")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def k_to_m():
    try:
        km = float(entry.get())
        miles = km / scalingFactor
        result_label.config(text=f"{km:.2f} km is approx. {miles:.2f} miles")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Miles to Km Converter")
root.geometry("300x200")

label = tk.Label(root, text="Input Value:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

btn1 = tk.Button(root, text="Miles to Km", command=m_to_k)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Km to Miles", command=k_to_m)
btn2.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()