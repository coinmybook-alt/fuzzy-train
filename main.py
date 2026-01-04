def create_m3u():
    # Kanal D, ATV ve senin son paylaştığın özel link dahil güncel liste
    kanallar = [
        {"ad": "KANAL D", "url": "https://demiroren.daioncdn.net/kanald/kanald.m3u8|User-Agent=Mozilla/5.0"},
        {"ad": "ATV", "url": "https://trkvz-live.daioncdn.net/atv/atv_1080p.m3u8|User-Agent=Mozilla/5.0"},
        {"ad": "OZEL YAYIN", "url": "http://104.238.23.182/d/live/out.m3u8"},
        {"ad": "TRT 1", "url": "https://tv-trt1.medya.trt.com.tr/master.m3u8"},
        {"ad": "STAR TV", "url": "https://dogus-live.daioncdn.net/startv/startv.m3u8"},
        {"ad": "SHOW TV", "url": "https://ciner-live.daioncdn.net/showtv/showtv.m3u8"},
        {"ad": "NOW TV", "url": "https://uycyyuuzyh.turknet.ercdn.net/nphindgytw/nowtv/nowtv.m3u8|User-Agent=Mozilla/5.0"}
    ]
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for k in kanallar:
            f.write(f"#EXTINF:-1,{k['ad']}\n{k['url']}\n")

if __name__ == "__main__":
    create_m3u()
