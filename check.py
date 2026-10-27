import os
import glob
import sys

def draw_art():
    art = """
⣠⠤⠤⠤⠶⡄⣯⣭⣭⣽⢠⠤⠤⠴⢤⡏⠉⣇⡤⠤⠤⠤⡄⢀⠀⢀⡴⠤⣄⡀
⡇⢰⣲⡆⠀⢻⠉⣥⣤⠈⣿⠀⡿⠖⢀⡇⠀⣿⠀⡖⢒⡖⢟⠉⠳⠋⢀⠴⠋⠀
⡇⢲⡄⢶⣒⡏⢸⣁⣸⠀⢸⠀⣖⡆⠉⣳⠀⣿⣀⣧⣸⠇⣸⠇⠀⡀⠙⠲⢤⣀
⣧⣘⡿⣄⣙⣿⡦⠤⠤⠴⠿⠤⠤⠤⠤⢷⡤⠤⠾⠤⠤⠤⠗⠦⡞⠙⠦⣄⡴⠋
    """
    print(art)

def get_roblox_path():
    local_app_data = os.getenv("LOCALAPPDATA")
    if local_app_data:
        versions_path = os.path.join(local_app_data, "Roblox", "Versions", "version-*")
        found = glob.glob(versions_path)
        if found:
            return found[0]
            
    program_files = os.getenv("ProgramFiles(x86)") or os.getenv("ProgramFiles")
    if program_files:
        versions_path_global = os.path.join(program_files, "Roblox", "Versions", "version-*")
        found_global = glob.glob(versions_path_global)
        if found_global:
            return found_global[0]
            
    return None

def verify_system():
    launcher_version = "1.0.0 Stable"
    print(f"Stup Launcher Version: {launcher_version}")
    
    roblox_dir = get_roblox_path()
    if not roblox_dir:
        print("ERROR: CRITICAL_MISSING_DIRECTORY")
        print("Reason: Roblox installation folder was not found on this PC.")
        sys.exit(1)
        
    version_name = os.path.basename(roblox_dir)
    print(f"Roblox Version: {version_name}")
    
    required_files = [
        "RobloxPlayerBeta.exe",
        "RobloxCrashHandler.exe",
        "shaders.dat"
    ]
    
    missing_files = []
    for file in required_files:
        full_path = os.path.join(roblox_dir, file)
        if not os.path.exists(full_path):
            missing_files.append(file)
            
    if missing_files:
        print("ERROR: CORRUPTED_INSTALLATION_FILES")
        print(f"Reason: Critical files are missing from Roblox folder: {', '.join(missing_files)}")
        sys.exit(1)
        
    print("Status: OK (All core files verified)")

def main():
    draw_art()
    verify_system()

if __name__ == "__main__":
    main()
