# yoskPY

`yoskPY` Python kütüphanesi, temel işlemleri gerçekleştirmek için basit ve kullanışlı fonksiyonlar sunar.

## Fonksiyonlar

- `hello_world(message)`: Bir mesajı ekrana yazdırır.
- `yosk(prompt)`: Kullanıcıdan girdi alır.
- `greet_user(name)`: Kişisel bir selam verir.
- `calculate_sum(a, b)`: İki sayının toplamını döndürür.
- `save_to_file(filename, content)`: İçeriği bir dosyaya kaydeder.
- `read_from_file(filename)`: Bir dosyadan içeriği okur.
- `repeat_message(message, times)`: Bir mesajı belirli bir sayıda tekrarlar.
- `run_command`: Yeni bir terminalde komut çalıştırır (bu örnekte Windows için).
- `open_app`: Belirtilen uygulamayı açar (örneğin, Windows'ta Komut İstemi).

## Kurulum

Kütüphaneyi kullanmak için öncelikle `yoskPY.py` dosyasını projenize ekleyin.

## Kullanım

Fonksiyonları kullanmak için aşağıdaki örnekleri inceleyebilirsiniz:

```python
import yoskPY as yp

# Konsola bir mesaj yazdırma
yp.hello_world("Merhaba Dünya!")

# Kullanıcıdan giriş alma ve selam verme
isim = yp.yosk("Adınızı girin: ")
yp.greet_user(isim)

# İki sayının toplamını hesaplama
toplam = yp.calculate_sum(5, 7)
print(f"5 ve 7'nin toplamı: {toplam}")

# Dosyaya içerik kaydetme ve okuma
dosya_adi = "ornek_dosya.txt"
icerik = "Bu dosyada saklanacak örnek içeriktir."
yp.save_to_file(dosya_adi, icerik)
okunan_icerik = yp.read_from_file(dosya_adi)
print(f"{dosya_adi} dosyasından okunan içerik:\n{okunan_icerik}")

# Bir mesajı tekrarlama
tekrarlanan_mesaj = yp.repeat_message("Merhaba! ", 3)
print(tekrarlanan_mesaj)

# Yeni bir terminalde komut çalıştırma (Windows için)
# 'echo Hello World' komutunu yeni bir terminalde çalıştırır
yp.run_command('echo Hello World', new_terminal=True, os='windows')

# Uygulama açma (Windows'ta Komut İstemi'ni açma)
yp.open_app('cmd', os='windows')

encrypt_text = yp.encrypt_text("selam")
print(encrypt_text)

decrypt_text = yp.decrypt_text("1218 264 1155 219 1164")
print(decrypt_text)

basic_encrypt_text = yp.basic_encrypt_text("selam")
print(basic_encrypt_text)

basic_decrypt_text = yp.basic_decrypt_text("22 6 15 1 16")
print(basic_decrypt_text)
