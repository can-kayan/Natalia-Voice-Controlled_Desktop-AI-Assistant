import pyautogui
import time
import subprocess
import shutil 
import pyttsx3 
from controls.sound_control import ses_al, sesli_cevap
def spotify_ac(): 
    """Spotify'ı başlatan fonksiyon"""
    spotify_path = shutil.which("spotify")
    if spotify_path:
        subprocess.Popen([spotify_path])
        time.sleep(2)
        print("Spotify başlatıldı.")
    else:
        print("Spotify bulunamadı.")

def spotify_sarki_arama_ve_cal(şarkı_adı): 
    pyautogui.hotkey('ctrl', 'l')  # Adres çubuğunu aktif et
    time.sleep(1)
    pyautogui.write(şarkı_adı)  # Şarkı adını yaz
    time.sleep(1)
    pyautogui.press('enter')  # Aramayı başlat
    time.sleep(1)
    pyautogui.press('tab')  # Oynatma butonuna geçiş yap
    time.sleep(1)
    pyautogui.press('enter')  # Oynatma butonuna tıkla
    time.sleep(1.1)  # Arama sonuçlarının gelmesi için bekle
    pyautogui.press('enter')  # Oynatmayı başlat

def init_spotify_sarki_cal(komut): 
    sabit_kelimeler = ["adlı şarkıyı açar mısın","şarkısını açar mısın","adlı şarkıyı çal", "adlı müziği çal","adlı şarkıyı","müziği aç","müziğini aç","adlı müziğini aç"]   
    istenen_kisim=""
    for sabit in sabit_kelimeler:
        if sabit in komut:
            print(komut)
            istenen_kisim = komut.replace(sabit, "").strip()  # Sabiti kaldır ve boşlukları temizle
            break 
    sesli_cevap(f'{istenen_kisim} adli muzigi baslatiyorum')
    spotify_ac()  # Spotify'ı başlat
    time.sleep(5)  # Spotify açıldıktan sonra biraz bekleyelim
    print(istenen_kisim)
    spotify_sarki_arama_ve_cal(istenen_kisim)  # Şarkıyı ara ve çal

if __name__ == "__main__":
    # Ana fonksiyon olarak çalıştırıldığında ne yapılacaksa buraya yazabiliriz.
    # Ancak başka dosyadan import edilecek, bu yüzden genellikle fonksiyonları çağırıyoruz.
    pass
