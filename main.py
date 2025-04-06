import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk 

def start_recognition():
    try:
        subprocess.run(['python', 'test.py']) 
        messagebox.showinfo("Success", "Attendance has been recorded.")
    except Exception as e:
        messagebox.showerror("Error", f"Error starting recognition: {str(e)}")  
  
def search_log():
    try:
        subprocess.run(['python', 'search.py']) 
    except Exception as e:
        messagebox.showerror("Error", f"Error running search: {str(e)}")

root = tk.Tk()
root.title("Smart Door Log")
root.geometry("900x700")

bg_image = Image.open("img.png")  
bg_image = bg_image.resize((900, 700))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  

btn_style = {
    "font": ("Arial", 12, "bold"),
    "fg": "white",  
    "bg": "#121212", 
    "relief": "solid",  
    "borderwidth": 2,  
    "highlightthickness": 0, 
    "activebackground": "black",  
    "activeforeground": "white",  
    "cursor": "hand2" 
}

btn1 = tk.Button(root, text="Mark Your Attendance", command=start_recognition, **btn_style)
btn1.place(x=80, y=350, width=250, height=50)

btn2 = tk.Button(root, text="Search Log", command=search_log, **btn_style)
btn2.place(x=80, y=410, width=250, height=50)

root.mainloop()