# YouTube Downloader Pro

Une application graphique moderne et performante pour télécharger des vidéos et de l'audio depuis YouTube, construite avec Python, `yt-dlp` et `ttkbootstrap`.

![Icon](assets/icon.png)

## 🚀 Fonctionnalités

- **Téléchargement Vidéo** : Choisissez la résolution souhaitée (1080p, 720p, etc.).
- **Téléchargement Audio** : Conversion automatique en MP3 haute qualité.
- **Interface Moderne** : UI basée sur Bootstrap avec thème sombre.
- **Barre de Progression** : Suivi en temps réel du téléchargement.
- **Fusion Intelligente** : Combine automatiquement l'audio et la vidéo pour les hautes résolutions (via FFmpeg).

## 🛠️ Installation

### Prérequis
- Python 3.8+
- **FFmpeg** (indispensable pour la fusion audio/vidéo et les formats 1080p+)
  - Sur Fedora : `sudo dnf install ffmpeg`
  - Sur Ubuntu/Debian : `sudo apt install ffmpeg`

### Dépendances Python
```bash
pip install -r requirements.txt
```

### Problème courant sur Linux (Fedora/Ubuntu)
Si vous rencontrez une erreur liée à `ImageTk`, installez le support Tkinter pour Pillow :
```bash
sudo dnf install python3-pillow-tk  # Fedora
# ou
sudo apt-get install python3-pil.imagetk  # Ubuntu
```

## 📖 Utilisation

Lancez simplement le script principal :
```bash
python UIX/main.py
```

1. Collez l'URL de la vidéo.
2. Cliquez sur **TÉLÉCHARGER**.
3. Choisissez le type (Vidéo ou Audio) puis la qualité.

## 📜 Crédits
Voir le fichier [CREDITS.md](./CREDITS.md) pour plus de détails sur les bibliothèques et ressources utilisées.

## ⚖️ Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](./LICENSE) pour plus de détails.
