import os
import glob
import subprocess

def find_roblox():
    local_app_data = os.getenv("LOCALAPPDATA")
    if not local_app_data:
        return None
        
    search_path = os.path.join(local_app_data, "Roblox", "Versions", "version-*", "RobloxPlayerBeta.exe")
    found_files = glob.glob(search_path)
    
    if found_files:
        return found_files[0]
        
    program_files = os.getenv("ProgramFiles(x86)") or os.getenv("ProgramFiles")
    if program_files:
        search_path_global = os.path.join(program_files, "Roblox", "Versions", "version-*", "RobloxPlayerBeta.exe")
        found_global = glob.glob(search_path_global)
        if found_global:
            return found_global[0]
            
    return None

def main():
    roblox_path = find_roblox()
    
    if roblox_path:
        subprocess.Popen([roblox_path])
    else:
        print("Roblox not found")

if __name__ == "__main__":
    main()
