def remove_unused_startup_programs():
    try:
        startup_keys = [
            r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
            r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
        ]
        for key_path in startup_keys:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ) as key:
                programs = []
                try:
                    i = 0
                    while True:
                        programs.append(winreg.EnumValue(key, i)[0])
                        i += 1
                except OSError:
                    pass  

            if programs:
                print("The following startup programs are configured:")
                for program in programs:
                    print(f" - {program}")
                choice = input("Do you want to disable all non-essential startup programs? (Y/N): ").strip().lower()
                if choice == 'y':
                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as write_key:
                        for program in programs:
                            winreg.DeleteValue(write_key, program)
                    print("Unused startup programs disabled successfully.")
                else:
                    print("Startup programs were not modified.")
    except Exception as e:
        print(f"Failed to manage startup programs: {e}")
