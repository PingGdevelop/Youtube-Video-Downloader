import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainView(ttk.Frame):
    def __init__(self, parent, on_download_click, url_var, progress_var, status_var):
        super().__init__(parent, padding=20)
        self.pack(fill=BOTH, expand=YES)
        
        self.on_download_click = on_download_click
        self.url_var = url_var
        self.progress_var = progress_var
        self.status_var = status_var

        self.create_widgets()

    def create_widgets(self):
        # Title
        lbl_title = ttk.Label(self, text="YouTube Downloader", font=("Helvetica", 16, "bold"))
        lbl_title.pack(pady=(0, 20))

        # Input Zone
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(fill=X, pady=10)

        self.ent_url = ttk.Entry(self.input_frame, textvariable=self.url_var, font=("Helvetica", 10))
        self.ent_url.pack(fill=X, ipady=5)

        self.progress_bar = ttk.Progressbar(self.input_frame, variable=self.progress_var, maximum=100, bootstyle="success-striped")
        
        # Status
        self.lbl_status = ttk.Label(self, textvariable=self.status_var, font=("Helvetica", 9), bootstyle="info")
        self.lbl_status.pack(pady=(5, 10))

        # Button
        self.btn_download = ttk.Button(self, text="DOWNLOAD", command=self.on_download_click, bootstyle="primary", width=20)
        self.btn_download.pack(pady=10)

    def show_progress(self, show=True):
        if show:
            self.ent_url.pack_forget()
            self.progress_bar.pack(fill=X, ipady=5)
        else:
            self.progress_bar.pack_forget()
            self.ent_url.pack(fill=X, ipady=5)

    def set_download_state(self, downloading=True):
        state = "disabled" if downloading else "normal"
        self.btn_download.config(state=state)
