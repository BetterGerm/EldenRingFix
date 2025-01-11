def disable_fullscreen_optimizations():
    try:
        exe_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\ELDEN RING\\Game\\eldenring.exe"
        if not os.path.exists(exe_path):
            print("Elden Ring executable not found at the expected path.")
            print("Do you want to manually specify the path? (Y/N): ")
            choice = input().strip().lower()
            if choice == 'y':
                exe_path = input("Enter the full path to eldenring.exe: ").strip()
                if not os.path.exists(exe_path):
                    print("Invalid path provided. Fullscreen optimizations will not be disabled.")
                    return
            else:
                print("Fullscreen optimizations will not be disabled.")
                return

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Layers", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, exe_path, 0, winreg.REG_SZ, "~ DISABLEDXMAXIMIZEDWINDOWEDMODE")
        winreg.CloseKey(key)
        print("Fullscreen optimizations disabled.")
    except Exception as e:
        print(f"Failed to disable fullscreen optimizations: {e}")
