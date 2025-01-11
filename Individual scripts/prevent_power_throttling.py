def prevent_power_throttling():
    try:
        subprocess.run("powercfg /setactive SCHEME_MAX", shell=True, check=True)
        print("High-performance power plan activated to prevent power throttling.")
    except Exception as e:
        print(f"Failed to activate high-performance power plan: {e}")
