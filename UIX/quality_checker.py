import yt_dlp

def get_video_info(url):
    """Extracts video information without downloading it."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=False)

def filter_formats(info):
    """Filters and returns a list of usable video formats."""
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

    # Sort by resolution (highest first)
    available_formats.sort(key=lambda x: x['height'], reverse=True)
    return available_formats
