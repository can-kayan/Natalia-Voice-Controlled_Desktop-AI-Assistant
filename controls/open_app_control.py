 
import subprocess  
import subprocess  
from controls.seach_apps import find_application_path
from controls.sound_control import sesli_cevap
def open_app_control(komut):
    sabit_kelimeler = ["adlı uygulamayı açar mısın", "uygulamasını açar mısın", "adlı uygulamayı aç", "adlı programı  aç", "adlı uygulamayı", "uygulamayı aç", "uygulamasını aç", "adlı uygulamasını aç","aç" ]   
     

    app_name = komut  # Varsayılan olarak komutun tamamını alıyoruz

    for sabit in sabit_kelimeler:
        if sabit in komut:
            app_name = komut.replace(sabit, "").strip()  # Kelimeyi çıkardıktan sonra baştaki ve sondaki boşlukları temizleyin
            break  # İlk eşleşmede çıkacak şekilde işlemi sonlandırıyoruz

    
    sesli_cevap(f'{app_name} adli uygulamayı baslatiyorum')
    path = find_application_path(app_name)
    print(path)
    if path: 
        process = subprocess.Popen(
            [path],
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            close_fds=True,
            shell=True
        )  
    else:
        print(f"{komut} uygulaması belirtilen dizinlerde bulunamadı.")