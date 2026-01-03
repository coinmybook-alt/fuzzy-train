def create_m3u():
    # 2026 Güncel ve Stabil Kanal Linkleri
    kanallar = [
        {"ad": "KANAL D", "url": "https://demiroren.daioncdn.net/kanald/kanald.m3u8"},
        {"ad": "CNN TURK", "url": "https://demiroren.daioncdn.net/cnnturk/cnnturk.m3u8"},
        {"ad": "TRT 1", "url": "https://tv-trt1.medya.trt.com.tr/master.m3u8"},
        {"ad": "TRT SPOR", "url": "https://tv-trtspor1.medya.trt.com.tr/master.m3u8"},
        {"ad": "STAR TV", "url": "https://dogus-live.daioncdn.net/startv/startv.m3u8"},
        {"ad": "SHOW TV", "url": "https://ciner-live.daioncdn.net/showtv/showtv.m3u8"},
        {"ad": "TV8", "url": "https://tv8-live.daioncdn.net/tv8/tv8.m3u8"},
        {"ad": "KANAL 7", "url": "https://kanal7-live.daioncdn.net/kanal7/kanal7.m3u8"},
        {"ad": "BEYAZ TV", "url": "https://beyaztv-live.daioncdn.net/beyaztv/beyaztv.m3u8"}
    ]
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for k in kanallar:
            f.write(f"#EXTINF:-1,{k['ad']}\n{k['url']}\n")

if __name__ == "__main__":
    create_m3u()
