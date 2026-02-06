# YouTube Downloader Pro

A modern and powerful graphical application for downloading videos and audio from YouTube, built with Python, `yt-dlp`, and `ttkbootstrap`.

![Icon](assets/icon.png)

## 🚀 Features

- **Video Download**: Choose the desired resolution (1080p, 720p, etc.).
- **Audio Download**: Automatic conversion to high-quality MP3.
- **Modern Interface**: Bootstrap-based UI with dark theme.
- **Progress Bar**: Real-time download tracking.
- **Intelligent Merging**: Automatically combines audio and video for high resolutions (via FFmpeg).

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- **FFmpeg** (essential for audio/video merging and 1080p+ formats)
  - On Fedora: `sudo dnf install ffmpeg`
  - On Ubuntu/Debian: `sudo apt install ffmpeg`

### Python Dependencies
```bash
pip install -r requirements.txt
```

### Common issue on Linux (Fedora/Ubuntu)
If you encounter an error related to `ImageTk`, install the Tkinter support for Pillow:
```bash
sudo dnf install python3-pillow-tk  # Fedora
# or
sudo apt-get install python3-pil.imagetk  # Ubuntu
```

## 📖 Usage

Simply run the main script:
```bash
python UIX/main.py
```

1. Paste the video URL.
2. Click on **DOWNLOAD**.
3. Choose the type (Video or Audio) then the quality.

## 📜 Credits
See the [CREDITS.md](./CREDITS.md) file for more details on the libraries and resources used.

## ⚖️ License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
