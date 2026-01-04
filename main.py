def create_m3u():
    # Çalışan en güncel kanal listesi
    kanallar = [
        {"ad": "KANAL D", "url": "https://demiroren.daioncdn.net/kanald/kanald.m3u8"},
        {"ad": "ATV", "url": "https://trkvz-live.daioncdn.net/atv/atv_1080p.m3u8"},
        {"ad": "TRT 1", "url": "https://tv-trt1.medya.trt.com.tr/master.m3u8"},
        {"ad": "STAR TV", "url": "https://dogus-live.daioncdn.net/startv/startv.m3u8"},
        {"ad": "SHOW TV", "url": "https://ciner-live.daioncdn.net/showtv/showtv.m3u8"},
        {"ad": "TV8", "url": "https://tv8-live.daioncdn.net/tv8/tv8.m3u8"},
        {"ad": "KANAL 7", "url": "https://kanal7-live.daioncdn.net/kanal7/kanal7.m3u8"}
    ]
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for k in kanallar:
            f.write(f"#EXTINF:-1,{k['ad']}\n{k['url']}\n")

if __name__ == "__main__":
    create_m3u()
