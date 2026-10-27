import os
import glob
import sys
import time
import urllib.request
import zipfile
import subprocess

def draw_noob():
    art = """
              ⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⣴⣶⣿⣿⣷⣤⡶⠿⡶⢦⡤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⢠⣿⣿⣩⣭⣽⣿⣿⣤⡿⣦⡈⢶⣝⣆⠀⠀⠀⠀⠀⠀⠀⠀
         ⢸⡟⢻⣿⣿⣿⠟⡍⣿⢤⣿⣿⣦⢹⣼⠀⠀⠀⠀⠀⠀⠀⠀
         ⠘⣿⢸⣿⠟⠁⠀⣷⢼⣾⣿⠘⣿⣧⢸⡀⠀⠀⠀⠀⠀⠀⠀
         ⢰⣿⣿⣿⠀⠀⠀⠉⠘⠋⠁⠀⣾⣦⡾⡇⠀⠀⠀⠀⠀⠀⠀
           ⠈⢿⡿⠀⠀⣦⠀⠀⢠⡆⠀⢻⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀
      ⣴⣶⣶⣤⣷⡀⠶⠈⠳⠶⠋⠀⢀⣾⣿⣶⣦⡀⠀⠀⠀⠀⠀⠀
     ⢠⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣷⣿⣆⠀⠀⠀⠀
     ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
    ⢰⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
   ⢠⠏⠀⠀⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠀⠀
 ⢀⣻⣴⠦⣄⣀⣹⣿⣿⣿⣿⠉⣿⣿⣿⣿⣿⣿⣿⣿⠉⠉⠁⠀⠀⢸⠀⠀
 ⣿⡤⠌⡟⠆⢀⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⡇⠀
 ⠳⣍⣠⣿⡷⠿⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣤⣧⣤⣤⣤⣌⡇⠀
 ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡆⣩⣑⣦⠈⢧⠀
 ⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠯⢴⣿⡗⣿⢀⣼⠇
 ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠻⠦⠝⠋⠁⠀
 ⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⣴⡋⠀⠈⢻⡿⣋⣼⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠷⣜⣦⡄⢀⣷⣿⣿⠏⠁⠉⢻⣿⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠈⠉⣏⢦⣀⡀⠀⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠾⠣⠖⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(art)

def find_roblox():
    local_app_data = os.getenv("LOCALAPPDATA")
    if not local_app_data:
        return None
    search_path = os.path.join(local_app_data, "Roblox", "Versions", "version-*", "RobloxPlayerBeta.exe")
    found_files = glob.glob(search_path)
    if found_files:
        return found_files[0]
    return None

def download_launcher_files():
    url = "https://github.com"
    zip_path = "stup_files.zip"
    extract_dir = os.path.join(os.environ["USERPROFILE"], "Desktop", "StupLauncher")

    print("[STUP SETUP]: Connecting to file server...")
    time.sleep(1.0)
    
    try:
        print("[STUP SETUP]: Downloading latest launcher files...")
        urllib.request.urlretrieve(url, zip_path)
        
        print("[STUP SETUP]: Extracting components...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            
        os.remove(zip_path)
        print(f"[STUP SETUP]: Files successfully saved to: {extract_dir}")
        return True
    except Exception as e:
        print(f"[ERROR]: Failed to download files. Reason: {e}")
        return False

def main():
    os.system("chcp 65001 > nul")
    os.system("cls" if os.name == "nt" else "clear")
    
    draw_noob()
    
    print("[STUP SETUP]: Initializing online installer...")
    time.sleep(1.0)
    
    if not download_launcher_files():
        input("\nPress Enter to close setup...")
        return
        
    print("[STUP SETUP]: Verifying Roblox configuration...")
    roblox_path = find_roblox()
    time.sleep(1.0)
    
    if roblox_path:
        print("[STUP SETUP]: SUCCESS. Roblox found.")
        print("[STUP SETUP]: Launching game client...")
        time.sleep(0.5)
        subprocess.Popen([roblox_path])
        print("[STUP SETUP]: Installation finished successfully!")
        time.sleep(3)
    else:
        print("[ERROR]: Roblox execution file not found.")
        input("\nPress Enter to close setup...")

if __name__ == "__main__":
    main()
import os
import glob
import sys
import time
import urllib.request
import zipfile
import subprocess

def draw_noob():
    art = """
              ⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⣴⣶⣿⣿⣷⣤⡶⠿⡶⢦⡤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
         ⢠⣿⣿⣩⣭⣽⣿⣿⣤⡿⣦⡈⢶⣝⣆⠀⠀⠀⠀⠀⠀⠀⠀
         ⢸⡟⢻⣿⣿⣿⠟⡍⣿⢤⣿⣿⣦⢹⣼⠀⠀⠀⠀⠀⠀⠀⠀
         ⠘⣿⢸⣿⠟⠁⠀⣷⢼⣾⣿⠘⣿⣧⢸⡀⠀⠀⠀⠀⠀⠀⠀
         ⢰⣿⣿⣿⠀⠀⠀⠉⠘⠋⠁⠀⣾⣦⡾⡇⠀⠀⠀⠀⠀⠀⠀
           ⠈⢿⡿⠀⠀⣦⠀⠀⢠⡆⠀⢻⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀
      ⣴⣶⣶⣤⣷⡀⠶⠈⠳⠶⠋⠀⢀⣾⣿⣶⣦⡀⠀⠀⠀⠀⠀⠀
     ⢠⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣷⣿⣆⠀⠀⠀⠀
     ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀
    ⢰⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
   ⢠⠏⠀⠀⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠀⠀
 ⢀⣻⣴⠦⣄⣀⣹⣿⣿⣿⣿⠉⣿⣿⣿⣿⣿⣿⣿⣿⠉⠉⠁⠀⠀⢸⠀⠀
 ⣿⡤⠌⡟⠆⢀⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⡇⠀
 ⠳⣍⣠⣿⡷⠿⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣤⣧⣤⣤⣤⣌⡇⠀
 ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡆⣩⣑⣦⠈⢧⠀
 ⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠯⢴⣿⡗⣿⢀⣼⠇
 ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠻⠦⠝⠋⠁⠀
 ⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⣴⡋⠀⠈⢻⡿⣋⣼⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠷⣜⣦⡄⢀⣷⣿⣿⠏⠁⠉⢻⣿⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠈⠉⣏⢦⣀⡀⠀⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠾⠣⠖⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(art)

def find_roblox():
    local_app_data = os.getenv("LOCALAPPDATA")
    if not local_app_data:
        return None
    search_path = os.path.join(local_app_data, "Roblox", "Versions", "version-*", "RobloxPlayerBeta.exe")
    found_files = glob.glob(search_path)
    if found_files:
        return found_files[0]
    return None

def download_launcher_files():
    url = "https://github.com"
    zip_path = "stup_files.zip"
    extract_dir = os.path.join(os.environ["USERPROFILE"], "Desktop", "StupLauncher")

    print("[STUP SETUP]: Connecting to file server...")
    time.sleep(1.0)
    
    try:
        print("[STUP SETUP]: Downloading latest launcher files...")
        urllib.request.urlretrieve(url, zip_path)
        
        print("[STUP SETUP]: Extracting components...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
            
        os.remove(zip_path)
        print(f"[STUP SETUP]: Files successfully saved to: {extract_dir}")
        return True
    except Exception as e:
        print(f"[ERROR]: Failed to download files. Reason: {e}")
        return False

def main():
    os.system("chcp 65001 > nul")
    os.system("cls" if os.name == "nt" else "clear")
    
    draw_noob()
    
    print("[STUP SETUP]: Initializing online installer...")
    time.sleep(1.0)
    
    if not download_launcher_files():
        input("\nPress Enter to close setup...")
        return
        
    print("[STUP SETUP]: Verifying Roblox configuration...")
    roblox_path = find_roblox()
    time.sleep(1.0)
    
    if roblox_path:
        print("[STUP SETUP]: SUCCESS. Roblox found.")
        print("[STUP SETUP]: Launching game client...")
        time.sleep(0.5)
        subprocess.Popen([roblox_path])
        print("[STUP SETUP]: Installation finished successfully!")
        time.sleep(3)
    else:
        print("[ERROR]: Roblox execution file not found.")
        input("\nPress Enter to close setup...")

if __name__ == "__main__":
    main()
