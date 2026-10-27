import os
import sys
import glob
import shutil

def find_roblox_textures():
    local_app_data = os.getenv("LOCALAPPDATA")
    if not local_app_data:
        return None
    
    search_path = os.path.join(local_app_data, "Roblox", "Versions", "version-*", "PlatformContent", "pc", "textures")
    found_folders = glob.glob(search_path)
    if found_folders:
        return found_folders[0]
    return None

def main():
    if len(sys.argv) < 2:
        return

    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        return

    texture_dir = find_roblox_textures()
    if not texture_dir:
        return

    skybox_files = [
        "sky51_bk.dds", "sky51_dn.dds", "sky51_ft.dds",
        "sky51_lf.dds", "sky51_rt.dds", "sky51_up.dds",
        "sky51_bk.png", "sky51_dn.png", "sky51_ft.png",
        "sky51_lf.png", "sky51_rt.png", "sky51_up.png"
    ]

    for filename in skybox_files:
        target_file = os.path.join(texture_dir, filename)
        if os.path.exists(target_file):
            try:
                shutil.copy(image_path, target_file)
            except:
                pass

if __name__ == "__main__":
    main()
