import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

class SearchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Search Attendance")
        self.root.geometry("700x500")
        self.root.configure(bg="#2c3e50") 

        tk.Label(root, text="Search Attendance", font=("Arial", 20, "bold"), bg="#2c3e50", fg="white").pack(pady=20)
        tk.Label(root, text="Enter Name:", font=("Arial", 14), bg="#2c3e50", fg="white").pack()

        self.entry_name = tk.Entry(root, width=40, font=("Arial", 14))
        self.entry_name.pack(pady=10)

        self.search_button = tk.Button(
            root, text="Search", command=self.search_name, width=20, height=2,
            font=("Arial", 12, "bold"), bg="#2c3e50", fg="white", relief="solid", borderwidth=2, highlightbackground="white"
        )
        self.search_button.pack(pady=20)

    def search_name(self):
        name = self.entry_name.get().strip().title()  
        if not name:
            messagebox.showwarning("Input Error", "Please enter a name to search.")
            return

        file_path = f'Attendance/Attendance_{pd.Timestamp.today().strftime("%d-%m-%Y")}.csv'
        
        if not os.path.exists(file_path):
            messagebox.showerror("File Not Found", f"Attendance file for today not found:\n{file_path}")
            return

        try:
            df = pd.read_csv(file_path)

            if "NAME" not in df.columns or "TIME" not in df.columns:
                messagebox.showerror("Error", "CSV file does not contain required columns: 'NAME' and 'TIME'")
                return

            df['NAME'] = df['NAME'].astype(str).str.title()

            result_df = df[df['NAME'] == name]
            
            if not result_df.empty:
                result = "\n".join([f"{row['NAME']} - {row['TIME']}" for _, row in result_df.iterrows()])
            else:
                result = "No records found."
        except Exception as e:
            result = f"Error reading file: {str(e)}"
        
        messagebox.showinfo("Search Result", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = SearchGUI(root)
    root.mainloop()