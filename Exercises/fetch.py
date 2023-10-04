import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if response.status_code == 200:
        data = response.json()
        # Clear any existing text in the Text widget
        data_text.delete("1.0", tk.END)
        # Inserting the new data into the Text widget
        data_text.insert(tk.END, "Title: " + data.get("title") + "\n")
        data_text.insert(tk.END, "User ID: " + str(data.get("userId")) + "\n")
        data_text.insert(tk.END, "Completed: " + str(data.get("completed")) + "\n")
    else:
        messagebox.showerror("Error", f"Failed to retrieve data. Status code: {response.status_code}")

# Initialize the main window
root = tk.Tk()
root.title("API Data Fetcher")

# Create the Text widget to display data
data_text = tk.scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
data_text.pack(pady=20)

# Create a Button to fetch the data
fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack(pady=20)

root.mainloop()
