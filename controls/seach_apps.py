import os

def find_application_path(app_name):
    # Kullanıcıya özgü AppData dizinlerine göz atmak için kullanıcı adını almak
    user_profile = os.environ.get('USERPROFILE', '')
    
    # Önemli dizinler
    appdata_folders = [
        os.path.join(user_profile, 'AppData', 'Local'),
        os.path.join(user_profile, 'AppData', 'Roaming'),
        os.path.join(user_profile, 'AppData', 'LocalLow')
    ]
    
    # Program Files dizinlerini kontrol et (hem 64-bit hem de 32-bit için)
    program_files = [
        "C:\\Program Files", 
        "C:\\Program Files (x86)",
        "C:\\ProgramData",  # Çeşitli programların bazı ortak dosyaları burada olabilir
    ]
    
    # Microsoft Store Uygulama klasörleri (UWP) - genelde gizlidir
    microsoft_store_apps = [
        os.path.join("C:", "Program Files", "WindowsApps"),  # Bu klasör Microsoft Store uygulamaları için kullanılır
    ]
    
    # Tüm dizinlerde tarama yapmak
    directories_to_search = appdata_folders + program_files + microsoft_store_apps
    
    for folder in directories_to_search:
        # Dizindeki .exe dosyalarını taramak
        for root, dirs, files in os.walk(folder):
            for file_name in files:
                if app_name.lower() in file_name.lower() and file_name.endswith(".exe"):
                    return os.path.join(root, file_name)
    return None
