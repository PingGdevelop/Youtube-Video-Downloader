import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import threading
import sys
import os

# Ajout du dossier UIX au path pour les imports si nécessaire
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from quality_checker import get_video_info, filter_formats
from downloader_engine import download_media
from view.main_view import MainView
from view.type_view import TypeSelectionPopup
from view.quality_view import QualitySelectionPopup

class YtDownloaderApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.title("Youtube Downloader Pro")
        self.geometry("600x250")
        self.resizable(False, False)

        # Chargement de l'icône
        try:
            icon_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "icon.png")
            img = tk.PhotoImage(file=icon_path)
            self.iconphoto(False, img)
        except Exception as e:
            print(f"Impossible de charger l'icône : {e}")

        self.url_var = tk.StringVar()
        self.progress_var = tk.DoubleVar()
        self.status_var = tk.StringVar(value="Prêt")
        self.video_info = None

        # Initialisation de la vue principale
        self.view = MainView(self, self.on_download_click, self.url_var, self.progress_var, self.status_var)

    def on_download_click(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Erreur", "Veuillez entrer une URL valide.")
            return

        self.view.set_download_state(True)
        self.status_var.set("Analyse de la vidéo...")
        threading.Thread(target=self.process_video_info, args=(url,), daemon=True).start()

    def process_video_info(self, url):
        try:
            self.video_info = get_video_info(url)
            self.after(0, self.open_type_popup)
        except Exception as e:
            self.after(0, lambda: self.show_error(f"Erreur : {str(e)}"))

    def show_error(self, msg):
        self.status_var.set("Erreur")
        self.view.set_download_state(False)
        messagebox.showerror("Erreur", msg)

    def open_type_popup(self):
        TypeSelectionPopup(
            self, 
            on_video_selected=self.open_quality_popup,
            on_audio_selected=lambda: self.start_download("bestaudio/best", True)
        )

    def open_quality_popup(self):
        available_formats = filter_formats(self.video_info)
        
        if not available_formats:
            # Fallback
            self.start_download("bestvideo+bestaudio/best", False)
            return

        QualitySelectionPopup(
            self,
            available_formats,
            on_quality_selected=lambda f_id: self.start_download(f"{f_id}+bestaudio/best", False)
        )

    def start_download(self, format_id, is_audio):
        self.view.show_progress(True)
        self.status_var.set("Téléchargement...")
        threading.Thread(target=self.run_download, args=(format_id, is_audio), daemon=True).start()

    def run_download(self, format_id, is_audio):
        try:
            download_media(self.url_var.get(), format_id, is_audio, self.progress_callback)
            self.after(0, self.on_complete)
        except Exception as e:
            self.after(0, lambda: self.show_error(str(e)))

    def progress_callback(self, d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            if total:
                percent = (d.get('downloaded_bytes', 0) / total) * 100
                self.after(0, lambda: self.progress_var.set(percent))
                self.after(0, lambda: self.status_var.set(f"Téléchargement : {percent:.1f}%"))

    def on_complete(self):
        messagebox.showinfo("Succès", "Téléchargement terminé !")
        self.view.show_progress(False)
        self.status_var.set("Prêt")
        self.url_var.set("")
        self.view.set_download_state(False)

if __name__ == "__main__":
    app = YtDownloaderApp()
    app.mainloop()
