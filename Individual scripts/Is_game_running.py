def is_game_running():
    try:
        for proc in psutil.process_iter(['name', 'status']):
            if proc.info['name'] and "eldenring.exe" in proc.info['name'].lower():
                if proc.info['status'] == psutil.STATUS_RUNNING:
                    return True
        return False
    except Exception as e:
        print(f"Error checking if game is running: {e}\n{traceback.format_exc()}")
        return False
