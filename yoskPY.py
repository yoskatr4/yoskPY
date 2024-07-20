# yoskPY.py

def hello_world(message):
    """Konsola bir mesaj yazdırır."""
    print(message)

def yosk(prompt):
    """Kullanıcıdan girdi alır."""
    return input(prompt)

def greet_user(name):
    """Kullanıcıya kişisel bir selam verir."""
    print(f"Merhaba, {name}! Hoş geldiniz!")

def calculate_sum(a, b):
    """İki sayının toplamını döndürür."""
    return a + b

def save_to_file(filename, content):
    """Verilen içeriği belirtilen dosyaya kaydeder."""
    with open(filename, 'w') as file:
        file.write(content)
    print(f"İçerik '{filename}' dosyasına kaydedildi.")

def read_from_file(filename):
    """Belirtilen dosyadan içeriği okur ve döndürür."""
    with open(filename, 'r') as file:
        content = file.read()
    return content

def repeat_message(message, times):
    """Bir mesajı belirtilen sayıda tekrarlar."""
    return message * times
