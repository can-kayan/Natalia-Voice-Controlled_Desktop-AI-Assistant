import pyautogui
import time
import subprocess 
 
def bionluk_ac():  
    try:
        brave_path = r"C:\\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        subprocess.Popen([brave_path])   
        time.sleep(2)   
        pyautogui.hotkey('ctrl', 'l')  
        time.sleep(1)
        pyautogui.write('https://www.bionluk.com')  
        pyautogui.press('enter')   
        time.sleep(3)   
    except FileNotFoundError:
        print("Brave belirtilen konumda bulunamadı. Yolu kontrol edin.")
    except Exception as e:
        print(f"Brave'yu başlatırken bir hata oluştu: {e}")
 