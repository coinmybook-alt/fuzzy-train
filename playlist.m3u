import requests

def create_m3u():
    # Eklediğin gerçek kanal linkleri
    kanallar = [
        {"ad": "TRT 1 HD", "url": "http://89.187.191.41/TRT-1-HD-TR/video.m3u8"},
        {"ad": "ATV", "url": "http://95.174.71.114/TR-ATV/index.m3u8"},
        {"ad": "STAR TV", "url": "http://95.174.71.114:80/TR-STAR/index.m3u8"},
        {"ad": "SHOW TV", "url": "http://95.174.71.114:80/TR-SHOW/index.m3u8"},
        {"ad": "TV8", "url": "http://95.174.71.114/TR-TV8/index.m3u8"},
        {"ad": "KANAL 7 HD", "url": "https://kanal7-live.daioncdn.net/kanal7/kanal7.m3u8"},
        {"ad": "BEYAZ TV", "url": "https://beyaztv-live.daioncdn.net/beyaztv/beyaztv.m3u8"}
{"ad": "KANAL D", "url": "ad": "KANAL D", "url": "https://demiroren.daioncdn.net/kanald/kanald.m3u8"},https//demiroren.daioncdn.net/kanald/kanald.m3u8"},
    ]
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for kanal in kanallar:
            f.write(f"#EXTINF:-1,{kanal['ad']}\n")
            f.write(f"{kanal['url']}\n")

if __name__ == "__main__":
    create_m3u()
