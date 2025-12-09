from yt_dlp import YoutubeDL

playlist_url = input("Ссылка на плейлист: ")

ydl_opts = {
    "extract_flat": True,  # Не качать, только получить список
    "quiet": True
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)

links = ["https://www.youtube.com/watch?v=" + entry["id"] for entry in info["entries"]]

for link in links:
    print(link)
