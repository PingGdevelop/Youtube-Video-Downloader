import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class QualitySelectionPopup(ttk.Toplevel):
    def __init__(self, parent, available_formats, on_quality_selected):
        super().__init__(parent)
        self.title("Qualité")
        self.geometry("350x180")
        
        # Centrage
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 175
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 90
        self.geometry(f"+{x}+{y}")

        ttk.Label(self, text="Sélectionnez la résolution :").pack(pady=15)
        
        combo_values = [f['desc'] for f in available_formats]
        self.combo = ttk.Combobox(self, values=combo_values, state="readonly", width=30)
        self.combo.current(0)
        self.combo.pack(pady=10)

        def confirm():
            selected_index = self.combo.current()
            f_id = available_formats[selected_index]['id']
            self.destroy()
            on_quality_selected(f_id)

        ttk.Button(self, text="Télécharger", command=confirm, bootstyle="success").pack(pady=15)
