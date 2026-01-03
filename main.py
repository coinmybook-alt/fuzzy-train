import requests

# Kaynak linkler (Örnektir, çalışan linklerinizi buraya ekleyin)
urls = [
    "https://example.com/api/get_links",
    "https://raw.githubusercontent.com/user/repo/main/links.txt"
]

def create_m3u():
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        # Buraya linkleri işleme mantığınızı ekleyin
        f.write("#EXTINF:-1,Kanal Adı\n")
        f.write("http://yayin-linki.com/stream.m3u8\n")

if __name__ == "__main__":
    create_m3u()


