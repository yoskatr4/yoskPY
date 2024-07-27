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
import subprocess
import platform


def run_command(command, new_terminal=False, os=None):
    try:
        # Determine the operating system if not specified
        if os is None:
            os = platform.system().lower()

        if new_terminal:
            if os == 'windows':
                # Windows için yeni terminalde komut çalıştır
                command = f'start cmd /k "{command}"'
            elif os == 'linux':
                # Linux için yeni terminalde komut çalıştır (gnome-terminal, konsole, etc. kullanılabilir)
                command = f'gnome-terminal -- {command}'
            elif os == 'darwin':
                # macOS için yeni terminalde komut çalıştır
                command = f'osascript -e \'tell application "Terminal" to do script "{command}"\''
            else:
                print("Bilinmeyen işletim sistemi. Yeni terminal açma özelliği desteklenmiyor.")
                return
        
        # Komutu çalıştır
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        # Komutun çıktısını ve hatasını yazdır
        if result.stdout:
            print('Çıktı:', result.stdout)
        if result.stderr:
            print('Hata:', result.stderr)
        print('Çıkış kodu:', result.returncode)
    except subprocess.CalledProcessError as e:
        print('Komut çalıştırılırken hata oluştu:', e)
        if e.stdout:
            print('Çıktı:', e.stdout)
        if e.stderr:
            print('Hata:', e.stderr)

def open_app(app_name, os=None):
    try:
        # Determine the operating system if not specified
        if os is None:
            os = platform.system().lower()

        if os == 'windows':
            # Windows için uygulama başlat
            command = f'start {app_name}'
        elif os == 'linux':
            # Linux için uygulama başlat (xdg-open, gnome-open, or the application name directly)
            command = f'{app_name}'
        elif os == 'darwin':
            # macOS için uygulama başlat
            command = f'open -a "{app_name}"'
        else:
            print("Bilinmeyen işletim sistemi. Uygulama açma özelliği desteklenmiyor.")
            return
        
        # Komutu çalıştır
        subprocess.run(command, shell=True, check=True)
        print(f'{app_name} başarıyla başlatıldı.')
    except subprocess.CalledProcessError as e:
        print(f'{app_name} başlatılırken hata oluştu:', e)
        if e.stdout:
            print('Çıktı:', e.stdout)
        if e.stderr:
            print('Hata:', e.stderr)
