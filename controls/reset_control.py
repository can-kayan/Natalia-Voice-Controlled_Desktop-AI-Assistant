import os

def reset_computer(): 
    try:
        print("Bilgisayar yeniden başlatılıyor...")
        os.system("shutdown /r /t 5")  # /r: Yeniden başlat, /t 0: Hemen başlat
    except Exception as e:
        print(f"Yeniden başlatma sırasında bir hata oluştu: {e}")
def shutdown_computer(): 
    try:
        print("Bilgisayar yeniden başlatılıyor...")
        os.system("shutdown /s /t 5")  # /r: Yeniden başlat, /t 0: Hemen başlat
    except Exception as e:
        print(f"Yeniden başlatma sırasında bir hata oluştu: {e}")

