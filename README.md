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

yp.hello_world("Merhaba Dünya!")
name = yp.yosk("Adınızı girin: ")
print(f"Hoş geldiniz, {name}!")
