import yt_dlp

def download_media(url, format_id, is_audio, progress_callback):
    """Gère le téléchargement de la vidéo ou de l'audio."""
    
    def internal_hook(d):
        if progress_callback:
            progress_callback(d)

    ydl_opts = {
        'format': format_id,
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [internal_hook],
        'noplaylist': True,
    }

    if is_audio:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        ydl_opts['merge_output_format'] = 'mp4'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
