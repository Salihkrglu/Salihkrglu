import sqlite3

# veriler.db isimli bir veritabanı yarat
baglanti = sqlite3.connect("veriler.db")

# tablo yaratma, silme ve diğer işlemler için cursor nesnesi yarat
imlec = baglanti.cursor()
sorgu = "CREATE TABLE IF NOT EXISTS kullanicilar (ad TEXT, email TEXT, sifre TEXT)"
# sql sorgusunu çalıştır
imlec.execute(sorgu)
# tüm veritabanı işlemlerini uygula, kaydet
baglanti.commit()

#tabloya veri kaydet
sorgu = "INSERT INTO kullanicilar VALUES('salih', 'salih@gmail.com', '123456')"
imlec.execute(sorgu)

baglanti.commit()


sorgu = """CREATE TABLE IF NOT EXISTS urunler (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                               kod TEXT,
                                               ISBN TEXT,
                                               isim TEXT,
                                               fiyat REAL,
                                               resim TEXT)"""
# sql sorgusunu çalıştır
imlec.execute(sorgu)
# tüm veritabanı işlemlerini uygula, kaydet
baglanti.commit()

#tabloya veri kaydet
import random
semboller= "0123456789abcdefghijklmnoprstABCDEFGHJKLMNPRST"
urun_kodu = "".join(random.choices(semboller, k=5))

sorgu = f"INSERT INTO urunler (kod, ISBN, isim, fiyat, resim) VALUES ('{urun_kodu}', '978-975-6856-00-9', 'suç ve ceza', 25, 'suçveceza.jpg')"
imlec.execute(sorgu)

baglanti.commit()






