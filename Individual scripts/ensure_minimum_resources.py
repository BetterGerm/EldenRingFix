def ensure_minimum_resources():
    try:
        memory_info = psutil.virtual_memory()
        if memory_info.available < (memory_info.total * 0.2):
            print("Warning: Low system memory available. Close background applications.")
        else:
            print("System memory check passed.")
    except Exception as e:
        print(f"Failed to verify system resources: {e}")
