
from controls.sound_control import sesli_cevap, ses_al
from controls.spotify_control import init_spotify_sarki_cal 
from controls.reset_control import reset_computer, shutdown_computer 
from controls.brave_control import bionluk_ac
from controls.close_app_control import close_app_control
from controls.open_app_control import open_app_control
from NLP_test import start_chat
import time
def komut_isle():
    # if "Nata" in komut:
    #     sesli_cevap("Efendim...") 
    # if "adın ne" in komut: 
    #     sesli_cevap("Benim adimi neden bilmiyorsun orospu çocuğu") 
    
    komut_zamani = time.time()
    while True: 
        komut=ses_al() 

        if "yazmak" in komut:
            sesli_cevap("Ne demek istiyorsun")
            komut=""
            komut=input()  
        if "uygulamayı aç" in komut:
            open_app_control(komut)
        elif "uygulamayı kapat" in komut:
            close_app_control(komut)
        elif "teşekkür" in komut or "çıkış" in komut:
            sesli_cevap("Rica ederim...")
            break 
        elif "yeniden başlat" in komut:
            reset_computer()
            sesli_cevap("Bilgisayar bes saniye icinde yeeniden baslatiliyor...")
        elif "bilgisayarı kapat" in komut:
            shutdown_computer()
            sesli_cevap("Bilgisayar bes saniye icinde kapatiliyor...")
        elif "iş yeri" in komut:
            bionluk_ac()
            sesli_cevap("Bionluk aciliyor...")
        elif "müziği" in komut or "şarkı" in komut:
            init_spotify_sarki_cal(komut)
            sesli_cevap("Muzik baslatildi...")  
        elif komut!="" :
            start_chat(komut)  
            komut=""
        elif komut=="" and time.time()-komut_zamani>=5:
            sesli_cevap("Bir sey demiyorsan ben gidiyorum. Kendine iyi bak...") 
            break
     
