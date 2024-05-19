import tkinter as tk
from tkinter import ttk
from tkhtmlview import HTMLLabel
from WEBBROWSER import get_html

# GET homepage FILE CONTENT
home_file = open("HOMEPAGE.html", "r")
home_file_cont = home_file.read()
home_file.close()

class SimpleBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Browser")
        self.root.geometry("800x600")

        # Create the main frame
        self.main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Create the search bar
        self.url_var = tk.StringVar()
        self.search_bar = ttk.Entry(self.main_frame, textvariable=self.url_var, width=60)
        self.search_bar.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.search_button = ttk.Button(self.main_frame, text="Search", command=self.search_html)
        self.search_button.grid(row=0, column=1, padx=5, pady=5)

        # Create the HTML viewer
        self.html_viewer = HTMLLabel(self.main_frame, html=home_file_cont)
        self.html_viewer.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Add row/column configuration
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)
        self.main_frame.rowconfigure(1, weight=1)

    def search_html(self):
        url = self.search_bar.get()

        # Fetch HTML content and save it to a file
        get_html(url)
        # GET HTML FILE CONTENT
        html_file = open("WEBSITE.html", "r")
        html_file_cont = html_file.read()
        html_file.close()

        # Display HTML file directly
        self.html_viewer = HTMLLabel(self.main_frame, html=html_file_cont)
        self.html_viewer.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.N, tk.S, tk.E, tk.W))
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleBrowser(root)
    root.mainloop()
