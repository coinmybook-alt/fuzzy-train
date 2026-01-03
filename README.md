# 📺 Otomatik Güncellenen IPTV Playlist

Bu depo, Python ve GitHub Actions kullanarak kendi kendini güncelleyen bir M3U playlist dosyası oluşturur. Sistem her 6 saatte bir çalışarak linkleri kontrol eder ve günceller.

## 🚀 Hızlı Kullanım

Playlist'i IPTV oynatıcınıza (VLC, GSE IPTV, Tivimate vb.) eklemek için aşağıdaki **RAW** linkini kopyalayın:

`https://raw.githubusercontent.com/KULLANICI_ADINIZ/DEPO_ADINIZ/main/playlist.m3u`

*(Not: KULLANICI_ADINIZ ve DEPO_ADINIZ kısımlarını kendi bilgilerinizle değiştirin.)*

## 🛠️ Nasıl Çalışır?

1. **Python Scripti (`main.py`):** Belirlenen kaynaklardan kanal linklerini çeker ve M3U formatına dönüştürür.
2. **GitHub Actions:** Belirlenen zaman aralıklarında (cron) scripti çalıştırır ve güncellenen `playlist.m3u` dosyasını depoya geri yükler.

## 📅 Güncelleme Sıklığı
- **Otomatik:** Her 6 saatte bir.
- **Manuel:** Actions sekmesinden "Guncelle" workflow'u çalıştırılarak anlık güncellenebilir.
