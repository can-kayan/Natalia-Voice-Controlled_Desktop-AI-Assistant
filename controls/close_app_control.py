import subprocess
import psutil
from controls.sound_control import sesli_cevap

def close_app_control(komut):
    try:
        sabit_kelimeler = ["adlı uygulamayı kapatır mısın", "uygulamasını kapatır mısın", "adlı uygulamayı kapat", "adlı programı  kapat", "uygulamayı kapat", "uygulamasını kapat", "adlı uygulamasını kapat","kapat" ]   
        app_name = komut  # Varsayılan olarak komutun tamamını alıyoruz
        for sabit in sabit_kelimeler:
            if sabit in komut:
                app_name = komut.replace(sabit, "").strip()  # Kelimeyi çıkardıktan sonra baştaki ve sondaki boşlukları temizleyin
                break  # İlk eşleşmede çıkacak şekilde işlemi sonlandırıyoruz

        print(app_name)
        # Uygulama adı ile taskkill komutunu çalıştırıyoruz
        subprocess.run(f"taskkill /F /IM {app_name}.exe", check=True, shell=True)
        print(f"{app_name} uygulaması başarıyla kapatıldı.")
    except subprocess.CalledProcessError:
        print(f"{app_name} uygulaması kapatılamadı.") 