def check_and_disable_hibernation():
    try:
        subprocess.run("powercfg /hibernate off", shell=True, check=True)
        print("Hibernation disabled successfully.")
    except Exception as e:
        print(f"Failed to disable hibernation: {e}")
