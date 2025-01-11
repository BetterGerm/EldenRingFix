def set_process_priority(pid):
    try:
        process = psutil.Process(pid)
        process.nice(psutil.HIGH_PRIORITY_CLASS)
        print(f"Process priority set to high for PID {pid}.")
    except psutil.AccessDenied:
        print(f"Failed to set process priority: Access is denied (pid={pid}). Ensure the script is run with administrator privileges.")
    except psutil.NoSuchProcess:
        print(f"Failed to set process priority: Process with PID {pid} does not exist.")
    except Exception as e:
        print(f"Unexpected error while setting process priority: {e}")
