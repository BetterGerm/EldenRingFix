def get_game_pid():
    try:
        exe_name = "eldenring.exe"
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] and exe_name in proc.info['name'].lower():
                return proc.info['pid']
        print("Failed to find the game process.")
        return None
    except Exception as e:
        print(f"Error retrieving game process: {e}")
        return None
