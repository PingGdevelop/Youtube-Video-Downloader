import yt_dlp

def get_video_info(url):
    """Extrait les informations de la vidéo sans la télécharger."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=False)

def filter_formats(info):
    """Filtre et retourne une liste de formats vidéo exploitables."""
    formats = info.get('formats', [])
    available_formats = []
    seen_res = set()

    for f in formats:
        if f.get('vcodec') != 'none':
            height = f.get('height')
            f_id = f.get('format_id')
            note = f.get('format_note', '')
            ext = f.get('ext')
            
            if height and height not in seen_res:
                desc = f"{height}p - {note} ({ext})"
                available_formats.append({
                    'desc': desc,
                    'id': f_id,
                    'height': height
                })
                seen_res.add(height)

    # Tri par résolution (plus haute en premier)
    available_formats.sort(key=lambda x: x['height'], reverse=True)
    return available_formats
