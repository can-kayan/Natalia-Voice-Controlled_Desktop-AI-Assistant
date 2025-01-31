 
from controls.sound_control import ses_al, sesli_cevap
from command_cal import komut_isle
from NLP_test import installation_chat
import time
def main(): 
    # installation_chat()
    wake_word = "Nata"  
    sessizlik_sayaci = 0
    while True: 
        komut = ses_al()

        if komut and wake_word in komut: 
            sessizlik_sayaci = 0  
            komut_zamani = time.time()  

            while True:
                komut = ses_al()   
                if komut:  
                    if "Nata" in komut:
                        sesli_cevap("Efendim...") 
                        komut_zamani = time.time() 
                        komut_isle()  
                    else: 
                        pass
                else: 
                    gecen_zaman = time.time() - komut_zamani  
                    print(f"Komut algılanmadı, sessiz süre: {int(gecen_zaman)} saniye")
                    if gecen_zaman >= 6:  
                        break

main()
