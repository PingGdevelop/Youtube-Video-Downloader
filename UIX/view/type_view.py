import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class TypeSelectionPopup(ttk.Toplevel):
    def __init__(self, parent, on_video_selected, on_audio_selected):
        super().__init__(parent)
        self.title("Type")
        self.geometry("300x150")
        self.resizable(False, False)
        
        # Centrage
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 150
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 75
        self.geometry(f"+{x}+{y}")

        ttk.Label(self, text="Choisissez le type :").pack(pady=20)
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=X, padx=20)

        def video_click():
            self.destroy()
            on_video_selected()

        def audio_click():
            self.destroy()
            on_audio_selected()

        ttk.Button(btn_frame, text="VIDÉO", command=video_click, bootstyle="success").pack(side=LEFT, expand=YES, padx=5)
        ttk.Button(btn_frame, text="AUDIO", command=audio_click, bootstyle="info").pack(side=RIGHT, expand=YES, padx=5)
