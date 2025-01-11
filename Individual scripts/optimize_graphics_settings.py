def optimize_graphics_settings():
    try:
        config_path = os.path.join(os.getenv('APPDATA'), "EldenRing")
        if os.path.exists(config_path):
            for root, _, files in os.walk(config_path):
                for file in files:
                    if file.endswith(".ini"):
                        settings_file = os.path.join(root, file)
                        with open(settings_file, "r") as f:
                            settings = f.readlines()
                        optimized_settings = []
                        for line in settings:
                            if "ScreenMode" in line:
                                optimized_settings.append("ScreenMode=Windowed\n")
                            elif "QualityLevel" in line:
                                optimized_settings.append("QualityLevel=Low\n")
                            elif "AntiAliasing" in line:
                                optimized_settings.append("AntiAliasing=None\n")
                            else:
                                optimized_settings.append(line)
                        with open(settings_file, "w") as f:
                            f.writelines(optimized_settings)
        print("Graphics settings optimized.")
    except Exception as e:
        print(f"Failed to optimize graphics settings: {e}")
